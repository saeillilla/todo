from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
# Create your views here.
from .models import Todo
@login_required
def home(request):
    if request.method == 'POST':
        data = request.POST['textarea1']
        obj = Todo(user = request.user, todo =data )
        obj.save()
        print(data)
        return redirect('/')
    if request.method == 'GET':
        obj = Todo.objects.filter(user = request.user)
        return render(request,'list/home.html',{'notes':obj})

def delete_entry(request,id):
    obj = Todo.objects.get(id = id)
    obj.delete()
    return redirect('/')