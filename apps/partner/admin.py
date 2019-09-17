# vim: set fileencoding=utf-8 :
from django.contrib import admin

from . import models
from django.urls import reverse
from django.utils.html import format_html
from django.conf.urls import url
from django.http import HttpResponseRedirect
from django.contrib import messages

import requests
import json


class PartnerAdmin(admin.ModelAdmin):


    list_display = (
        'id',
        'reference',
        'brand_name',
        'contact_email',
        'contact_phone_number',
        'currency',
        'created_at',
        'modified_at',
        'status',
    )
    list_filter = (
        'currency',
        'created_at',
        'modified_at',
        'status',
        'id',
        'reference',
        'brand_name',
        'contact_email',
        'contact_phone_number',
        'currency',
        'created_at',
        'modified_at',
        'status',
    )
    date_hierarchy = 'created_at'


class PartnerBalanceAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'reference',
        'partner',
        'balance',
        'parent',
        'created_at',
        'modified_at',
        'status',
    )
    list_filter = (
        'partner',
        'parent',
        'created_at',
        'modified_at',
        'status',
        'id',
        'reference',
        'partner',
        'balance',
        'parent',
        'created_at',
        'modified_at',
        'status',
    )
    date_hierarchy = 'created_at'


class ServiceAdmin(admin.ModelAdmin):

    def account_actions(self, obj):
        return format_html(
                '<a class="button success" href="{}">Check</a>&nbsp;'
                '<a class="button" href="{}">Withdraw</a>',
                reverse('admin:account-deposit', args=[obj.reference]),
                reverse('admin:account-withdraw', args=[obj.pk]),
        )
    account_actions.short_description = 'Actions'
    account_actions.allow_tags = True


    def process_deposit(self, request, service_ref, *args, **kwargs):

        entity_ref = "68625189"
        amount = 1000
        url = "http://127.0.0.1/api/v0/transaction/create/?format=json"
        data = {"service_reference":service_ref,"entity_ref":entity_ref,"amount":amount}
        req = requests.post(url, data = json.dumps(data))


        self.message_user(request, req.text() , level=messages.ERROR)
        return HttpResponseRedirect("/admin/partner/service/")

    def process_withdraw(self, request, service_ref, *args, **kwargs):
        self.message_user(request, "All heroes are now mortal bis")
        return HttpResponseRedirect("/admin")

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            url(
                r'^(?P<service_ref>.+)/deposit/$',
                self.admin_site.admin_view(self.process_deposit),
                name='account-deposit',
            ),
            url(
                r'^(?P<service_ref>.+)/withdraw/$',
                self.admin_site.admin_view(self.process_withdraw),
                name='account-withdraw',
            ),
        ]
        return custom_urls + urls



    list_display = (
        'id',
        'reference',
        'partner',
        'brand_name',
        'created_at',
        'modified_at',
        'max_retries',
        'ping_status',

        'status',
        'account_actions',
    )
    list_filter = (
        'partner',
        'created_at',
        'modified_at',
        'status',
        'id',
        'reference',
        'partner',
        'brand_name',
        'created_at',
        'modified_at',
        'max_retries',
        'status',
    )
    date_hierarchy = 'created_at'


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Partner, PartnerAdmin)
_register(models.PartnerBalance, PartnerBalanceAdmin)
_register(models.Service, ServiceAdmin)
