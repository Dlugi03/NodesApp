from django.shortcuts import redirect, render

from .models import Node
from . import forms

# Create your views here.
def index(request):
    nodes = Node.objects.all()
    
    if nodes is not Node:
        return render(request, 'index.html', {'form': forms.AddNodeForm(), 'nodes': nodes})


def add_node(request):
    if request.method == 'POST':
        new_name = request.POST['name']
        
        if new_name is not None and new_name != "":
            n = Node(name=new_name)
            n.save()
            
    return redirect('/')

def remove_node(request, name):
    if request.method == 'POST':
        n = Node.objects.filter(name=name)
        n.delete()
    
    return redirect('/')