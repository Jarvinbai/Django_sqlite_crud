from django.shortcuts import render,redirect
from django.core.paginator import Paginator
from django.http import HttpResponse
from .models import people

# Create your views here.

def home(request):
    mydata=people.objects.all()
    if(mydata!=''):
        return render(request,'home.html',{'datas':mydata})
    else:
        return render(request,'home.html')

def addData(request):
    if request.method=='POST':
        name=request.POST['sname']
        mail=request.POST['email']
        passw=request.POST['pass']

        obj=people()
        obj.Name=name
        obj.Mail=mail
        obj.password=passw
        obj.save()
        mydata=people.objects.all()
        return redirect('home')
    return render(request,'home.html')

def showtable(request):
    mydata=people.objects.all()
    paginator = Paginator(mydata,5)  # Show 5 records per page.

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "showtable.html", {"page_obj": page_obj})

def updateData(request,id):
    mydatas=people.objects.get(id=id)
    if request.method=='POST':
        name=request.POST['sname']
        mail=request.POST['email']
        passw=request.POST['pass']

        mydatas.Name=name
        mydatas.Mail=mail
        mydatas.password=passw
        mydatas.save()
        return redirect('showtable')
    return render(request,'update.html',{'data':mydatas})

def deleteData(request,id):
    mydatas=people.objects.get(id=id)
    mydatas.delete()
    return redirect('showtable')

