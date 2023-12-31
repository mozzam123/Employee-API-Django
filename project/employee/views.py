from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import EmployeeSerializer
from .models import Employee

class EmployeeCreateView(APIView):
    def post(self, request):
        try:
            data = request.data
            input_email = data.get('email')

            # Check if required parameters are present
            required_params = ['name', 'email', 'age', 'gender', 'addressDetails', 'workExperience', 'qualifications', 'projects']
            missing_params = [param for param in required_params if param not in data]
            if missing_params:
                return Response({"message": "invalid body request", "success": False}, status=status.HTTP_400_BAD_REQUEST)


            # Check if email already exists
            if Employee.objects.filter(email=input_email).exists():
                return Response({"message": "Employee already exists", "success": False}, status=status.HTTP_400_BAD_REQUEST)
            
            serializer = EmployeeSerializer(data=request.data)

            if serializer.is_valid():
                employee_instance = serializer.save()
                response_data = {
                    "message": "Employee created successfully",
                    "regid": f"EMP{employee_instance.id:03d}",
                    "success": True
                }
               
                return Response(response_data, status=status.HTTP_200_OK)
            else:
                return Response({"message": "Invalid body request", "errors": serializer.errors, "success": False}, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            response_data = {
                "message": "Employee creation failed",
                "success": False
            }
            return Response(response_data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class EmployeeUpdateView(APIView):
    def put(self, request):
        try:
            data = request.data
            input_regid = data.get('regid')

            # Check if required parameters are present
            required_params = ['regid', 'name', 'email', 'age', 'gender', 'addressDetails', 'workExperience', 'qualifications', 'projects']
            missing_params = [param for param in required_params if param not in data]
            if missing_params:
                return Response({"message": "Invalid body request", "success": False}, status=status.HTTP_400_BAD_REQUEST)

            # Retrieve the employee instance
            try:
                queryset = Employee.objects.get(id=input_regid)
                print("queryset: ", queryset)
            except Employee.DoesNotExist:
                return Response({"message": f"No employee found with regid", "success": False}, status=status.HTTP_200_OK)

            serializer = EmployeeSerializer(queryset, data=data, partial=True, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                response_data = {
                    "message": "Employee details updated successfully",
                    "success": True
                }
                return Response(response_data, status=status.HTTP_200_OK)
            else:
                print("not valid")
                return Response({"message": "Employee details updation failed", "errors": serializer.errors, "success": False}, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            response_data = {
                "message": "Employee updation failed",
                "success": False,
            }
            return Response(response_data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

class EmployeeDeleteView(APIView):
    def delete(self, request):
        try:
            data = request.data
            input_regid = data.get('regid')

            # Check if required parameters are present
            if not input_regid:
                return Response({"message": "Invalid body request", "success": False}, status=status.HTTP_400_BAD_REQUEST)

            # Retrieve the employee instance
            try:
                employee_instance = Employee.objects.get(id=input_regid)
            except Employee.DoesNotExist:
                return Response({"message": f"No employee found with regid", "success": False}, status=status.HTTP_200_OK)

            # Delete the employee
            employee_instance.delete()

            response_data = {
                "message": "Employee deleted successfully",
                "success": True
            }
            return Response(response_data, status=status.HTTP_200_OK)

        except Exception as e:
            response_data = {
                "message": "Employee deletion failed",
                "success": False
            }
            return Response(response_data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class EmployeeGetView(APIView):
    def get(self, request):
        try:
            params = request.query_params
            regid = params.get('regid')

            if regid:
                # Single employee request
                try:
                    queryset = Employee.objects.get(id=regid)
                    serializer = EmployeeSerializer(queryset)
                    response_data = {
                        "message": "Employee details found",
                        "success": True,
                        "employees": [serializer.data]
                    }
                except Employee.DoesNotExist:
                    response_data = {
                        "message": "Employee details not found",
                        "success": False,
                        "employees": []
                    }
            else:
                # All employee request
                queryset = Employee.objects.all()
                serializer = EmployeeSerializer(queryset, many=True)
                response_data = {
                    "message": "Employee details found",
                    "success": True,
                    "employees": serializer.data
                }

            return Response(response_data, status=status.HTTP_200_OK)

        except Exception as e:
            response_data = {
                "message": "Employee retrieval failed",
                "success": False,
                "employees": []
            }
            return Response(response_data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


