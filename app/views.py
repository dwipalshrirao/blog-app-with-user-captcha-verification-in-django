from django.shortcuts import render
from django.contrib.auth import login, authenticate,logout  
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm,loginform
from django.shortcuts import render, redirect
from blogapp.models import blog

import random

@login_required(login_url='login')
def home_view(request):
    blogs=blog.objects.filter(author=request.user)
    return render(request, 'home.html',{'blog':blogs})
    

def signup_view(request):
    fno=random.randint(1,9)
    sno=random.randint(1,9)

    if request.method=='POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
        else:
            print(form.cleaned_data)
            # form = SignUpForm(request.POST,initial={'fno':str(fno),'sno':sno})
            form.data={'fno':fno,'sno':sno}
            # form.cleaned_data={**form.cleaned_data,'fno':fno,'sno':sno}
            print(form.cleaned_data)
            # print(form)
            print(form.__dict__)
            return render(request, 'signupform.html', {'form': form, 'fno':fno,'sno':sno})
            # form = SignUpForm({'fno':fno,'sno':sno})
    else:
        
        form = SignUpForm(initial={'fno':fno,'sno':sno})
        # print(form.__dict__)
    return render(request, 'signupform.html', {'form': form,'fno':fno,'sno':sno})


def login_view(request):
    if request.method=='POST':
        form=loginform(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('home')
            else:
                massege='password not matched'
                return render(request,'login.html',{'form':form,'massege':massege})   
        else:
            return render(request,'login.html',{'form':form})
    form=loginform()
    return render(request,'login.html',{'form':form})


@login_required(login_url='login')
def logout_view(request):
    
    logout(request)
    return redirect('login')