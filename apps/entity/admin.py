# vim: set fileencoding=utf-8 :
from django.contrib import admin
from . import models


class EntityAdmin(admin.ModelAdmin):



    list_display = (
        'id',
        'reference',
        'brand_name',
        'contact_email',
        'contact_phone_number',
        'country',
        'currency',
        'created_at',
        'modified_at',
        'status',
        'is_provider',


    )
    list_filter = (
        'country',
        'currency',
        'created_at',
        'modified_at',
        'status',
        'is_provider',
        'id',
        'reference',
        'brand_name',
        'contact_email',
        'contact_phone_number',
        'country',
        'currency',
        'created_at',
        'modified_at',
        'status',
        'is_provider',
    )
    date_hierarchy = 'created_at'


class PosAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'reference',
        'entity',
        'user',
        'brand_name',
        'adress',
        'city',
        'country',
        'contact_phone_number',
        'created_at',
        'modified_at',
        'status',
    )
    list_filter = (
        'entity',
        'user',
        'country',
        'created_at',
        'modified_at',
        'status',
        'id',
        'reference',
        'entity',
        'user',
        'brand_name',
        'adress',
        'city',
        'country',
        'contact_phone_number',
        'created_at',
        'modified_at',
        'status',
    )
    date_hierarchy = 'created_at'


class EntityBalanceAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'reference',
        'entity',
        'balance',
        'parent',
        'created_at',
        'modified_at',
        'status',
    )
    list_filter = (
        'entity',
        'parent',
        'created_at',
        'modified_at',
        'status',
        'id',
        'reference',
        'entity',
        'balance',
        'parent',
        'created_at',
        'modified_at',
        'status',
    )
    date_hierarchy = 'created_at'


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Entity, EntityAdmin)
_register(models.Pos, PosAdmin)
_register(models.EntityBalance, EntityBalanceAdmin)
