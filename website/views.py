from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from . forms import singUpForm
from . models import Post   
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import login_required

def first_site(request):
    return render(request, 'first-site.html')

def homePage(request):
    # checking if the user is login
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('homePage')   
        else:
            return redirect('homePage')
    else:
        return render(request, 'home.html')


def logout_user(request):
    logout(request)
    return redirect('homePage')


@login_required
def posts(request):
    if request.user.is_superuser:
        posts = Post.objects.all()
    else:
        posts = Post.objects.filter(post_published=True)
    return render(request, 'posts/post.html', {'post':posts})
        
def post_reading(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, 'posts/post_reading.html', {'post': post})
    



def add_post(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            post_title = request.POST['post_title']
            slug = request.POST['slug']
            body = request.POST['body']
            image = request.POST['image']
            creater = request.POST['creater']
            post_published = request.POST.get('post_published', False)
            post_create = Post(post_title=post_title, body=body, slug=slug,
                                image=image, creater=creater, post_published=post_published)
            post_create.save()
            return redirect('postPage')
        else:
            return redirect('postPage')
    else:
        return render(request, 'posts/add_post.html',)


def update_post(request, id):
    if request.user.is_authenticated:
        current_post = get_object_or_404(Post, pk=id)
        if request.method == 'POST':
            current_post.post_title = request.POST['post_title']
            current_post.slug = request.POST['post_slug']
            current_post.body = request.POST['post_body']
            current_post.image = request.POST['post_image']
            current_post.creater = request.POST['post_author']
            current_post.post_published = request.POST.get('post_published', False) == 'on'
            
            current_post.save()
            return redirect('postPage')
        else:
            return render(request, 'posts/update-post.html', {'post': current_post})
    return render(request, 'posts/update-post.html')



def delete_post(request, id):
    post = Post.objects.get(id=id)
    post.delete()
    return redirect('postPage')

def user_register(request):
    if request.method == 'POST':
        form = singUpForm(request.POST)
        if form.is_valid():
            form.save()
            # authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('homePage')
    else:
        form = singUpForm()
        return render(request, 'register_user/register.html', {
            'form':form
        })


    return render(request, 'register_user/register.html')



# custome filters
