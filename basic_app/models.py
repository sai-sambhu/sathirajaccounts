from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib import admin
import locale
locale.setlocale(locale.LC_MONETARY, 'en_IN')
# Create your models here.

from datetime import date

creditss = 0
debitss = 0

def credit(value):
    global creditss
    creditss = value
    pass

def creditDebitValidator(value):
          global creditss
          global debitss
          debitss = value
          if creditss ==0 and debitss == 0:
              raise ValidationError("Credit Debit both are 0")
              
          elif creditss !=0 and debitss != 0:
              raise ValidationError("Credit Debit both are given")    
def cashTick(value):
    if value == True:
        cash = Cash.objects.first()
        if creditss>0:
            cash.cash = cash.cash + creditss
        elif debitss > 0:
            cash.cash = cash.cash - debitss
        cash.save()    
        
class Users(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    #additional
    
    
    def __str__(self):
        return self.user.username
    
class Cash(models.Model):
        cash = models.IntegerField(blank=True, default=0)
        def __str__(self):
            return str(self.cash)
    
class AccountHeads(models.Model):
      
      name = models.CharField(unique=True, blank=False,max_length=100)
      phone = models.IntegerField(blank=False)
      address =  models.CharField(blank=True,max_length=100)
      status = models.CharField(blank=True,max_length=100,default="Active")
      
      
      def __str__(self):
        return self.name    
    
       
    
class Records(models.Model):
      
      
      date = models.DateField(blank=False, default = date.today())
      accountHeads = models.ForeignKey(AccountHeads, on_delete=models.CASCADE)
      credit = models.IntegerField(blank=False, validators=[credit], default = 0)
      debit = models.IntegerField(blank=False, validators=[creditDebitValidator],default = 0)
      cash = models.BooleanField(default=False, validators=[cashTick])
      remarks = models.CharField(blank=True,max_length=15)
      
      class Meta:
        ordering = ("-date",)
        
      
      
      def __str__(self):
        return str(self.date)+ " | " + self.accountHeads.name + " | " + locale.currency(self.credit, grouping=True)[2:-3]+ " | " +  locale.currency(self.debit, grouping=True)[2:-3]    


