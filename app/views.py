from app.forms import ProfileForm, ServiceRequestForm
from typing import ContextManager
from django.shortcuts import render, redirect
from .models import  Human_Resource, Profile, ServiceRequest
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
def homeview(request):
    ctx ={'title':'welcome'}
    return render(request,'index.html',context= ctx)

def welcomeview(request):
    return render(request,'welcome.html')

def ordering(request):
        return render(request,'ordering.html')

def view_hr(request):
    hr= Human_Resource.objects.all()
    context = {'hr':hr}
    return render(request,'hr/view.html',context)  

def detail_hr(request,pk):
    hr= Human_Resource.objects.get(pk=pk)
    context = {'hr':hr}
    return render(request,'hr/detail.html',context)

def purchase(request):
    return render(request,'purchase/purchase.html')

def rent(request):
    return render(request,'rent_services/rent.html')

def service_request(request,pk):
    hr=Human_Resource.objects.filter(pk=pk)[0]
    form = ServiceRequestForm()
    if request.method=='POST':
        form = ServiceRequestForm(request.POST)
        if form.is_valid():
            fd = form.save(commit = False)
            fd.hr=hr
            fd.for_user = request.user
            fd.save()
            messages.success(request,"Service request has been sent") 
            return redirect('home')
    context = {'form':form}
    return render(request,'hr/request_form.html', context)


def user_profile(request):
    return render(request, 'user_profile/user.html')

def equipment(request):
    return render(request,'equipment/equipment.html')

@login_required
def user_profileview(request):
    users = Profile.objects.filter(user__pk=request.user.pk)
    if len(users)==1:
        context= {'userprofile':users}
    else:
        context = {'userprofile': None}
    return render(request, 'user_profile.html',context)

def edit_profileview(request, pk):
    try:
        udata = Profile.objects.filter(pk=pk)
        if len(udata)==1:
            form = ProfileForm(instance=udata[0])
        else:
            form = ProfileForm()
        if request.method=='POST':
            if len(udata)==1:
                form = ProfileForm(request.POST, request.FILES, instance=udata[0])
            else:
                form = ProfileForm(request.POST, request.FILES)
            if form.is_valid():
                fd=form.save(commit=False)
                fd.user=request.user
                fd.email=request.user.email
                fd.save()
                return redirect('up')
        
        context = {"pform":form}
        return render(request, 'edit_profile.html', context)
    except Exception as e:
        print('some error occurred',e)
        return redirect('up')

def about(request):
    return render(request,'about.html')
