from django.db import models
from django.contrib.auth.models import User
class Game(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    img = models.ImageField(upload_to='images/')
    created_time = models.TimeField(auto_now_add=True)
    update_time = models.TimeField(auto_now=True)
    auther = models.ForeignKey(User , on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Auther is : {self.auther} , Name of Game is : {self.name}"

class Comment(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.CharField(max_length=500)
    game = models.ForeignKey(Game , on_delete=models.CASCADE)
    time = models.TimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.body}"
