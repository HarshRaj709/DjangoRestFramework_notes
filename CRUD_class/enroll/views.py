from django.shortcuts import render,redirect
from django.views import View
from .forms import UserForm
from django.contrib import messages
from .models import User

# Create your views here.
class Home(View):
    def get(self,request):
        fm = UserForm()
        info = User.objects.all()
        print(info)
        return render(request,'enroll/home.html',{'form':fm,'info':info})
    
    def post(self,request):
        fm = UserForm(request.POST)
        info = User.objects.all()
        if fm.is_valid():
            fm.save()
            messages.success(request,'Data saved successfully')
        return render(request,'enroll/home.html',{'form':fm,'info':info})
        
class UserInfoEdit(View):
    def get(self,request,pk):
        info = User.objects.get(pk=pk)
        fm = UserForm(instance=info)
        return render(request,'enroll/infoupdate.html',{'form':fm,'info':info})
    
    def post(self,request,pk):
        info = User.objects.get(pk=pk)
        fm = UserForm(request.POST,instance=info)
        if fm.is_valid():
            fm.save()
            messages.success(request,'Data Updated Successfully')
        return redirect('home')
    
class userdelete(View):
    def post(self,request,id):
        user = User.objects.get(id=id)
        user.delete()
        messages.success(request,'User deleted Successfully')
        return redirect('home')