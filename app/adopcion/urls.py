from django.conf.urls import url
from app.adopcion.views import index

urlpatterns = [
    url(r'^$', index, name='index')
]
