from django.views.generic.base import RedirectView
from django.conf.urls import url, include
from django.contrib import admin
from user import views

urlpatterns = [
    url(r'^favicon\.ico$', RedirectView.as_view(url='/static/img/favicon.ico', permanent=True)),
    url(r'^robots\.txt', RedirectView.as_view(url='/static/robots.txt', permanent=True)),
    url(r'^register/$', views.RegisterFormView.as_view(), name='register'),
    url(r'^login/$', views.LoginFormView.as_view(), name='login'),
    url(r'^logout/$', views.LogoutView.as_view(), name='logout'),
    url(r'^admin/', admin.site.urls),
    url(r'', include('user.urls')),
    url(r'', include('database.urls')),
    url(r'', include('content.urls')),
    url(r'', include('test.urls')),
]
