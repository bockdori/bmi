from django.urls import path
from .views import index, bmi_list, bmi_enter, bmi_update, bmi_detail, bmi_delete
urlpatterns = [
    #path(url pattern, view, name)
    #path("", index, name='main'),
    path("", bmi_list, name="list"),
    path("enter/", bmi_enter, name="enter"),
    path("update/<int:pk>", bmi_update, name="update"),
    path("detail/<int:pk>", bmi_detail, name='detail'),
    path("delete/<int:pk>", bmi_delete, name='delete'),
]