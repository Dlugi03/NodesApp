from django.db import models

# Create your models here.
class Node(models.Model):
    name = models.CharField(max_length=30)
    
    def delete_node(self):
        self.delete()