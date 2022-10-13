
from django.urls import path,include
from . import views

urlpatterns = [

    path("", views.employee_form,name='employee_insert'),
    path("<int:id>/",views.employee_form,name='employee_update'),
    path("list/", views.employee_List,name='employee_list')

]
