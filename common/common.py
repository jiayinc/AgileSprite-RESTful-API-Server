from rest_framework.authtoken.models import Token
from account.models import ExtendedUser as User

def get_user_id(request):
    token = request.data.get('token')
    try:
        user = Token.objects.get(key=token).user_id
        return user
    except:
        return None

def get_user_instance(request):
    token = request.data.get('token')
    try:
        user_id = Token.objects.get(key=token).user_id
        user = User.objects.get(id=user_id)
        return user
    except:
        return None

