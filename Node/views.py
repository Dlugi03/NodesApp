from django.shortcuts import redirect, render

from .models import Node
from . import forms

# Create your views here.
def index(request):
    nodes = Node.nodes.all()
    
    if nodes is not None:
        return render(request, 'index.html', {'add_form': forms.AddNodeForm(), 'nodes': nodes, 'edit_form': forms.EditNodeForm()})


def add_node(request):
    if request.method == 'POST':
        new_name = request.POST['name']
        
        if new_name is not None and new_name != "":
            n = Node.nodes.create_node(name=new_name)
            
    return redirect('/')

def edit_node(request, name):
    if request.method == 'POST':
        ni = Node.nodes.filter(name=name).values('pk')[0]['pk']
        Node.nodes.edit_name(pk=ni, new_name=request.POST['new_name'])

    return redirect('/')


def remove_node(request, name):
    if request.method == 'POST':
        n = Node.nodes.filter(name=name)
        n.delete()
    
    return redirect('/')