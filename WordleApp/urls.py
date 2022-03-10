from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('play', views.gameView, name='play'),
    path('handleSubmit', views.handleSubmit, name='handleSubmit')
]