from .models import Entity, EntityBalance
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=Entity)
def create_entity_account(sender, instance, created, **kwargs):
    if created:
        e_balance = EntityBalance()
        e_balance.entity = instance
        e_balance.balance = 0
        e_balance.save()
