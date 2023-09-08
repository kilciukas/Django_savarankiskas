from django.urls import path, include
from django.views import generic

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('publishers/', views.PublisherView.as_view(), name='publishers'),
    path('publisher/<int:pk>',
         views.PublisherDetailView.as_view(), name='publisher'),
    path('games/', views.GameListView.as_view(), name='games'),
    path('game/<int:pk>', views.GameDetailView.as_view(), name='game'),
    path('i18n/', include('django.conf.urls.i18n'))
]
