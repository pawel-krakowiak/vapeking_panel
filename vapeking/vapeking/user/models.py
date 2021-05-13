from django.db import models
from django import forms

class User(models.Model):

    class Powers(models.IntegerChoices):
        UNACTIVE = 0
        EMPLOYEE = 1
        MANAGER  = 2
        ADMIN    = 3
        # __empty__ = _('(Unknown)')

    u_name = models.CharField(max_length=30, null=False, blank=False)
    u_surename = models.CharField(max_length=30, null=False, blank=False)
    u_password = models.CharField(max_length=100, null=False, blank=False)
    u_power_flag = models.IntegerField(blank=False, choices=Powers.choices)
    # TODO: u_store = models.ForeignKey("app.Model", verbose_name=_(""), on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    
