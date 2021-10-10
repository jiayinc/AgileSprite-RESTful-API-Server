from rest_framework.authtoken.models import Token


def get_user_id(request):
    token = request.data.get('token')
    try:
        user_id = Token.objects.get(key=token).user_id
        return user_id
    except:
        return None
