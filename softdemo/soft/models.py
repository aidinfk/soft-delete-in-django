from django.utils import timezone
from django.db import models
from django.db.models import QuerySet, Manager
from django.db.models import Q


# Create your models here.
class SoftQuerySet(QuerySet):
    def delete(self):
        return self.update(is_deleted = True, deleted_at=timezone.now())


class SoftManager(Manager):
    def get_queryset(self):
        return SoftQuerySet(self.model, self._db).filter(Q(is_deleted=False) | Q(is_deleted__isnull=True))


class Soft(models.Model):

    is_deleted = models.BooleanField(null=True, blank=True, editable=False)
    deleted_at = models.DateTimeField(null= True, blank=True, editable=False)

    objects = SoftManager()
    

    class Meta:
        abstract = True

    
    def delete(self, using=None, keep_parent = False):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()
