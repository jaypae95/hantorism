from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Post,User
from .forms import UserForm
def list(request):
    posts=Post
    return render(request, 'list.html', {'post':posts})

def who(request):
    who_list=User.object.order_by('name')
    context = {'who_list':who_list}
    return render(request,'who.html',context)
def who_detail(request, ID):
    person=User.object.get(pk=ID)
    context={'who':person}
    return render(request,'detail.html',context)

def join(request):
    if request.method =='POST':
        form=UserForm(request.POST)
        if form.is_valid():
            obj=User(ID=form.data['ID'],
                     PW=form.data['PW'],
                     name=form.data['name'],
                     studentNum=form.data['studentNum'],
                     major=form.data['major'],
                     gender=form.data['gender'],
                     email=form.data['email'],
                     isHantor=form.data['isHantor'])
            obj.save()
            return HttpResponse('success')
        return HttpResponse('fail')
    else:
        form=UserForm()
        print(13)
    return render(request,'join.html',{'form':form,})