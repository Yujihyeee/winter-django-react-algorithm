from django.conf.urls import url

from admin.user import views

urlpatterns = {
    url(r'', views.users, name='users'),
    url(r'/login', views.login),
    url(r'/<slug:pk>', views.users),
    url(r'', views.users),
    url(r'', views.users),
    url(r'', views.users)
}
