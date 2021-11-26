from django.urls import path
from .views import (
    home, log_out, 
    login_page, 
    register_page,
    create_room, 
    room,
    delete_room,
    delete_message,
    update_room,
    user_profile,
    update_user,
)

app_name = 'base'

urlpatterns = [
    path('register_page/', register_page, name="register"),
    path('', home, name="home"),
    path('login_page/', login_page, name="login"),
    path('logout/', log_out, name="logout"),
    path('room_create/', create_room , name='new_room'),
    path('room/<int:pk>', room, name="room"),
    path('delete_room/<int:pk>', delete_room, name="delete_room"),
    path('delete_msg/<int:pk>', delete_message, name="delete_message"),
    path('update_room/<int:pk>', update_room, name="update_room"),
    path('profile/<int:pk>', user_profile, name="profile"),
    path('update_user/<int:pk>', update_user, name="update_user"),

]