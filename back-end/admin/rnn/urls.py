from django.conf.urls import url
from admin.rnn import views

urlpatterns = {
    url(r'price', views.ram_price),
    url(r'kia_predict', views.kia_predict)

}