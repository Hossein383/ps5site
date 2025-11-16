from django.shortcuts import render, redirect
from . import models
from . import forms
from django.contrib.auth import login, authenticate  , logout
from django.contrib.auth.models import User

def index(request):
    return render(request, 'games/index.html')


def listgames(request):
    ListGamesModel = models.Game.objects.all()
    return render(request, 'games/listgames.html', context={"lists": ListGamesModel})


def detailsgame(request, id):
    DetailsGameModel = models.Game.objects.get(id=id)
    ListCommentModel = models.Comment.objects.filter(game=DetailsGameModel)
    if request.method == "POST":
        form = forms.CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.game = DetailsGameModel
            comment.name = request.user
            comment.save()
            return redirect('Details', id=id)
    elif request.method == "GET":
        form = forms.CommentForm()
    return render(request, 'games/detailsgame.html', context={"DetailsGameModel": DetailsGameModel, "ListCommentModel": ListCommentModel, "form": form})


def LoginUser(request):
    if request.user.is_authenticated:
        return redirect('ListGames')
    
    if request.method == "POST":
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('ListGames')
            else:
                return redirect('login')
        return render(request, 'games/login.html', context={'form': form})
    elif request.method == "GET":
        form = forms.LoginForm()
        return render(request, 'games/login.html', context={'form': form})

def Register(request):
    if request.user.is_authenticated:
        return redirect('ListGames')

    if request.method == "POST":
        form = forms.SingUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            user = User.objects.create_user(username=username , email=email , password=password)
            return redirect('login')
        return render(request , 'games/Register.html' , context={'form':form})  
    elif request.method == "GET":
        form = forms.SingUpForm()
        return render(request , 'games/Register.html' , context={'form':form})  

def logoutuser(request):
    logout(request)
    return redirect('index')