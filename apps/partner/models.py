from django.db import models
from base.models import CurrencyArea
import rstr

# Create your models here.


class Partner(models.Model):

    def reference():
        return rstr.digits(7)

    reference = models.CharField(max_length=255,unique=True,default=reference)
    brand_name = models.CharField(max_length=255, unique=True)
    contact_email = models.CharField(max_length=255)
    contact_phone_number = models.CharField(max_length=255)
    currency = models.ForeignKey(CurrencyArea, max_length=128, null=True, blank=True,on_delete = models.DO_NOTHING)
    created_at = models.DateTimeField(('Creation date'),auto_now_add=True,null=True, blank=True,)
    modified_at = models.DateTimeField('Modification date', auto_now=True)
    status = models.BooleanField(('Status'),help_text="Partner's status in the system", default=True)

    class Meta:
        verbose_name = "Partner"
        verbose_name_plural= "Partners"

    def __str__(self):
        return "%s"%self.brand_name

    @property
    def balance(self):
        obj_balance = 0
        obj = PartnerBalance.objects.filter(partner=self)
        if obj.count() > 0:
            obj_balance = obj.last().balance
        return obj_balance


class PartnerBalance(models.Model):

    def reference():
        return rstr.digits(8)

    reference = models.CharField(max_length=255,unique=True,default=reference)
    partner = models.ForeignKey("Partner", max_length=128, null=True, blank=True,on_delete = models.DO_NOTHING)
    balance = models.DecimalField(decimal_places=3,max_digits=5)
    parent = models.ForeignKey('self', blank=True, null=True, related_name='children',on_delete = models.DO_NOTHING)
    created_at = models.DateTimeField(('Creation date'),auto_now_add=True,null=True, blank=True,)
    modified_at = models.DateTimeField('Modification date', auto_now=True)
    status = models.BooleanField(('Status'),help_text="POS's status in the system", default=True)

    class Meta:
        verbose_name = "Prtner Balance"

    def __str__(self):
        return "%s"%self.reference

    @property
    def previous_balance(self):
        return self.parent.balance


class Service(models.Model):

    def reference():
        return rstr.digits(7)

    reference = models.CharField(max_length=255,unique=True,default=reference)
    partner = models.ForeignKey("Partner", max_length=128, null=True, blank=True,on_delete = models.DO_NOTHING)
    brand_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(('Creation date'),auto_now_add=True,null=True, blank=True,)
    modified_at = models.DateTimeField('Modification date', auto_now=True)
    max_retries = models.PositiveIntegerField(default=True)
    ping_status = models.BooleanField(('Service activity status'),help_text="Service's activity status in the system", default=False)
    demo_base_url = models.CharField(max_length=255,default="http://")
    prod_base_url = models.CharField(max_length=255,default="http://")
    status = models.BooleanField(('Status'),help_text="Service's status in the system", default=True)

    class Meta:
        verbose_name = "Service"
        verbose_name_plural= "Services"

    def __str__(self):
        return "%s"%self.brand_name
