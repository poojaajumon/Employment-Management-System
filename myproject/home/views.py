from django.shortcuts import render,redirect
from . models import Employees
# Create your views here.
# def home(request):
#     return render(request,'home.html')
def index(request):
    data={
   "emp":Employees.objects.all()
    }
    print(data)
    return render(request,'index.html',data)
def add(request):
    return render(request,'about.html')
def insert(request):
    if request.method=="POST":
        name=request.POST.get('name')
        print(name)
        ids=request.POST.get('ids')
        department=request.POST.get('department')
        mobile=request.POST.get('mobile')
        email=request.POST.get('email')
        place=request.POST.get('place')
        query=Employees(name=name,ids=ids,department=department,mobile=mobile,email=email,place=place,)
        query.save()
    return redirect("/index")    

def delete(request,id):
    dlt=Employees.objects.get(id=id)
    dlt.delete()
    return redirect("/index") 
def edit(request,id):
    data={"data":Employees.objects.get(id=id)}
    if request.method=="POST":
        name=request.POST.get('name')
        ids=request.POST.get('ids')
        department=request.POST.get('department')
        mobile=request.POST.get('mobile')
        email=request.POST.get('email')
        place=request.POST.get('place')
        edit=Employees.objects.get(id=id)
        edit.name=name
        edit.ids=ids
        edit.department=department
        edit.mobile=mobile
        edit.email=email
        edit.place=place
        edit.save()
        return redirect("/index")
    return render(request,'edit.html',data)

    
def home(request):
    return render(request,"home.html")