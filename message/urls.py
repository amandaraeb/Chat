from django.urls import path

from message import views

urlpatterns = [
    path('', views.compose),
    path('received/', views.received)
]
