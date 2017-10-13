
from django.conf.urls import url
import views

urlpatterns = [
    url(r'get_student_soap$', views.get_student_soap),
]

