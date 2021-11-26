from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from api.serializers import RoomSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import Room



@api_view(['GET'])
def get_routes(request):
    routes = [
        'GET /api/',
        'GET /api/rooms/',
        'GET /api/room/:id',
    ]
    return Response(routes)

@api_view(['GET'])
def get_rooms(request):
    rooms = Room.objects.all()
    serializer = RoomSerializer(rooms, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_room(request, pk):
    room = get_object_or_404(Room, pk=pk)
    serializer = RoomSerializer(room, many=False)
    return Response(serializer.data)
