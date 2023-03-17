from django.db import models

class DataModel(models.Model):
    column1 = models.CharField(max_length=50)
    column2 = models.CharField(max_length=50)
    column3 = models.CharField(max_length=50)
    

    class Meta:
        ordering = ['column1']