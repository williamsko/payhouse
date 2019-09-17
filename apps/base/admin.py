# vim: set fileencoding=utf-8 :
from django.contrib import admin

from . import models


class CurrencyAreaAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'name',
        'iso_code',
        'created_at',
        'modified_at',
        'status',
    )
    list_filter = (
        'created_at',
        'modified_at',
        'status',
        'id',
        'name',
        'iso_code',
        'created_at',
        'modified_at',
        'status',
    )
    search_fields = ('name',)
    date_hierarchy = 'created_at'


class CountryAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'name',
        'iso2_code',
        'iso3_code',
        'created_at',
        'modified_at',
        'status',
    )
    list_filter = (
        'created_at',
        'modified_at',
        'status',
        'id',
        'name',
        'iso2_code',
        'iso3_code',
        'created_at',
        'modified_at',
        'status',
    )
    search_fields = ('name',)
    date_hierarchy = 'created_at'


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.CurrencyArea, CurrencyAreaAdmin)
_register(models.Country, CountryAdmin)
