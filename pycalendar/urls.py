from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('month/<int:year>/<int:month>/<str:language>/', views.month, name='month')
]