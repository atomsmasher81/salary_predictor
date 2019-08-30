from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class DataSet:
    id = models.AutoField(primary_key=True)
    Experience = models.FloatField(blank=True,null=True)
    salary = models.FloatField(blank=True,null=True)

class trainingData:
    id = models.AutoField(primary_key=True),
    user_linked = models.ForeignKey(User,on_delete=models.PROTECT)
    data_set_linked = models.ForeignKey(DataSet,on_delete=models.PROTECT)
    model_trained_flag= models.BooleanField(default=False)
    trained_model= models.FileField(upload_to="{}/".format(user_linked.name))




