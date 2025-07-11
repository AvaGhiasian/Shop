from django.db.models.signals import pre_save
from django.dispatch import receiver

from store.models import Product

@receiver(pre_save, sender=Product)
def calculate_new_price(sender, instance, *args, **kwargs):
    instance.new_price = instance.price - instance.off
