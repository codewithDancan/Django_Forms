from django.urls import path
from . import views 

urlpatterns = [
    path('', views.employee_data, name='employee_data'),
]
