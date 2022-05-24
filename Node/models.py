from django.db import models

class NodeManager(models.Manager):

    def create_node(self, name):
        node = self.create(name=name)
        node.save()
        return node

    def edit_name(self, pk, new_name):
        if new_name != "" and pk is not None:
            print(new_name)
            node = self.get_queryset().filter(pk=pk).update(name=new_name)
            

class Node(models.Model):
    name = models.CharField(max_length=30)
    
    nodes = NodeManager()