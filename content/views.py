from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Photo, Comment
from .forms import PostImageForm,CommentForm
from django.contrib import messages


@login_required(login_url='/account/register/')
def dashboard(request):

    query = request.GET.get('q', None)
    if query is not None:
        photos = Photo.search(query)

    else:
        photos = Photo.objects.all()
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST,instance=request.user)
        if comment_form.is_valid():
            print(comment_form)
            comment_form.save()
    else:
        comment_form = CommentForm()
    
    return render(request, 'dashboard.html', {'section':'dashboard', 'photos':photos,'comment_form': comment_form, 'query':query})

def add_photo(request):
    if request.method == 'POST':
        image_form = PostImageForm(data=request.POST, files=request.FILES,instance=request.user)
        if image_form.is_valid():
            # image_form.save()
            instance = Photo(user=request.user, title=request.POST['title'], description=request.POST['description'],image=request.FILES['image'])
            instance.save()
            messages.success(request, 'Image post successifully added')
            return redirect('profile')
        else:
            messages.success(request, 'Errors')
    else:
        image_form = PostImageForm()

    return render(request, 'add_image.html', {'image_form': image_form})
