from itertools import count
from os import uname
from django.core.mail import send_mail
import string
from xmlrpc.client import ResponseError
from django.shortcuts import render,redirect
from .models import registerdata,servicedetail,ownermain,adminvalid


# Create your views here.
#views.py file used to write a business logic

tag=""
tag1=""
j=0
#the Home page  
def home(request):
    global tag1,tag,j
    if(j==0):
        tag=0
    else:
        tag=1

    return render(request,"home.html",{"tag":tag,"tag1":tag1})

#the function return the register detail page    
def register(request):
    global error
    global unameunique
    
    if request.method=="POST":
        unameunique=request.POST['first_name']
        mnumber=request.POST['mnumber']
        email=request.POST['email']
        pass1=request.POST['password1']
        if registerdata.objects.filter(uname=unameunique).exists():
            error="User name already exist"
            return render(request,"register.html",{"error":error})
        else:
            registerdata(uname=unameunique,mnumber=mnumber,email=email,Password=pass1).save()
            return redirect('login')

    return render(request,"register.html")

#the function return the service booking    
def service(request):
    global tag1
    lst=[]
    cbox=""
    tol=ownermain.objects.all()
    total=ownermain.objects.count() 
    if(tag1==""):
        return redirect('login')
    if request.method=="POST":
        uname1=request.POST['yourname']
        date=request.POST['date']
        vname=request.POST['vname']
        vnumber=request.POST['vnumber']
        vtype=request.POST['vtype']
        lst=request.POST.getlist('same')
        for i in lst:
            cbox+=i+","
        servicedetail(uname=tag1,date=date,servicedel=cbox,vname=vname,vnumber=vnumber,vtype=vtype,flag=1).save()
        getmail=registerdata.objects.get(uname=tag1).email
        bookdetail=" hellow Sir, our customer "+uname1+" need  a services of "+cbox+" for his "+vname+" bike And he book the services Date that was "+date+" thank you sir."
        send_mail("Servicebooked",bookdetail,'johnbikeservicebooking@gmail.com',["sathyaforjob1@gmail.com","codelabtamil@gmail.com"])
        send_mail("Johnbikeservices","email as soon as his booking is ready for delivery",'johnbikeservicebooking@gmail.com',[getmail])
        print('mail send successfully')
        return redirect('status')
    return render(request,"service.html",{"checkbox":tol})
   
#this was the admin page here i mention owner
def owner(request):
    
    return render(request,"owner.html")

#this was the admin page here i mention owner
def status(request):
    global tag1
    curuser=""
    if(tag1==""):
        return redirect('login')
    detail=servicedetail.objects.filter(uname=tag1)
    return render(request,"status.html",{"detail":detail})

#list of all your previous booking 
def prebook(request):
    global tag1
    if(tag1==""):
        return redirect('login')
    data=servicedetail.objects.filter(uname=tag1)
    return render(request,"prebook.html",{"data":data})

#user login page
def login(request):
    global tag1,j
    
    if request.method=="POST":
        mail2=request.POST['email']
        password1=request.POST['password1']
        if registerdata.objects.filter(email=mail2,Password=password1):
                tags=registerdata.objects.get(email=mail2)
                tag1=tags.uname
                j=j+1
                print(tag1)
                return render(request,"home.html" ,{"tag":1,"tag1":tag1})
        else:        
            return render(request,"login.html",{"error":"email or password Incorrect"})
    return render(request,"login.html")

#this was return the detail about the work for the worker need to complete
def worker(request):
    repet=""
    if request.method=="POST":
        a=request.POST['0']
        
        print(a)
    servicedata=servicedetail.objects.all()
    last=servicedetail.objects.filter(flag=0).count()
    if(servicedata.count()==last):
        repet="Feel free No Work Yet"
    return render(request,"worker.html",{"servicedata":servicedata,"repet":repet})

#Here we return Create,update,delete,read operations
def crud(request):
    global servicedata   
    servicedata=ownermain.objects.all()
    return render(request,"crud.html",{"servicedata":servicedata,"del":"Accept","go":"#"})

#Here the Admin can View a list of all bookings (pending, ready for delivery and completed).
def editbooking(request):
    tol=servicedetail.objects.all()    

    return render(request,"editbooking.html",{"servicedata":tol})   
#edit the servics details
def editdata(request,id):
    global edt,val
    servicedata=ownermain.objects.filter(id=id)
    edt="SAVE"
    val="editdata"   
    allservicedata=ownermain.objects.all()
    uname2=vname2=""
    edetail=ownermain.objects.filter(id=id)
    if request.method=="POST":
        uname2=request.POST['title']
        vname2=request.POST['content']       
        edetail.update(main=uname2,adout=vname2)
        return render(request,"crud.html",{"servicedata":allservicedata})
    return render(request,"editdata.html",{"servicedata":servicedata,"del":"Delete","go":"deletedata"})

#this function used to update the service data
def updatedetai(request,id):
    return render(request,"crud.html")

#this function used to delete the service data
def deletedata(request,id):
    ownermain.objects.filter(id=id).delete()
    servicedata=ownermain.objects.all()
    return render(request,"crud.html",{"servicedata":servicedata,"del":"Accept","go":"#"})

#Here the function the admin login page
def adminlog(request):
    global admin_name
    if request.method=="POST":
        admin_name=request.POST['username']
        password1=request.POST['pw']
        if adminvalid.objects.filter(username=admin_name,password=password1):
            return render(request,"owner.html")
        else:        
            return render(request,"adminlog.html",{"error":"email or password Incorrect"})
    return render(request,"adminlog.html")


def createservice(request):
    if request.method=="POST":
        tit=request.POST['title']
        dess=request.POST['des']
        ownermain(main=tit,adout=dess).save()
        return redirect('crud')
    return render(request,"createservice.html")


def changeflag(request,id):
    repet=""
    final=servicedetail.objects.filter(id=id)
    final.update(flag=0)
    servicedata=servicedetail.objects.all()
    last=servicedetail.objects.filter(flag=0).count()
    print(last)
    if(servicedata.count()==last):
        repet="Feel free No Work Yet"
    return render(request,"worker.html",{"servicedata":servicedata,"repet":repet})


def alluserservice(request,id):
    final=servicedetail.objects.filter(id=id)
    final.update(flag=2)
    final1=servicedetail.objects.get(id=id)
    user=final1.uname
    emailforuser=registerdata.objects.get(uname=user)
    mail=emailforuser.email
    send_mail("Johnbikeservices","your service has been completed. come and take your bike",'johnbikeservicebooking@gmail.com',[mail])
    servicedata=servicedetail.objects.all()
    return render(request,"editbooking.html",{"servicedata":servicedata})


def alldetail(request):
    data=servicedetail.objects.all()
    return render(request,"alldetail.html",{"data":data})

    
def allservices(request):
    data=ownermain.objects.all()
    return render(request,"allservices.html",{"data":data})