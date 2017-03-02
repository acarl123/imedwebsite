from django.conf.urls import url
from django.contrib import admin
import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^contact$', views.contact, name='contact'),
    url(r'^acuity/$', views.acuity, name='acuity'),

]
