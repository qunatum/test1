from django.shortcuts import render,redirect

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm


# Create your views here.


def login(request):

    return render(request, 'login.html')

def signup(request):
    # if request.method == 'POST':
    #     form = UserCreationForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         username = form.cleaned_data.get('username')
    #         raw_password = form.cleaned_data.get('password1')
    #         user = authenticate(username=username, password=raw_password)
    #         login(request, user)
    #         return redirect('home')
    # else:
    #     form = UserCreationForm()
    #  return render(request, 'signup.html', {'form': form})
     return render(request, 'signup.html')


def home(request):
    return render(request,'home.html')

def logout_view(request):
    logout(request)
    # Redirect to a success page.