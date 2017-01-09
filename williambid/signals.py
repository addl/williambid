from django.db.models.signals import pre_save, pre_delete, post_save, post_delete
from django.dispatch import receiver
from williambid.models import Subasta


@receiver(post_save, sender=Subasta)
def model_post_save(sender, **kwargs):
    print('Saved: {}'.format(kwargs['instance'].__dict__))


@receiver(post_delete, sender=Subasta)
@receiver(post_delete, sender=Subasta)
def model_post_delete(sender, **kwargs):
    print('Deleted: {}'.format(kwargs['instance'].__dict__))

