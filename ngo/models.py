from django.db import models

# Create your models here.
class ngodatamodel(models.Model):
    ngoname = models.CharField(max_length=30, unique=True)
    email = models.EmailField(max_length=30, unique=True)
    password = models.CharField(max_length=20, unique=True)
    unique_id = models.UUIDField()
    admin_name = models.CharField(max_length=20)
    address = models.CharField(max_length=200)

    class Meta:
        db_table = 'ngodatatable'

    



