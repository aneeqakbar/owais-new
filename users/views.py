from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect("sheets:HomeView")

class RegisterView(View):
    def get(self, request):
        form = UserRegisterForm()
        return render(request, 'users/register.html', {'form': form})

    def  post(self, request):
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('users:login')
        return render(request, 'users/register.html', {'form': form})


class ProfileView(LoginRequiredMixin, View):
    def get(self, request):
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

        context = {
            'u_form': u_form,
            'p_form': p_form
        }

        return render(request, 'users/manage_profile.html', context)

    def post(self, request):
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            
            previous_url = request.META.get("HTTP_REFERER", None)
            
            if previous_url:
                return redirect(previous_url)
            return redirect('sheets:IndexView')
        context = {
            'u_form': u_form,
            'p_form': p_form
        }
        return render(request, 'users/manage_profile.html', context)
