from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from testapp.forms import SignupForm
from django.http import HttpResponseRedirect

# Create your views here.
def home_view(request):
    return render(request,'home.html')




@login_required
def python_view(request):
    return render(request,'python.html')
@login_required
def java_view(request):
    return render(request,'java.html')
@login_required
def aptitude_view(request):
    return render(request,'aptitude.html')

def signup_view(request):
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(user.password) # to hash password
            user.save()
            return HttpResponseRedirect('/accounts/login')
    return render(request,'signup.html',{'form':form})

