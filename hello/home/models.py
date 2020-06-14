from django.db import models

# makemigrations mean save changes
# migrate mean apply the changes


# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    desc = models.TextField()
    date=models.DateField()
    def __str__(self):
        return self.name
    