from django.db import models

# Create your models here.
#makesmigration  create changes and store in file
#mirate apply panding changes

class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.EmailField()
    desc = models.TextField()
    date = models.DateField()


    def __str__(self):
        return self.name