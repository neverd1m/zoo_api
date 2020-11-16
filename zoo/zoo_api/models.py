from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from django.utils import timezone


class Animal(models.Model):

    name = models.CharField(db_index=True, max_length=50, unique=True)
    animal_type = models.ForeignKey(
        'AnimalType', on_delete=models.PROTECT, related_name='animals', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)
    linked_staff_date = models.DateTimeField(null=True)
    __original_staff = None
    shelter = models.ForeignKey(
        'Shelter', related_name='animals', on_delete=models.PROTECT, null=True)
    staff = models.ForeignKey(
        'Staff', related_name='animals', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.name

# При сохранении модели, проставляю дату смены staff'а
    def save(self, *args, **kwargs):
        if self.staff != self.__original_staff:
            self.linked_staff_date = timezone.now()

        super(Animal, self).save(*args, **kwargs)
        self.__original_staff = self.staff


# считаю кол-во животных текущего типа
@receiver(post_save, sender=Animal)
def count_animals(sender, instance, **kwargs):
    if instance.animal_type:
        animal_type = instance.animal_type
        quantity = animal_type.animals.count()
        animal_type.quantity = quantity
        animal_type.save()


class AnimalType(models.Model):
    name = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)
    quantity = models.IntegerField(default=0)
    description = models.TextField()

    def __str__(self):
        return self.name


class Shelter(models.Model):
    name = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return self.name


class Staff(models.Model):
    name = models.CharField(db_index=True, max_length=50, unique=True)
    phone = models.IntegerField()
    probation = models.BooleanField(default=True)
    shelter = models.ForeignKey(
        "Shelter", on_delete=models.PROTECT, related_name='staff', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return self.name
