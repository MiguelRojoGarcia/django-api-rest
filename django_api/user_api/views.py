import json
from http import HTTPStatus

from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from .application.user.use_cases.create_user import CreateUser
from .application.user.use_cases.delete_user import DeleteUser
from .application.user.use_cases.find_users import FindUsers
from .application.user.use_cases.get_user import GetUser
from .application.user.use_cases.update_user import UpdateUser
from .serializer import UserSerializer

class UserView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def _returnJsonUser(self, user: dict, many: bool = False, status: HTTPStatus = HTTPStatus.OK):
        return JsonResponse(UserSerializer(instance=user).data, status=status)
    def _validateInputUser(self, post_data: dict):
        if 'user' not in post_data:
            return False

        serializer = UserSerializer(data=post_data['user'])

        return serializer.is_valid()

    def _returnEmptyJsonResponse(self,status: HTTPStatus = HTTPStatus.OK):
        return JsonResponse({}, status=status)

    def get(self, request, id=None):
        if id is not None:
            user = (GetUser())(user_id=id)
            if user is not None:
                return self._returnJsonUser(user=user)
            else:
                return self._returnEmptyJsonResponse(status=HTTPStatus.NOT_FOUND)

        else:
            users = (FindUsers())()
            if len(users) > 0:
                return JsonResponse(UserSerializer(users, many=True).data, status=HTTPStatus.OK, safe=False)
            else:
                return JsonResponse([], status=HTTPStatus.OK, safe=False)

    def post(self, request):
        post_data = json.loads(request.body)

        if self._validateInputUser(post_data=post_data) is False:
            return self._returnEmptyJsonResponse(status=HTTPStatus.BAD_REQUEST)

        user = (CreateUser())(**post_data['user'])

        return self._returnJsonUser(user=user)

    def delete(self, request, id):
        user = (GetUser())(user_id=id)
        if user is not None:
            (DeleteUser())(user_id=id)
            return self._returnEmptyJsonResponse()
        return self._returnEmptyJsonResponse(status=HTTPStatus.BAD_REQUEST)

    def put(self, request, id):

        update_user = json.loads(request.body)

        if self._validateInputUser(post_data=update_user) is False:
            return self._returnEmptyJsonResponse(status=HTTPStatus.BAD_REQUEST)

        user = (GetUser())(user_id=id)

        if user is not None:
            user = (UpdateUser())(update_user=update_user, user_id=id)
            return self._returnJsonUser(user=user)

        return self._returnEmptyJsonResponse(status=HTTPStatus.NOT_FOUND)
