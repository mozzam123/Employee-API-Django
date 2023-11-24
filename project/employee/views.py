from rest_framework.views import APIView
from django.http import JsonResponse
from .serializers import *
from rest_framework.status import *
# Create your views here.

class createUserView(APIView):
    def post(self, request):
        response = {"status": "success", "errorcode": "",
                            "reason": "", "result": "", "httpstatus": HTTP_200_OK}
        try:
            data = request.data
            serializer = UserSerializer(data=data)
            if serializer.is_valid():
                response['status'] = "success"
                response['reason'] = "User Created"

            else:
                response["status"] = "not valid"
                response['reason'] = serializer._errors
        except Exception as e:
            response["status"] = "Error"
            response['reason'] = str(e)

        return JsonResponse(response)