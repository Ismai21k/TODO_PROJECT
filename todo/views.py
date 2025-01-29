from django.shortcuts import render, redirect
from django.contrib import messages



# import todo form modles
from .forms import TodoForm
from .models import Todo

# Create your views here.

def home(request):# this function will display all todo items
    
    item_list = Todo.objects.order_by("-date") # get all todo items oreder by date
    
    
    if request.method == 'POST': #  check if the form is submitted
        forms = TodoForm(request.POST)
        if forms.is_valid():
            forms.save()
            messages.success(request, 'Todo Item added Successfully!!!')

            return redirect('home')
    else:
        return render(request, 'todo/index2.html/',{'item_list':item_list})
    

def remove(request, item_id): # this function will remove todo item
    item = Todo.objects.get(id=item_id)
    item.delete()
    messages.info(request, 'Todo Item removed!!!')
    return redirect('home')