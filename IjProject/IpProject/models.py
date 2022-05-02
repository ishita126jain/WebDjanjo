from django.db import models

# Create your models here.

class Form(models.Model):
    Name = models.CharField(max_length=20)
    Enroll_no = models.CharField(max_length=7)
    Branch = models.CharField(max_length=3)

    def _str_(self):
        return self.Name 