from django.conf.urls import url

from admin.crime import views

urlpatterns = {
    url(r'crime-model', views.create_police_position)
}