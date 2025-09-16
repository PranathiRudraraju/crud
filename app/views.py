from django.shortcuts import redirect, render

from app.models import student

from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
@login_required
def index(request):
    data=student.objects.all()
    return render(request,'app/index.html',{'data':data})
def insertdata(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        age=request.POST.get('age')
        gender=request.POST.get('gender')
        query=student(name=name,email=email,age=age,gender=gender)
        query.save()
        return redirect("/")
    return render(request,'app/index.html')
def updateData(request,id):
    d=student.objects.get(id=id)
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        age=request.POST.get('age')
        gender=request.POST.get('gender')
        x=student.objects.get(id=id)
        x.name=name
        x.email=email
        x.age=age
        x.gender=gender
        x.save()
        return redirect('/')
    return render(request,'app/edit.html',{'d':d})
def deleteData(request,id):
    d=student.objects.get(id=id)
    d.delete()
    return redirect('/')
def register(request):
 if request.method=='POST':
    form=UserCreationForm(request.POST)
    if form.is_valid():
     form.save()
     return redirect('login')
 else:  
     form=UserCreationForm()
 return render(request,'app/register.html',{'form':form})
