from django.db import models
import uuid
from accounts.models import User
# Create your models here.

class BaseModel(models.Model):
     
     uid = models.UUIDField(primary_key = True,default=uuid.uuid4)
     created_at = models.DateField(auto_now_add=True)
     updated_at = models.DateField(auto_now_add=True)

     class Meta:
          abstract = True

class TodoModel(BaseModel):
     user = models.ForeignKey(User,on_delete=models.CASCADE)
     title = models.CharField(max_length=150)
     description = models.TextField()
     is_completed = models.BooleanField(default=False)

     def __str__(self):
         return self.title

