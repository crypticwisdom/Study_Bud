from api.views import get_routes, get_rooms, get_room
from django.urls import path

app_name = 'api'


urlpatterns = [
    path('', get_routes, name="get_routes"),
    path('rooms/', get_rooms, name="get_rooms"),
    path('room/<int:pk>', get_room, name="get_room")
]
