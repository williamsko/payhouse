from django.db import models
from base.models import CurrencyArea, Country
from partner.models import Partner, PartnerBalance, Service
from entity.models import Entity, Pos, EntityBalance
import rstr

# Create your models here.


class Transaction(models.Model):

    def reference():
        return rstr.digits(8)

    reference = models.CharField(max_length=255,unique=True,default=reference)
    input_data = models.TextField(max_length=1000)
    output_data = models.TextField(max_length=1000)
    service = models.ForeignKey(Service, max_length=128, null=True, blank=True,on_delete = models.DO_NOTHING)
    pos = models.ForeignKey(Pos, max_length=128, null=True, blank=True,on_delete = models.DO_NOTHING)
    entity = models.ForeignKey(Entity, max_length=128, null=True, blank=True,on_delete = models.DO_NOTHING)
    partner = models.ForeignKey(Partner, max_length=128, null=True, blank=True,on_delete = models.DO_NOTHING)
    amount = models.DecimalField(decimal_places=3,max_digits=5)
    currency = models.ForeignKey(CurrencyArea, max_length=128, null=True, blank=True,on_delete = models.DO_NOTHING)
    created_at = models.DateTimeField(('Creation date'),auto_now_add=True,null=True, blank=True,)
    modified_at = models.DateTimeField('Modification date', auto_now=True)
    retries_count = models.PositiveIntegerField(default=0)
    status = models.BooleanField(('Status'),help_text="Transaction transmission status", default=False)
    result = models.BooleanField(('Transaction result'),help_text="Partner result summary", default=False)

    class Meta:
        verbose_name = "Transaction"
        verbose_name_plural= "Transactions"

    def __str__(self):
        return "%s"%self.reference


class TransactionBalanceDetail(models.Model):

    def reference():
        return rstr.digits(8)

    reference = models.CharField(max_length=255,unique=True,default=reference)
    transaction = models.ForeignKey("Transaction", max_length=128, null=True, blank=True,on_delete = models.DO_NOTHING)
    partner_account =  models.ForeignKey(PartnerBalance, max_length=128, null=True, blank=True,on_delete = models.DO_NOTHING)
    entity_account =  models.ForeignKey(EntityBalance, max_length=128, null=True, blank=True,on_delete = models.DO_NOTHING)
    created_at = models.DateTimeField(('Creation date'),auto_now_add=True,null=True, blank=True,)
    modified_at = models.DateTimeField('Modification date', auto_now=True)

    class Meta:
        verbose_name = "Transaction balance detail"

    def __str__(self):
        return "%s"%self.reference
