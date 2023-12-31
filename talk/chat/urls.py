from django.urls import path
from . import views

app_name = 'chat'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<slug:slug>/', views.ChatRoomView.as_view(), name='chatroom'),
]
