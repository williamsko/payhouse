from django.db import models
from django.contrib.auth.models import User
from base.models import CurrencyArea, Country
import rstr

# Create your models here.


class Entity(models.Model):

    def reference():
        return rstr.digits(8)

    reference = models.CharField(max_length=255,unique=True,default=reference)
    brand_name = models.CharField(max_length=255, unique=True)
    contact_email = models.CharField(max_length=255)
    contact_phone_number = models.CharField(max_length=255)
    country = models.ForeignKey(Country, max_length=128, null=True, blank=True,on_delete = models.DO_NOTHING)
    currency = models.ForeignKey(CurrencyArea, max_length=128, null=True, blank=True,on_delete = models.DO_NOTHING)
    created_at = models.DateTimeField(('Creation date'),auto_now_add=True,null=True, blank=True,)
    modified_at = models.DateTimeField('Modification date', auto_now=True)
    status = models.BooleanField(('Status'),help_text="Entity's status in the system", default=True)
    is_provider = models.BooleanField(('Provider'),help_text="Check if this entity is the provider of this plateform", default=False)

    class Meta:
        verbose_name = "Entity"
        verbose_name_plural= "Entities"

    def __str__(self):
        return "%s"%self.brand_name

    @property
    def obj_balance(self):
        obj_balance = None
        obj = EntityBalance.objects.filter(entity=self)
        if obj.count() > 0:
            obj_balance = obj.last()
        return obj_balance


    def has_enough_balance(self,amount):
        return self.obj_balance.balance - amount >= 0

    def credit(self,amount,comments):
        new_balance = self.obj_balance.balance + amount

        obj = EntityBalance()
        obj.parent = self.obj_balance
        obj.entity = self
        obj.comments = comments
        obj.status = True
        obj.balance = new_balance
        obj.save()




class Pos(models.Model):

    def reference():
        return rstr.digits(8)

    reference = models.CharField(max_length=255,unique=True,default=reference)
    entity = models.ForeignKey("Entity", max_length=128, null=True, blank=True,on_delete = models.DO_NOTHING)
    user = models.ForeignKey(User, max_length=128, null=True, blank=True,on_delete = models.DO_NOTHING)
    brand_name = models.CharField(max_length=255)
    adress = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    country = models.ForeignKey(Country, max_length=128, null=True, blank=True,on_delete = models.DO_NOTHING)
    contact_phone_number = models.CharField(max_length=255)
    created_at = models.DateTimeField(('Creation date'),auto_now_add=True,null=True, blank=True,)
    modified_at = models.DateTimeField('Modification date', auto_now=True)
    status = models.BooleanField(('Status'),help_text="POS's status in the system", default=True)

    class Meta:
        verbose_name = "Pos"
        verbose_name_plural= "Pos"

    def __str__(self):
        return "%s"%self.brand_name



class EntityBalance(models.Model):

    def reference():
        return rstr.digits(8)

    reference = models.CharField(max_length=255,unique=True,default=reference)
    entity = models.ForeignKey("Entity", max_length=128, null=True, blank=True,on_delete = models.DO_NOTHING)
    balance = models.DecimalField(decimal_places=3,max_digits=7)
    parent = models.ForeignKey('self', blank=True, null=True, related_name='children',on_delete = models.DO_NOTHING)
    created_at = models.DateTimeField(('Creation date'),auto_now_add=True,null=True, blank=True,)
    modified_at = models.DateTimeField('Modification date', auto_now=True)
    status = models.BooleanField(('Status'),help_text="POS's status in the system", default=True)
    comments = models.TextField(max_length=10000,null=True,blank=True,default="")

    class Meta:
        verbose_name = "Entity balance"
        verbose_name_plural= "Entities' balance"

    def __str__(self):
        return "%s"%self.reference

    @property
    def previous_balance(self):
        return self.parent.balance
