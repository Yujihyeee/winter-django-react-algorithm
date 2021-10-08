from django.conf.urls import url

from admin.crime import views

urlpatterns = {
    url(r'police_position', views.create_police_position),
    url(r'cctv', views.create_cctv_model),
    url(r'pop', views.create_population_model),
    url(r'new', views.merge_cctv_pop),
    url(r'cctv_pos', views.merge_cctv_position)

}
