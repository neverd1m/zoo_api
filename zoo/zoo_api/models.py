from django.db import models
from django.utils import timezone

# Create your models here.


class Animal(models.Model):

    name = models.CharField(db_index=True, max_length=50)
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

    def __init__(self, *args, **kwargs):
        super(Animal, self).__init__(*args, **kwargs)
        self.__original_staff = self.staff

    def save(self, *args, **kwargs):
        if self.staff != self.__original_staff:
            self.linked_staff_date = timezone.now()

        super(Animal, self).save(*args, **kwargs)
        self.__original_staff = self.staff

    # def post_save(self, **args, **kwargs):
    #     if self.animal_type:
    #         super().save()


class AnimalType(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)
    quantity = models.IntegerField(default=0)
    description = models.TextField()

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):

        super(Animal, self).save(*args, **kwargs)
        self.quantity = self.animals.count()


class Shelter(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return self.name


class Staff(models.Model):
    name = models.CharField(db_index=True, max_length=50)
    phone = models.IntegerField()
    probation = models.BooleanField(default=True)
    shelter = models.ForeignKey(
        "Shelter", on_delete=models.PROTECT, related_name='staff', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return self.name
