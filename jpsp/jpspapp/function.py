from .models import stars, message, post_request


class admin_content:
    def get_base_content(self):
        message_list = message.objects.all()
        post_request_list = post_request.objects.all()
        base_content = {
            'username': '社团部',
            'message_list_all': message_list,
            'post_request_list': post_request_list,
            'message_unread_num': '0',
            'post_request_num': '0',
        }
        return base_content