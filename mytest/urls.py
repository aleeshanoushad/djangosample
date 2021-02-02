from django.urls import path

from .import views

# urlpatterns = [
#     path('/hello', mytest.views.hello,name='hello')
# ] 
urlpatterns = [
    url(r'^$', views.hello, name='hello'),
]