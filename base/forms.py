from django import forms
from django.db.models import fields
from django.forms import widgets
# from django.contrib.auth.models import User
from .models import User, Room
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm

# from django.forms import fields

class RoomForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
        "id":'room_name',
        'name':'room_name',
        'type': 'text',
        'placeholder':"E.g. Mastering Python + Django",
    }))

    topic = forms.CharField(widget=forms.TextInput(attrs={

        "id":'room_topic',
        'name':'topic',
        'type': 'text',
        'placeholder':"E.g. Django Features",
        'list':'topic-list'
    }))
            #   <!-- <textarea name="room_about" id="room_about" placeholder="Write about your study group..."></textarea> -->

    description = forms.CharField(widget=forms.Textarea(attrs={
        'id':'room_about',
        'name':'room_about',
        'placeholder':'Enter Room Description ...',
        'type':'textarea'
    }))
    class Meta:
        model = Room
        fields = ['name', 'topic', 'description']


class LoginForm(AuthenticationForm):

    email = forms.CharField(widget=forms.EmailInput(attrs={
        'id':'email',
        'placeholder':'email',
        'type':'email',
    }))

    password = forms.CharField(widget=forms.EmailInput(attrs={
        'id':'password',
        'placeholder':'Password',
        'type':'password',
    }))

    
class RegistrationForm(UserCreationForm):

    fullname = forms.CharField(widget=forms.TextInput(attrs={
        'name':'fullname',
        'id':'fullname',
        'type':'text',
        'placeholder':'Fullname',
    }))

    username = forms.CharField(widget=forms.TextInput(attrs={
        'id':'username',
        'placeholder':'Username',
        'name':'username',
        'type':'text',
    }))

    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'name':'email',
        'id':'email',
        'placeholder':'Email',
        'type':'email',
    }))

    password1 = forms.CharField(label='Password', widget=forms.TextInput(attrs={
        'id':"password",
        'name':"password",
        'type':"password",
        'placeholder':"&bull;&bull;&bull;&bull;&bull;&bull;&bull;&bull"
    })) 

    password2 = forms.CharField(label='Password Confirmation', widget=forms.TextInput(attrs={
        'id':"confirm_password",
        'name':"confirm_password",
        'type':"password",
        'placeholder':"&bull;&bull;&bull;&bull;&bull;&bull;&bull;&bull"
    }))


    class Meta:

        model = User
        fields = ['username', 'fullname', 'email', 'password1', 'password2']

# class LoginForm(AuthenticationForm):
#     class Meta:
#         model

# class UpdateForm()

class UserForm(forms.ModelForm):
    # <textarea name="bio" id="user_bio" placeholder="Write about yourself..."></textarea>
    # <input id="email" name="email" type="text" placeholder="E.g. john@email.com" />   
    # <input id="username" name="username" type="text" placeholder="E.g. John doe" /> 
    # <input id="username" name="username" type="text" placeholder="E.g. John doe" /> 

    fullname = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'Enter Fullname',
        'name':'fullname',
'id':'username',
'type':'text'
    }))


    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'Enter Username',
        'name':'username',
        'id':'username',
        'type':'text'
        
    }))

    
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder':'Enter Email',
        'name':'email',
        'id':'email',
        'type':'email'
    }))

    bio = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder':'Enter Bio',
        'name':'user_bio',
        'id':'user_bio',
        'type':'textarea',
    }))

    class Meta:

        model = User
        fields = ['fullname', 'username', 'email', 'bio', 'avatar']