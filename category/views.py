from django.shortcuts import render, redirect
from category.forms import TaskCategoryForm
# Create your views here.
def category(request):
    if request.method == 'POST':
        form = TaskCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = TaskCategoryForm()
    return render(request,'category.html',{"form": form})
    