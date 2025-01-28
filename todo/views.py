from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse


# import todo form modles
from .forms import TodoForm
from .models import Todo

# Create your views here.

def home(request):
    
    item_list = Todo.objects.order_by("-date")
    
    
    if request.method == 'POST':
        forms = TodoForm(request.POST)
        if forms.is_valid():
            forms.save()
            messages.success(request, 'Todo Item added Successfully!!!')

            return redirect('home')
    else:
        return render(request, 'todo/index2.html/',{'item_list':item_list})
    

'''def remove(request, item_id):
    item = Todo.objects.get(id=item_id)
    item.delete()
    messages.info(request, 'Todo Item removed!!!')
    return redirect('home')'''