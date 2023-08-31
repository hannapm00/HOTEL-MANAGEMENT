from django.shortcuts import render,redirect
from . import models
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import User
from hoteltacos.models import chef,staff,reservation,outsideuser
from . import models
# Create your views here.

def index(request):
    return render(request,'home.html')


def mainfood(request):
    return render(request,'mainfood.html') 

def chefdashboard(request):
    return render(request,'chefdashboard.html')       

def pagerenderchefregister(request):
    return render(request,'chefregister.html')

def pagerenderstaffregister(request):
    return render(request,'staffregister.html')    

def loginpagerender(request):
    return render(request,'login.html')

def chefregister(request):
    
    if request.method=='POST':

        name=request.POST.get('name')
        email=request.POST.get('email')
        number=request.POST.get('number')
        place=request.POST.get('place')
        experiance=request.POST.get('experiance')
        password=request.POST.get('password')
        cpassword=request.POST.get('cpassword')
        role='chef'
        status="0"
    
        if password==cpassword:

            if User.objects.filter(username=name).exists():

                messages.info(request,"username Taken")
                return redirect('chefregister')


            elif User.objects.filter(email=email).exists():

                messages.info(request,"email already exists")    
                return redirect('chefregister')
            else:

                user=User.objects.create_user(username=name,password=password)
                user.save()
                print(user) 

                userDetails=models.chef(user=user,name=name,email=email,number=number,place=place,experiance=experiance,password=password,cpassword=cpassword,role=role,status=status)
                userDetails.save()
                print(userDetails)

                print('user created')
        else:

            messages.info(request," password is not matching")
            return redirect('chefregister')
        return redirect('loginpagerender')
    else:

        return render(request,'chefregister.html')
                                

def adminviewallchef(request):
    data=chef.objects.all()
    return render(request,'adminviewchef.html',{'dt' :data})

    

    # staff


def staffregister(request):
    
    if request.method=='POST':

        name=request.POST.get('name')
        email=request.POST.get('email')
        number=request.POST.get('number')
        place=request.POST.get('place')
        experiance=request.POST.get('experiance')
        password=request.POST.get('password')
        cpassword=request.POST.get('cpassword')
        role='staff'
        status="0"
    
        if password==cpassword:

            if User.objects.filter(username=name).exists():

                messages.info(request,"username Taken")
                return redirect('staffregister')


            elif User.objects.filter(email=email).exists():

                messages.info(request,"email already exists")    
                return redirect('staffregister')
            else:

                user=User.objects.create_user(username=name,password=password)
                user.save()
                print(user) 

                userDetails=models.staff(user=user,name=name,email=email,number=number,place=place,experiance=experiance,password=password,cpassword=cpassword,role=role,status=status)
                userDetails.save()
                print(userDetails)

                print('user created')
        else:

            messages.info(request," password is not matching")
            return redirect('staffregister')
        return redirect('loginpagerender')
    else:

        return render(request,'staffregister.html')  


         


 
#  to login

role=''
stat=''
def loginactivate(request):
    global role
    global stat
    if request.method=='POST':
        username=request.POST.get('lname') 
        password=request.POST.get('lpass')  


        data=User.objects.filter(username=username).values()
        print("userModelData==>",data)
        for i in data:
           
            u_name=i['username']
            id=i['id']

            d=chef.objects.filter(user_id=id).values()
            print("chefdata==>",d)
            for i in d:
                stat=i['status']
                role=i['role']


            da=staff.objects.filter(user_id=id).values()
            print("staffdata==>",da)
            for i in da:
                stat=i['status']
                role=i['role']


            dat=outsideuser.objects.filter(user_id=id).values()
            print("outsidedata==>",dat)
            for i in dat:
                stat=i['status']
                role=i['role']    


           
            user = authenticate(username=username,password=password)     

            if user is not None and role=="chef" and username==u_name and stat=="1":
                auth_login(request,user)
                return render(request,'chefdashboard.html')

            elif user is not None and role=="staff" and username==u_name and stat=="1":
                auth_login(request,user)
                return render(request,'staffdashboard.html')


            elif user is not None and role=="outsideuser" and username==u_name and stat=="1":
                auth_login(request,user)
                return render(request,'outsideuserdashboard.html')    

            elif user is not None and username=="admn" and password=="hamd123":
                return render(request,'admindashboard.html')

            else:
                pass


        else:
            messages.info(request,'invalid credentials')

        return redirect('loginactivate')

    else:
        return render(request,'login.html')


# to approve
def foradmintoapprovechef(request,reg_id):
    reg=chef.objects.get(id=reg_id) 
    reg.status=1
    reg.save()         
    return redirect('adminapprovedchef')

def adminapprovedchef(request):
    data=chef.objects.all()
    return render(request,'viewapprovedchef.html',{'dt' :data}) 

# to reject
def rejectchef(request,id):
    add=chef.objects.get(id=id)
    add.delete()
    return redirect('adminviewallchef')  



    # staff approve and reject

# to approve
def foradmintoapprovestaff(request,reg_id):
    reg=staff.objects.get(id=reg_id) 
    reg.status=1
    reg.save()         
    return redirect('adminapprovedstaff')

def adminapprovedstaff(request):
    data=staff.objects.all()
    return render(request,'viewapprovedstaff.html',{'dt' :data}) 

# to reject
def rejectstaff(request,id):
    add=staff.objects.get(id=id)
    add.delete()
    return redirect('adminviewallchef')      


def adminviewallstaff(request):
    data=staff.objects.all()
    return render(request,'adminviewstaff.html',{'dt' :data})





    # to edit profile

def chef_profile(request):
    if request.user:
        user=request.user
        print(user)
        data=chef.objects.all().filter(user=user).values()


        for i in data:
            print("//////////",i)
            return render(request,'viewchef2.html',{'i':i})
        return render(request,'mainfood.html')

    #  to edit chef profile

def updatechefprofile(request,id):
     if request.method=="POST":
        add=chef.objects.get(id=id)
        add.name=request.POST['name'] 
        add.email=request.POST['email']  
        add.number=request.POST['number']  
        add.place=request.POST['place']  
        add.experiance=request.POST['experiance']
        add.password=request.POST['password']  
        add.save()
        return redirect('chef_profile')

def editchefprofile(request,id):
    Data=chef.objects.get(id=id)
    return render(request,'editchefprofile.html',{'Data':Data})          


#    to view staff profile

def staff_profile(request):
    if request.user:
        user=request.user
        print(user)
        data=staff.objects.all().filter(user=user).values()


        for i in data:
            print("//////////",i)
            return render(request,'viewstaff.html',{'i':i})
        return render(request,'mainfood.html')

def updatestaffprofile(request,id):
     if request.method=="POST":
        add=staff.objects.get(id=id)
        add.name=request.POST['name'] 
        add.email=request.POST['email']  
        add.number=request.POST['number']  
        add.place=request.POST['place']  
        add.experiance=request.POST['experiance']
        add.password=request.POST['password']  
        add.save()
        return redirect('staff_profile')

def editstaffprofile(request,id):
    Data=staff.objects.get(id=id)
    return render(request,'editstaffprofile.html',{'Data':Data}) 


           

def career(request):
    return render(request,'career.html') 


def contactus(request):
    return render(request,'contactus.html') 


def thankyoupage(request):
    return render(request,'thankyoupage.html')      

# reservation



   

# outside user login


def outsideuserregister(request):
    
    if request.method=='POST':

        name=request.POST.get('name')
        email=request.POST.get('email')
        num=request.POST.get('num')
        address=request.POST.get('address')
        password=request.POST.get('password')
        cpassword=request.POST.get('cpassword')
        role='outsideuser'
        status="0"
    
        if password==cpassword:

            if User.objects.filter(username=name).exists():

                messages.info(request,"username Taken")
                return redirect('outsideuserregister')


            elif User.objects.filter(email=email).exists():

                messages.info(request,"email already exists")    
                return redirect('outsideuserregister')
            else:

                user=User.objects.create_user(username=name,password=password)
                user.save()
                print(user) 

                userDetails=models.outsideuser(user=user,name=name,email=email,num=num,address=address,password=password,cpassword=cpassword,role=role,status=status)
                userDetails.save()
                print(userDetails)

                print('user created')
        else:

            messages.info(request," password is not matching")
            return redirect('staffregister')
        return redirect('loginpagerender')
    else:

        return render(request,'outsideuserregister.html')  



def pagerenderoutsiderregister(request):
    return render(request,'outsideuserregister.html')        


    # to approve

def adminviewalloutsideuser(request):
    data=outsideuser.objects.all()
    return render(request,'adminviewoutsideuser.html',{'dt' :data})    

def toapproveoutsideuser(request,reg_id):
    reg=outsideuser.objects.get(id=reg_id) 
    reg.status=1
    reg.save()         
    return redirect('adminapprovedoutsideuser')

def adminapprovedoutsideuser(request):
    data=outsideuser.objects.all()
    return render(request,'viewapprovedoutsideuser.html',{'dt' :data}) 

# to reject
def rejectoutsideuser(request,id):
    add=outsideuser.objects.get(id=id)
    add.delete()
    return redirect('adminviewallchef')      



  # reservation



def bookreservation(request):
    if request.user:
        user=request.user
        if request.method=="POST":
            name=request.POST['name']
            email=request.POST['email'] 
            fordate=request.POST['fordate'] 
            fromtime=request.POST['fromtime']
            totime=request.POST['totime']
            num=request.POST['num']
            tablemembers=request.POST['tablemembers']
            address=request.POST['address']
            status="0"
            add=models.reservation(user=user,name=name,email=email,fordate=fordate,fromtime=fromtime,totime=totime,num=num,tablemembers=tablemembers,address=address,status=status)
            add.save()
            return redirect('bookreservation')
        else:
            return redirect('thankyoupage')      


def reservation(request):
    return render(request,'reservation.html')  


def viewallreser(request):
    data=reservation.objects.all()
    return render(request,'viewallreservation.html',{'dt' :data})

def reserapprove(request,reg_id):
    reg=reservation.objects.get(id=reg_id) 
    reg.status=1
    reg.save()         
    return redirect('approvedreservation')

def approvedreser(request):
    data=reservation.objects.all()
    return render(request,'approvedreservation.html',{'dt' :data})
