from django.db import models
from  helpers.models import TrackingModel
from authentication.models import User







# Create model Todo 
class Todo(TrackingModel):
    title = models.CharField(max_length = 255)
    description = models.TextField()
    is_completed = models.BooleanField(default=False)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title