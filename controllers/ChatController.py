from flask import (g, jsonify, request, send_file)
from forms import (StoreChatForm)
from utilities.form_helpers import get_error_message
from utilities.file_helpers import get_extension_with_dot, image_to_webp, file_exists
from utilities.hash_helpers import md5_current_timestamp
from enums import ChatStatusEnum
from models import Chat, User
from http import HTTPStatus
from pony.orm import db_session, commit, select
from db import get_db

class ChatController:
    def store():
        form = StoreChatForm(request.form) 

        if form.validate() == False: 
            return {'message': get_error_message(form)}, HTTPStatus.BAD_REQUEST

        # TODO: implements chatbot with AI model
        answer = None;
        try: 
            answer = 'Lorem ipsum dolor sit amet.'
        except Exception as e:
            return {'message': 'Chatbot failed to respond.'}, HTTPStatus.BAD_REQUEST    

        with db_session: 
            chat = Chat(
                question = form.question.data,
                answer = answer,
                status = ChatStatusEnum.ACTIVE.value,
                user = User[g.user.id]
            )
            commit()
            return {'answer' : chat.answer}, HTTPStatus.CREATED
        
    def history():
        with db_session:
            limit = 8
            chats = select(c for c in Chat if c.status == ChatStatusEnum.ACTIVE.value) \
                .order_by(Chat.created_at) \
                .limit(limit)[:limit]
            return jsonify([{
                "id": chat.id,
                "question": chat.question,
                "answer": chat.answer,
            } for chat in chats]), HTTPStatus.OK
