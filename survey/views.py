from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *

from django.views import View

class RegisterView(View):
    def get(self, request):
        return render(request, 'survey/register.html', { 'form': UserCreationForm() })

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect(reverse('login'))

        return render(request, 'survey/register.html', { 'form': form })


class LoginView(View):
    def get(self, request):
        return render(request, 'survey/login.html', { 'form':  AuthenticationForm })

    # really low level
    def post(self, request):
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = authenticate(
                request,
                username=form.cleaned_data.get('username'),
                password=form.cleaned_data.get('password')
            )

            if user is None:
                return render(
                    request,
                    'survey/login.html',
                    { 'form': form, 'invalid_creds': True }
                )

            try:
                form.confirm_login_allowed(user)
            except ValidationError:
                return render(
                    request,
                    'survey/login.html',
                    { 'form': form, 'invalid_creds': True }
                )
            login(request, user)

            return redirect(reverse('profile'))


class ProfileView(LoginRequiredMixin, View):
    def get(self, request):
        surveys = Post.objects.filter(author=request.user).all()

        context = {
          'surveys': surveys,
        }

        return render(request, 'survey/profile.html', context)

def post(self, request):
	form = AuthenticationForm(request, data=request.POST)
	if form.is_valid():
		try:
			form.clean()
		except ValidationError:
			return render(
				request,
				'survey/login.html',
				{'form': form, 'invalid_creds': True }
			)

		login(request, form.get_user())

		return redirect(reverse('profile'))

	return render(request, 'survey/login.html', { 'form': form })        

def homeView(request):
	return render(request, 'index.html')

def categoryDetail(request, slug):
    category = Category.objects.get(slug=slug)
    post = Post.objects.filter(category=category)
    print(post)
    context = {"objects": post}
    return render(request, "categories.html", context)

def postDetail(request, post_slug):
    if request.method == "POST":
        form = CommentForm(request.form)
        if form.is_valid():
            form.save()
    else:
        form = CommentForm()
        print("NONONO")
    post = Post.objects.get(slug=post_slug)
    context = {"object":post, "form":form}
    return render(request, "detail.html",context)    