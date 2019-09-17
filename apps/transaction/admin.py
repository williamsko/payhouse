from django.contrib import admin

# Register your models here.
# vim: set fileencoding=utf-8 :

from . import models


class TransactionAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'reference',
        'input_data',
        'output_data',
        'service',
        'pos',
        'entity',
        'partner',
        'amount',
        'currency',
        'created_at',
        'modified_at',
        'retries_count',
        'status',
        'result',
    )
    list_filter = (
        'service',
        'pos',
        'entity',
        'partner',
        'currency',
        'created_at',
        'modified_at',
        'status',
        'result',
        'id',
        'reference',
        'input_data',
        'output_data',
        'service',
        'pos',
        'entity',
        'partner',
        'amount',
        'currency',
        'created_at',
        'modified_at',
        'retries_count',
        'status',
        'result',
    )
    date_hierarchy = 'created_at'


class TransactionBalanceDetailAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'reference',
        'transaction',
        'partner_account',
        'entity_account',
        'created_at',
        'modified_at',
    )
    list_filter = (
        'transaction',
        'partner_account',
        'entity_account',
        'created_at',
        'modified_at',
        'id',
        'reference',
        'transaction',
        'partner_account',
        'entity_account',
        'created_at',
        'modified_at',
    )
    date_hierarchy = 'created_at'


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Transaction, TransactionAdmin)
_register(models.TransactionBalanceDetail, TransactionBalanceDetailAdmin)
