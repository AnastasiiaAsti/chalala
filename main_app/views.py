from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Profile, Chat

# Create your views here.


def home(request):
    return render(request, 'home.html')


@login_required
def about(request):
    return render(request, 'about.html')


@login_required
def profile(request):
    profile = Profile.objects.all()
    return render(request, 'profile.html', {'profile': profile})


def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)


def chats_index(request):
    chats = Chat.objects.all()
    return render(request, 'chats/index.html', {'chats': chats})


class ChatDetail(DetailView):
    model = Chat


class ChatDelete(LoginRequiredMixin, DeleteView):
    model = Chat
    success_url = '/chats/'


class ChatUpdate(LoginRequiredMixin, UpdateView):
    model = Chat
    fields = '__all__'


class ChatCreate(LoginRequiredMixin, CreateView):
    model = Chat
    fields = '__all__'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
