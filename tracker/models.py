from django.db import models

# Create your models here.


class Application(models.Model):
    text = models.TextField(blank=True, null=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    location = models.CharField(max_length=200, blank=True, null=True)
    remote = models.CharField(max_length=200, blank=True, null=True)
    compensation = models.CharField(max_length=200, blank=True, null=True)
    company = models.CharField(max_length=200, blank=True, null=True)
    status = models.CharField(max_length=200, blank=True, null=True,default='Applied')
    is_complete = models.BooleanField(default=False,)
    offer_accept = models.BooleanField(default=False)
    start_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.title


#YYYY-MM-DD