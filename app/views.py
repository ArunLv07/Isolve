from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.views import View
from django.contrib.auth import authenticate, login, logout
from .models import Posts
from django.contrib.auth.mixins import LoginRequiredMixin

class Dashboard(View):
    def get(self,request):
        return render(request,'blog/dashboard.html')

class Register(View):
    def get(self,request):
        return render(request, 'blog/register.html')
    
    def post(self,request):
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User(first_name = first_name,last_name=last_name,email=email,username=username,password=password)
        user.save()
        return redirect('login')



class Login(View):
    def get(self,request):
        return render(request,'blog/login.html')
    
    def post(self,request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.filter(username=username,password=password).first()
        print(user)
        if user is not None:
            login(request, user)
            request.session['user'] = user.username
            return redirect('home')
        
class Logout(LoginRequiredMixin,View):
    login_url = 'login'
    def get(self,request):
        logout(request)
        return redirect('login')

class Home(LoginRequiredMixin,View):
    login_url = 'login'
    def get(self,request):
        posts = Posts.objects.all()
        return render(request,'blog/home.html',{'posts':posts})    
 
        
class MyPosts(LoginRequiredMixin,View):
    login_url = 'login'
    def get(self,request):
        posts = Posts.objects.all()
        user = request.session['user']
        return render(request,'blog/mypost.html',{'posts':posts,'user':user})

class AddPost(LoginRequiredMixin,View):
    login_url = 'login'
    def get(self,request):
        return render(request,'blog/add_post.html')
    
    def post(self,request):
        title = request.POST.get('title')
        content = request.POST.get('content')
        author = User.objects.filter(username=request.session['user']).first()

        post = Posts(title=title,content=content,author=author)
        post.save() 
        return redirect('myposts')
    
class EditPost(LoginRequiredMixin,View):
    login_url = 'login'
    def get(self,request,id):
        posts = Posts.objects.filter(id=id).first()
        return render(request,'blog/edit_post.html',{'posts':posts})
    
    def post(self,request,id):
        title = request.POST.get('title')
        content = request.POST.get('content')
    
        post = Posts.objects.filter(id=id).first()
        post.title = title
        post.content = content
        post.save()
        return redirect('myposts')

class DeletePost(LoginRequiredMixin,View):
    login_url = 'login'
    def get(self,request,id):
        posts = Posts.objects.filter(id=id).first()
        posts.delete()
        return redirect('myposts')
    