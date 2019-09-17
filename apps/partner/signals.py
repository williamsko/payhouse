from .models import Partner, PartnerBalance
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=Partner)
def create_partner_account(sender, instance, created, **kwargs):
    if created:
        p_balance = PartnerBalance()
        p_balance.partner = instance
        p_balance.balance = 0
        p_balance.save()
