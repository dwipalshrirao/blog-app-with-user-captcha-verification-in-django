from django.shortcuts import render,redirect
from .forms import blogForm
from django.contrib.auth.models import User
from .models import blog
# Create your views here.

def create_blog(request):
    if request.method=='POST':
        form = blogForm(request.POST or None, request.FILES or None) 
        print(request.user.__dict__)

        if form.is_valid(): 
            print(request.user,'uae')
            form=form.save(commit=False)
            user=User.objects.get(username=request.user.username)
            form.author = request.user
            
            form.save() 
        else:
            return render(request,'create_blog.html',{'form':form})
    form = blogForm()
    return render(request,'create_blog.html',{'form':form})


def single_blog(request,id):
    sblog=blog.objects.get(id=id)
    return render(request,'single_blog.html',{'blog':sblog})


def search_blog(request):
    if request.method=='POST':
        username=request.POST.get('search')
        try:
            author=User.objects.get(username=username)
            blogs=blog.objects.filter(author=author,status='public')
            return render(request,'search.html',{'blog':blogs,'author':author})
        except:
            return render(request,'search.html',{'massege':"User '{}' doesn't exist".format(username)})
    return render(request,'search.html',{'massege':'You havent search anything'})



def delete_blog(request,id):
    blog.objects.filter(id=id).delete()
    return redirect('home')


def update_blog(request,id):
    
        instance=blog.objects.get(id=id)
    # if request.method=='POST':
        form = blogForm(request.POST or None, request.FILES or None,instance=instance) 
        # print(request.user.__dict__)

        if form.is_valid(): 
            
            form=form.save(commit=False)
            user=User.objects.get(username=request.user.username)
            form.author = request.user
            
            form.save() 
            return redirect('home')
        else:
            return render(request,'create_blog.html',{'form':form})
    
    # form = blogForm(instance=instance)
    # return render(request,'create_blog.html',{'form':form})