from django.db import models
import rstr

# Create your models here.


class CurrencyArea(models.Model):

    def reference():
        return rstr.digits(7)

    name = models.CharField(max_length=255,unique=True)
    iso_code = models.CharField(max_length=255,unique=True)
    created_at = models.DateTimeField(('Creation date'),auto_now_add=True,null=True, blank=True,)
    modified_at = models.DateTimeField('Modification date', auto_now=True)
    status = models.BooleanField(('Status'),help_text="Currency area's status in the system", default=True)

    class Meta:
        verbose_name = "Currency area"
        verbose_name_plural= "Currency areas"

    def __str__(self):
        return "%s"%self.name


class Country(models.Model):

    def reference():
        return rstr.digits(7)

    name = models.CharField(max_length=255,unique=True)
    iso2_code = models.CharField(max_length=255,unique=True)
    iso3_code = models.CharField(max_length=255,unique=True)
    created_at = models.DateTimeField(  ('Creation date'),auto_now_add=True,null=True, blank=True,)
    modified_at = models.DateTimeField('Modification date', auto_now=True)
    status = models.BooleanField(('Status'),help_text="Country's status in the system", default=True)

    class Meta:
        verbose_name = "Country"
        verbose_name_plural= "Countries"

    def __str__(self):
        return "%s"%self.name
