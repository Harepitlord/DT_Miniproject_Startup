from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView, UpdateView
from .models import *
from django.urls import reverse_lazy, reverse
from . import forms


# Create your views here.

class Homepage(View):
    def get(self, request):
        render(request=request, template_name='startup/main.html')


class Profile(LoginRequiredMixin, View):
    def get(self, request):
        render(request=request, template_name='startup/profile.html')

    def post(self, request):
        pass


class Signup(CreateView):
    model = get_user_model()
    form_class = forms.NewUser
    template_name = 'startup/signup.html'
    success_url = reverse_lazy('startup:DashBoard')

    def form_valid(self, form):
        form.save(commit=True)
        user = authenticate(username=form.cleaned_data['email'], password=form.cleaned_data['password'])
        login(request=self.request, user=user)
        return redirect(to=self.success_url)


class DashBoard(LoginRequiredMixin, View):
    login_url = reverse_lazy('starup:Login')

    def get(self, request):
        return render(request=request, template_name='startup/home.html')


class Login(LoginView):
    template_name = 'startup/login.html'


class Logout(LogoutView):
    next_page = reverse_lazy('startup:HomePage')


class About(View):
    def get(self, request):
        render(request, 'startup/about.html')


class Post(LoginRequiredMixin, SuccessMessageMixin,CreateView):
    model = FeedPost
    form_class = forms.NewPost
    success_url = reverse_lazy('startup:DashBoard')
    template_name = 'startup/post.html'
    success_message = "Posted!!!"

    def form_valid(self, form):
        post = form.save(commit=False)
        post.senderId = self.request.user.id
        post.save()


class CompanyProfile(LoginRequiredMixin, View):
    def get(self, request):
        render(request=request, template_name='startup/editComDetail.html')


class Signup_old(View):
    def get(self, request):
        render(request=request, template_name='startup/signup.html')

    def post(self, request):
        if 'POST' in request:
            data = request['POST']
            user = User(Name=data['Name'], email=data['E-mail'], gender=data['gender'], mobile=data['mobile'], userName=data['Name'],
                        password=data['password'])
            user.save()
            redirect('startup:DashBoard')
        else:
            render(request=request, template_name='startup/signup.html')
