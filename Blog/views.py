from django.shortcuts import render,get_object_or_404, redirect
from Blog.models import Blog
from Blog.forms import BlogForm

# Create your views here.
def home_view(request):
    queryset = Blog.objects.all()
    blogs = {'blogs': queryset}
    return render(request,"home.html", blogs)

def detail_view(request, id):
    obj = get_object_or_404(Blog,id=id)
    context = {'object': obj}
    return render(request,"detail.html", context)

def create_view(request):

     if request.method == "POST":
         form = BlogForm(request.POST,request.FILES)
         if form.is_valid():
             form.save()
             form = BlogForm()
             return redirect('home')
     else:
         form = BlogForm()

     return render(request,"create.html",{'form': form})

def update_view(request,id):

    obj = Blog.objects.get(id=id)
    form = BlogForm(instance=obj)

    if request.method == "POST":
        form = BlogForm(request.POST,request.FILES,instance=obj)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request,"update.html", {'form': form})

def delete_view(request, id):

    obj = get_object_or_404(Blog, id=id)
    if request.method == "POST":
        obj.delete()
        return redirect('/')
    else:
        context = {'obj': obj}
        return render(request,"delete.html", context)