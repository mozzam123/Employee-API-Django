# urls.py

from django.urls import path
from .views import *

urlpatterns = [
    path('create_employee/', EmployeeCreateView.as_view(), name='create_employee'),
    path('update_employee/', EmployeeUpdateView.as_view(), name='update_employee'),
]
