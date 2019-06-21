from django.conf.urls import url
from impersonate.views import stop_impersonate

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^style-guide/', views.styleguide, name='styleguide'),
    url(r'^impersonate/(?P<uid>\d+)/', views.impersonate,
        name='impersonate-start'),
    url(r'^impersonate/stop/$', stop_impersonate,
        name='impersonate-stop'),
    url(r'^404', views.handle_404, name='handle-404'),
    url(r'^manifest\.json$', views.manifest, name='manifest'),
    url(r'^quiero-ser-distribuidor$', views.want_to_be_distributor, name='want_to_be_distributor'),
    url(r'^quienes-somos', views.who_we_are, name='who_we_are'),
    url(r'^contacto', views.contact, name='contact'),
]
