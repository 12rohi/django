from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from intern.models import Destination, Transfer
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request, "index.html")

    #registration

def register(request):
    if request.method == 'POST':
        Name = request.POST.get('Name')
        Email = request.POST.get('Email')
        Gender = request.POST.get('Gender')
        Balance = request.POST.get('Balance')

        en = Destination(Name=Name, Email=Email, Gender=Gender, Balance=Balance)
        en.save()

        return render(request, 'index.html')
    else:
        return render(request, 'Register.html')

        #for customers
def customers(request):
    data = Destination.objects.all()
    
    return render(request, "customers.html",{'dest':data})

    #for history
def history(request):
    return render(request, "history.html")

    #for transaction
def details(request):
    customer = Destination.objects.all()
    j='null'
    if request.method=="POST":
        email=request.POST['email']
        amt=request.POST['amount']
        rec=request.POST['rec']
        print(email)
        print(amt)
        print(rec)
        amt=int(amt)
        if email == 'select' or rec == 'select' or (email=='select' and rec=='select') or rec==email:
            messages.warning(request,"EmailId not selected or both EmailId's are same")  
        elif amt <= 0:
            messages.warning(request,'Please provide valid money details!!')
        else:
            for c in customer:
                if c.Email==email:
                    j=email
                    i=c.id
                    name=c.Name
                    if amt > c.Balance:
                        messages.warning(request,"Insufficient Balance!!")   
                    break
            for x in customer:
                if x.Email==rec:
                    rid=x.id
                    rname=x.Name
                    rbal=x.Balance
                    break
            for c in customer: 
                if c.Email==email and rec!=email and rec!='select' and amt<=c.Balance and amt>0:
                    q1= Transfer(sender=name,reciever=rname,amount=amt)
                    q1.save()
                    accbal=c.Balance-amt
                    q2= Destination.objects.filter(id=i).update(Balance=accbal)
                    accbal=rbal+amt
                    q3=Destination.objects.filter(id=rid).update(Balance=accbal)
                    messages.success(request,"Transfer complete!!")

            return render(request, 'index.html')
    else:

            return render(request, "details.html",{'cust':customer})

            #for transer history
def history(request):
    tr = Transfer.objects.all()
    return render(request, 'history.html',{'tr':tr})




