from django.conf.urls import url

from admin.crime import views

urlpatterns = {
    url(r'police_position', views.create_police_position),
    url(r'cctv', views.create_cctv_model),
    url(r'pop', views.create_population_model)
}
