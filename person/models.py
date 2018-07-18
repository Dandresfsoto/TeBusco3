from django.db import models


class ActiveManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(active=True)


class Person(models.Model):
    GENDER_CHOISES = (
        ('M', 'Hombre'),
        ('F', 'Mujer'),
        ('O', 'Otro'),
    )
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255)
    gender = models.CharField(max_length=1, choices=GENDER_CHOISES)
    birthdate = models.DateField('Nacimiento', null=True, blank=True)
    disappereance = models.DateField('Desaparición', null=True, blank=True)
    description = models.TextField()
    active = models.BooleanField(default=True)
    active_manager = ActiveManager()
    objects = models.Manager()
    photo = models.ImageField()

    def __str__(self):
        return self.name
