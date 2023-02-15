from django.shortcuts import render
from basic_app.forms import ChatBotAdminForm as UserForm 
# Create your views here.


from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import AccountHeads, Records, Cash
from datetime import datetime,date,timedelta 
from dateutil import relativedelta

def report(request):
    cash = Cash.objects.first()
    accountHeads = AccountHeads.objects.all()
    reportDict = []
    for i in accountHeads:
    
            records = Records.objects.filter(accountHeads__name__contains=i.name)
            if getInterest(records, "2020-02-02", 18)[0] >0:
                reportDict.append([i.name,0,getInterest(records, "2020-02-02", 18)[0]])
            elif getInterest(records, "2020-02-02", 18)[0] <0:
                reportDict.append([i.name,abs(getInterest(records, "2020-02-02", 18)[0]),0])
            else:
                reportDict.append([i.name,0,0])
                
            
    
    reportDict.append( ["Total",sum([i[1] for i in reportDict ]),sum([i[2] for i in reportDict ])])
    return render(request,'basic_app/reportDict.html',{"reportDict":reportDict,"cashInHand":cash.cash})


def compAndSimpleCalculator(amount,fromDate,toDate, interest):
    
    end =   datetime.strptime(toDate, "%Y-%m-%d")
    start = datetime.strptime(fromDate, "%Y-%m-%d")
    
    res=[]
    
    
    delta = relativedelta.relativedelta(end, start)
    res_months = delta.months + (delta.years * 12)
    
    print(delta.months,delta.days,delta.years)
    simpleInterest = ((amount * int(interest) * res_months) / (100 * 12) ) +((amount * delta.days * int(interest) / 100 * 1/365))
    
    print(simpleInterest)
    res.append([amount,int(simpleInterest)])
    
    compIntrest = amount*(1+interest/100)**(delta.years)
    amount = compIntrest
    simpleInterest = ((amount * int(interest) * delta.months) / (100 * 12) ) +((amount * delta.days * int(interest) / 100 * 1/365))
    
    
    res.append([int(amount),int(simpleInterest)])
    
    return res
    pass


def intcal(request):
    total = None
    cash = Cash.objects.first()
    
    if request.POST.get("SimInterestSub"):
       res = compAndSimpleCalculator(int(request.POST["amount"]), request.POST["from"], request.POST["to"], int(request.POST["interest"])) 
       
       total = res[0]
       
       return render(request,'basic_app/interestCalculator.html',{"fromDate":request.POST["from"],
                                                                   "toDate":request.POST["to"],
                                                                   "amt":request.POST["amount"],
                                                                   "inte":request.POST["interest"],
                                                                   "total":total,"cashInHand":cash.cash})
    elif request.POST.get("ComInterestSub"):
        res = compAndSimpleCalculator(int(request.POST["amount"]), request.POST["from"], request.POST["to"], int(request.POST["interest"])) 
       
        total = res[1]
        return render(request,'basic_app/interestCalculator.html',{"fromDate":request.POST["from"],
                                                                   "toDate":request.POST["to"],
                                                                   "amt":request.POST["amount"],
                                                                   "inte":request.POST["interest"],
                                                                   "total":total,"cashInHand":cash.cash})
        
       
        
    
    
        
    return render(request,'basic_app/interestCalculator.html', {"amt":0,
                                                                   "inte":18
                                                                   ,"cashInHand":cash.cash})




def index(request):
    accountHeads = AccountHeads.objects.all()
    
    cash = Cash.objects.first()
    
    records = Records.objects.filter( date__range=(date.today() + timedelta(-30), date.today())
                                         ).order_by('date')
        
    return render(request,'basic_app/index.html',{'accountHeads':accountHeads,"records":records,
                                                  "CredSum":sum(records.values_list('credit', flat=True)),
                                                  "DebSum":sum(records.values_list('debit', flat=True)),
                                                  "CredDeb":sum(records.values_list('debit', flat=True))-sum(records.values_list('credit', flat=True))
                                                  ,"cashInHand":cash.cash})

def getRecords(request):
    cash = Cash.objects.first()
    
    if request.POST.get("interestSub"):
        records = Records.objects.filter( date__range=(request.POST["from"], request.POST["to"]),
                                         accountHeads__name__contains=request.POST["AccountHeads"])
        
        
        total = getInterest(records[::-1],request.POST["to"],request.POST["interest"])
        
        
        accountHeads = AccountHeads.objects.all()
        records = Records.objects.filter( date__range=(request.POST["from"], request.POST["to"]),accountHeads__name__contains=request.POST["AccountHeads"] ).order_by('date')
    
        
        return render(request,'basic_app/simpleInterest.html',{'accountHeads':accountHeads,
                                                           "hidden": request.POST["AccountHeads"],
                                                           "records":records,
                                                           "fromDate":request.POST["from"],"toDate":request.POST["to"],"total":"Asalu: "+str(total[0]) + " Vaddi: "+str(total[1]),
                                                           "interestVal":request.POST["interest"],"cashInHand":cash.cash,
                                                           "CredSum":sum(records.values_list('credit', flat=True)),
                                                           "DebSum":sum(records.values_list('debit', flat=True)),
                                                           "CredDeb":sum(records.values_list('debit', flat=True))-sum(records.values_list('credit', flat=True))})
    
        
        
        
        
        
    
    if request.POST["AccountHeads"] == "All":
        accountHeads = AccountHeads.objects.all()
        records = Records.objects.filter( date__range=(request.POST["from"], request.POST["to"])).order_by('date')
        return render(request,'basic_app/index.html',{'accountHeads':accountHeads,
                                                      "records":records,"fromDate":request.POST["from"],
                                                      "toDate":request.POST["to"],
                                                      "CredSum":sum(records.values_list('credit', flat=True)),
                                                      "DebSum":sum(records.values_list('debit', flat=True)),
                                                      "CredDeb":sum(records.values_list('debit', flat=True))-sum(records.values_list('credit', flat=True))
                                                           ,"cashInHand":cash.cash})
        
         
     
  
     
    accountHeads = AccountHeads.objects.all()
    records = Records.objects.filter( date__range=(request.POST["from"], request.POST["to"]),accountHeads__name__contains=request.POST["AccountHeads"] ).order_by('date')
    
    return render(request,'basic_app/simpleInterest.html',{'accountHeads':accountHeads,
                                                           "hidden": request.POST["AccountHeads"],
                                                           "records":records,
                                                           "fromDate":request.POST["from"],"toDate":request.POST["to"],
                                                           
                                                           "interestVal":18,
                                                           "CredSum":sum(records.values_list('credit', flat=True)),
                                                           "DebSum":sum(records.values_list('debit', flat=True)),
                                                           "CredDeb":sum(records.values_list('debit', flat=True))-sum(records.values_list('credit', flat=True))
                                                           ,"cashInHand":cash.cash
                                                           })
    
    pass


def getInterest(records,toDate, interest):
    
    end =   datetime.strptime(toDate, "%Y-%m-%d")
    
    
    asaluDeb = []
    asaluCred=[]
    deb = []
    cred = []
        
    for i in records:
        
        delta = relativedelta.relativedelta(end, i.date)
        res_months = delta.months + (delta.years * 12)
        
        
        if i.debit != 0:
            deb.append( ((i.debit * int(interest) * res_months) / (100 * 12) )  + (( i.debit * delta.days * int(interest) / 100 * 1/365)))
            asaluDeb.append(i.debit)
            
            
            pass
        
        if i.credit != 0:
            cred.append( ((i.credit * int(interest) * res_months) / (100 * 12) ) + (( i.credit * delta.days * int(interest) / 100 * 1/365)))
            asaluCred.append(i.credit)
            pass
        
        print(res_months,delta.days, i.debit,i.credit,deb,cred)
        
    
    return [int(sum(asaluDeb)) - int(sum(asaluCred)),int(sum(deb) - sum(cred))]



def register(request):
    registered=False
    
    if request.method=="POST":
        
        user_form=UserForm(data=request.POST)
        
        if user_form.is_valid() :
            print("NAME: "+ user_form.cleaned_data['username'])
            user=user_form.save()
            user.set_password(user.password)
            user.save()
            
            registered=True
        else:
                print(user_form.errors)
    else:
         user_form=UserForm ()

    return render (request,'basic_app/registration.html',
                   {'user_form':user_form,
                    'registered':registered})          

@login_required   
def special(request):
     return HttpResponse("your are logged in")     
    
@login_required   
def user_logout(request):
     logout(request)
     return HttpResponseRedirect(reverse('index'))    
   
def user_login(request):
    
           
       if request.method=="POST":
           username=request.POST.get('username')
           password=request.POST.get('password')
           
           user=authenticate(username=username,password=password)
          
           
           
           if user:
               
               if user.is_active:
                   login(request,user)
                   return HttpResponseRedirect(reverse('index'))
               else :
                   return HttpResponse("ACCOUNT NOT ACTIVE")
           else:
               print("someone tried to login and failed")
               print(f'username: {username} and password: {password} ')
               return HttpResponse("invalid login details supplied!!")
       else:
            return render(request,'basic_app/login.html')
               