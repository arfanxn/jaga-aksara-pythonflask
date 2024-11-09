from flask import (g)
from forms import (StoreArticleForm)
from utilities.form_helpers import get_error_message
from utilities.file_helpers import get_extension_with_dot, image_to_webp
from utilities.hash_helpers import md5_current_timestamp
from models import Article, User
from http import HTTPStatus
from pony.orm import db_session, commit

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
                user = User[g.user.id]
            )
            commit()
            return article.to_json(), HTTPStatus.CREATED