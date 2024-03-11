from django.shortcuts import render,redirect
from .models import Todo
# Create your views here.
def home(request):
    todos = Todo.objects.all()
    if request.method == "POST":
        title = request.POST['title']
        if title !="":
            todo = Todo.objects.create(title=  title)
            todo.save()
    context = {"todos":todos}
    return render(request,'index.html',context)
def done(request,pk):
            todo = Todo.objects.get(id = pk)
            if todo.is_done != True:
                  todo.is_done = True
            else:
                  todo.is_done = False
            todo.save()
            return redirect('home')

def update(request,pk):
      todo = Todo.objects.get(id = pk)
      if request.method == 'POST':
            if request.POST['title'] != '': 
                  todo.title = request.POST['title']
                  todo.save()           
                  return redirect('home')

      context = {"update":todo}
      return render(request,'update.html',context)

def delete(request,pk):
      todo = Todo.objects.get(id = pk)
      todo.delete()
      return redirect('home')