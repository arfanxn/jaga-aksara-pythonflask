from flask import (g, request, send_file)
from forms import (StoreArticleForm)
from utilities.form_helpers import get_error_message
from utilities.file_helpers import get_extension_with_dot, image_to_webp, file_exists
from utilities.hash_helpers import md5_current_timestamp
from models import Article, User
from http import HTTPStatus
from pony.orm import db_session, commit, select
from db import get_db

class ArticleController:
    def store():
        form = StoreArticleForm() 

        if form.validate() == False: 
            return {'message': get_error_message(form)}, HTTPStatus.BAD_REQUEST
        
        title = form.title.data
        thumbnail = form.thumbnail.data
        saved_thumbnail_filename = md5_current_timestamp() 
        saved_thumbnail_ext = get_extension_with_dot(thumbnail.filename)
        thumbnail.save('images/temps/' + saved_thumbnail_filename + saved_thumbnail_ext)
        content = form.content.data
        saved_content_filename = md5_current_timestamp()
        saved_content_ext = get_extension_with_dot(content.filename)
        content.save('contents/articles/' + saved_content_filename + saved_content_ext)

        image_to_webp(
            'images/temps/' + saved_thumbnail_filename + saved_thumbnail_ext, 
            'images/articles/' + saved_thumbnail_filename + '.webp', quality=85
        )

        with db_session: 
            article = Article(
                title = title,
                thumbnail = saved_thumbnail_filename,
                content = saved_content_filename,
                author = User[g.user.id]
            )
            commit()
            return article.to_json(), HTTPStatus.CREATED
        
    def index():
        db = get_db()
        with db_session:
            sql_query = '''
                SELECT a.id, a.title, a.thumbnail, u.name AS author_name FROM articles a
                JOIN users u ON a.user_id = u.id '''
            if 'popular' in request.args: 
                sql_query += '''
                ORDER BY 
                CASE 
                    WHEN impression > 0 THEN view_time / impression 
                    ELSE NULL 
                END DESC '''
            sql_query += '''LIMIT 6; '''
            
            cursor = db.execute(sql_query)
            results = cursor.fetchall()
            column_names = [column[0] for column in cursor.description]
            rows = [dict(zip(column_names, row)) for row in results]
            return rows, HTTPStatus.OK

    def get ():
        id = request.args.get('id') # article id

        with db_session:
            article = select(a for a in Article if a.id == id).prefetch(Article.author).first()

            if article == None: 
                return {'message': 'Data not found.'}, HTTPStatus.NOT_FOUND
        
            return article.to_json(), HTTPStatus.OK

    def download_thumbnail (): 
        filename = request.args.get('file')
        filepath = 'images/articles/' + filename + '.webp'
        
        if (file_exists(filepath) == False):
            return {'message': 'Data not found.'}, HTTPStatus.NOT_FOUND
        
        return send_file(filepath, as_attachment=True)

    def download_content (): 
        filename = request.args.get('file')
        filepath = 'contents/articles/' + filename + '.pdf'
        
        if (file_exists(filepath) == False):
            return {'message': 'Data not found.'}, HTTPStatus.NOT_FOUND
        
        return send_file(filepath, as_attachment=True)
