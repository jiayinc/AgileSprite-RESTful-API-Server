# Create your views here.

from django.contrib import auth
from django.http import JsonResponse
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView

from common.code import *
from common.common import get_user_instance
from common.returnMsg import *
from .models import ExtendedUser as User


class InvalidPassword(Exception):
    message = MSG_INVALID_PASSWORD

    def __str__(self):
        return self.message


class InvalidEmail(Exception):
    message = MSG_INVALID_EMAIL

    def __str__(self):
        return self.message


def validate_password(password):
    import re
    reg = '^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,30}$'
    if (password is None) or (not re.match(reg, password)):
        raise InvalidPassword


# https://www.geeksforgeeks.org/check-if-email-address-valid-or-not-in-python/
def validate_email(email):
    import re
    # Make a regular expression
    # for validating an Email
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

    # pass the regular expression
    # and the string into the fullmatch() method
    if (email is None) or (not re.fullmatch(regex, email)):
        raise InvalidEmail


class LogOutViewSet(APIView):

    def post(self, request, *args, **kwargs):
        token = request.data.get('token')
        try:
            Token.objects.get(key=token).delete()
            return JsonResponse({"code": ACCOUNT_LOGOUT_SUCCESS,
                                 "msg": MSG_ACCOUNT_LOGOUT_SUCCESS})
        except:
            return JsonResponse({"code": ACCOUNT_TOKEN_ERROR,
                                 "msg": MSG_ACCOUNT_TOKEN_ERROR})
        # Token.objects.filter(key=token).delete()


class GetViewSet(APIView):

    def post(self, request, *args, **kwargs):
        user = get_user_instance(request)
        if user is None:
            return JsonResponse({"code": ACCOUNT_TOKEN_ERROR,
                                 "msg": MSG_ACCOUNT_TOKEN_ERROR})

        return JsonResponse({"code": ACCOUNT_GET_SUCCESS,
                             "msg": MSG_ACCOUNT_GET_SUCCESS,
                             "details": {
                                 'email': user.email,
                                 'birthday': user.birthday,
                                 'first_name': user.first_name,
                                 'last_name': user.last_name,
                             }})


class UpdateViewSet(APIView):

    def post(self, request, *args, **kwargs):
        token = request.data.get('token')
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')
        birthday = request.data.get('birthday')
        password = request.data.get('password')
        email = request.data.get('email')

        try:
            user_id = Token.objects.get(key=token).user_id
        except:
            return JsonResponse({"code": ACCOUNT_TOKEN_ERROR,
                                 "msg": MSG_ACCOUNT_TOKEN_ERROR})
        user_obj = User.objects.get(id=user_id)

        if first_name is not None:
            user_obj.first_name = first_name
        if last_name is not None:
            user_obj.last_name = last_name
        if birthday is not None:
            user_obj.birthday = birthday
        if password is not None:
            try:
                validate_password(password)
                user_obj.set_password(password)
            except InvalidPassword as e:
                return JsonResponse({"code": ACCOUNT_UPDATE_PASSWORD_INVALID,
                                     "msg": MSG_ACCOUNT_UPDATE_PASSWORD_INVALID})
        try:
            if email is not None:
                validate_email(email)

                user_obj.email = email
                user_obj.username = email
            user_obj.save()
        except Exception as e:
            if (type(e) == InvalidEmail) or ("account_extendeduser.username" in str(e)):
                return JsonResponse({"code": ACCOUNT_UPDATE_EMAIL_INVALID,
                                     "msg": MSG_ACCOUNT_UPDATE_EMAIL_INVALID})
            else:
                # Other unexpected errors occurred
                return JsonResponse({"code": ACCOUNT_UPDATE_FAIL,
                                     "msg": MSG_ACCOUNT_UPDATE_FAIL})

        return JsonResponse({"code": ACCOUNT_UPDATE_SUCCESS,
                             "msg": MSG_ACCOUNT_UPDATE_SUCCESS})


class RegisterViewSet(APIView):

    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')
        try:
            validate_password(password)
            validate_email(email)
            User.objects.create_user(username=email, password=password, email=email, first_name=first_name,
                                     last_name=last_name, birthday="1970-01-01")
        except InvalidPassword as e:
            return JsonResponse({"code": ACCOUNT_REGISTER_PASSWORD_INVALID,
                                 "msg": MSG_ACCOUNT_REGISTER_PASSWORD_INVALID})
        except Exception as e:
            if (type(e) == InvalidEmail) or ("account_extendeduser.username" in str(e)):
                return JsonResponse({"code": ACCOUNT_REGISTER_EMAIL_INVALID,
                                     "msg": MSG_ACCOUNT_REGISTER_EMAIL_INVALID})
            else:
                # Other unexpected errors occurred
                return JsonResponse({"code": ACCOUNT_REGISTER_ERROR,
                                     "msg": str(e)})

        return JsonResponse({"code": ACCOUNT_REGISTER_SUCCESS,
                             "msg": MSG_ACCOUNT_REGISTER_SUCCESS})


class LoginViewSet(APIView):

    def validate_user(self, request):
        pass

    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')
        try:
            validate_email(email)
            validate_password(password)
        except InvalidEmail:
            return JsonResponse({"code": ACCOUNT_LOGIN_EMAIL_INVALID,
                                 "msg": MSG_ACCOUNT_LOGIN_EMAIL_INVALID})
        except InvalidPassword:
            return JsonResponse({"code": ACCOUNT_LOGIN_PASSWORD_INVALID,
                                 "msg": MSG_ACCOUNT_LOGIN_PASSWORD_INVALID})

        user = auth.authenticate(username=email, password=password)
        if not user:
            return JsonResponse({"code": ACCOUNT_LOGIN_FAIL,
                                 "msg": MSG_ACCOUNT_LOGIN_FAIL})
        Token.objects.filter(user=user).delete()
        return JsonResponse({"code": ACCOUNT_LOGIN_SUCCESS,
                             "msg": MSG_ACCOUNT_LOGIN_SUCCESS,
                             "token": Token.objects.create(user=user).key})


class ForgotPasswordViewSet(APIView):

    def post(self, request, *args, **kwargs):

        email = request.data.get('email')

        if self.username_exists(email):
            usr = User.objects.get(username=email)
            name = usr.first_name + ' ' + usr.last_name
            pwd = self.generateRandomPwd()
            usr.set_password(pwd)
            usr.save()
            self.sendEmail(email, pwd, name)

            return JsonResponse({"code": ACCOUNT_USERNAME_EXIST,
                                 "msg": MSG_ACCOUNT_USERNAME_EXIST})
        else:
            return JsonResponse({"code": ACCOUNT_USERNAME_NOT_EXIST,
                                 "msg": MSG_ACCOUNT_USERNAME_NOT_EXIST})

    @staticmethod
    def username_exists(username):
        if User.objects.filter(username=username).exists():
            return True

        return False

    @staticmethod
    def sendEmail(to, pwd, name):
        import email
        import smtplib

        gmail_user = 'AgileSpriteCRM@gmail.com'
        gmail_password = 'vrsfctvtbkzjzisl'

        msg = email.message.Message()
        msg['From'] = gmail_user
        msg['To'] = to
        msg['Subject'] = "Agile Sprite CRM"
        msg.add_header('Content-Type', 'text')
        msg.set_payload(f"Hi, {name}. \n"
                        f"Your new temporary password for Agile Sprite CRM is: \n\n{pwd}\n\n"
                        f"Please login with your email {to} and reset your password ASAP. \n\n"
                        f"Login: http://www.agilespritecrm.com/login\n")

        try:
            smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            smtp_server.ehlo()
            smtp_server.login(gmail_user, gmail_password)
            smtp_server.sendmail(gmail_user, to, msg.as_string())
            smtp_server.close()
            print(f"Email successfully sent to {to} !")
        except Exception as ex:
            print(f"Something went wrong when sending email to {to}, {str(ex)}")

    @staticmethod
    def generateRandomPwd():
        import random
        import string
        pwd = []
        lower = string.ascii_lowercase
        upper = string.ascii_uppercase
        iterations = 4
        for i in range(iterations):
            pwd.append(lower[random.randint(0, len(lower) - 1)])
            pwd.append(upper[random.randint(0, len(upper) - 1)])
            pwd.append(str(random.randint(0, 9)))
        random.shuffle(pwd)
        return "".join(pwd)
