from django.contrib.auth.password_validation import password_changed
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from .forms import RegistrationForm, LoginForm, RoomForm, UserForm
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from base.models import Room, Message, Topic, User
from django.db.models import Q
from django.contrib import messages

# from django.urls import 

# Create your views here.

def register_page(request):
    if request.user.is_authenticated:
        return redirect('base:home')
        
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            return redirect('base:login')
            
    return render(request, 'base/auths.html', {
        'form':form,
        'auth_type':'register',
    })


@login_required(login_url='base:login')
def home(request):
    rooms = Room.objects.all()
    topics = Topic.objects.all()[:5]
    all_messages = Message.objects.all().order_by('-created')
    if request.method == 'GET' and 'q' in request.GET:
        # print(request.GET['q'])

        query_string = request.GET.get('q') if request.GET['q'] else ''
        # rooms = Room.objects.filter(name__icontains=query_string) or \
        #     Room.objects.filter(topic__name__icontains=query_string) or \
        #         Room.objects.filter(description__icontains=query_string)

        rooms = Room.objects.filter(
            Q(name__icontains=query_string) |
            Q(topic__name__icontains=query_string) |
            Q(description__icontains=query_string)
        )

    return render(request, 'base/home.html', {
        'rooms':rooms,
        'topics':topics,
        'all_messages':all_messages,
    })


@login_required(login_url='base:login')
def create_room(request):
    topics = Topic.objects.all()
    form = RoomForm()

    if request.method == 'POST':
        room_name = request.POST['name']
        room_topic = request.POST['topic']
        room_description = request.POST['description']

        # This method creates or gets a record in the db, it returns true if the record is newly created.
        topic, created = Topic.objects.get_or_create(name = room_topic)

        # print(topic, created)
        room_object = Room(name=room_name, host=request.user, topic=topic, description=room_description)
        room_object.save()

        messages.success(request, f'Successfully Created {room_name}')

        return redirect(reverse('base:home'))
        
    return render(request, 'base/room_cu.html', {
        'form':form,
        'topics':topics,
    })


@login_required(login_url='base:login')
def room(request, pk):
    room = get_object_or_404(Room, pk=pk)
    room_messages = room.message_set.all()
    participants = room.participants.all()

    if request.method == 'POST' and 'message' in request.POST:
        message = request.POST['message']
        message_obj = Message(user=request.user, room=room, body=message)
        message_obj.save()

        room.participants.add(request.user)

        
    return render(request, 'base/room.html', {
        'room':room,
        'room_messages':room_messages,
        'participants':participants,
    })


def login_page(request):
    if request.user.is_authenticated:
        return redirect('base:home')

    form = LoginForm()
    if request.method == 'POST':
        # print(request.POST)
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request.POST, email=email, password=password)
        print(user, email, password)

        if user is not None:
            login(request, user)

            return redirect('base:home')
    return render(request, 'base/auths.html', {
        'form':form,
        'auth_type':'login'
    })


@login_required(login_url='base:login')
def delete_room(request, pk):
    obj = get_object_or_404(Room, pk=pk)
    if request.method == 'POST':
        obj.delete()
        messages.success(request, f'Successfully deleted "{obj}". ')
        return redirect(reverse('base:home'))
    return render(request, 'base/delete.html', {
        'obj':obj,
    })


@login_required(login_url='base:login')
def delete_message(request, pk):
    obj = get_object_or_404(Message, pk=pk)
    room_id = obj.room.id
    print(room_id)
    if request.method == 'POST':
        obj.delete()
        messages.success(request, f'Successfully deleted "{obj}"')
        return redirect(reverse('base:room', args=(room_id, )))
    return render(request, 'base/delete.html', {
        'obj':obj,
    })

@login_required(login_url='base:login')
def update_room(request, pk):
    room = Room.objects.get(id=pk)
    if request.user != room.host:
        return HttpResponse(f'So sorry {request.user}, you are not allowed to make updates.')
    
    topics = Topic.objects.all()
    form = RoomForm(initial={'name':room.name, 'topic':room.topic, 'description':room.description})
    if request.method == 'POST':
        # print(request.POST)

        topic_name = request.POST.get('topic')
        topic, created = Topic.objects.get_or_create(name=topic_name)
        room.name = request.POST.get('name')
        room.topic = topic
        room.description = request.POST.get('description')
        room.save()
        messages.success(request, f'Successfully updated "{room}" room.')
        return redirect(reverse('base:room', args=(room.id,)))
    return render(request, 'base/room_cu.html', {
        'room':room,
        'form':form,
        'topics':topics,
    })

@login_required(login_url='base:login')
def user_profile(request, pk):
    user = User.objects.get(pk=pk)
    rooms = user.room_set.all()
    topics = Topic.objects.all()[:5]
    all_messages = user.message_set.all().order_by('-created')
    return render(request, 'base/profile.html', {
        'users':user,
        'topics':topics,
        'all_messages':all_messages,
        'rooms':rooms,
    })
    

@login_required(login_url='base:login')
def update_user(request, pk):
    user = get_object_or_404(User, pk=pk)

    form = UserForm(instance=user)

    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect(reverse('base:profile', args=(user.id,)))
        print(request.POST, request.FILES)
    return render(request, 'base/update_user.html', {
        'users':user,
        'form':form,
    })


def log_out(request):
    logout(request)
    return redirect('/login_page/')