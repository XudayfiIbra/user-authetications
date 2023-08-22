from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from . forms import singUpForm
from . models import Post



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



def posts(request):
    posts = Post.objects.all()
    return render(request, 'posts/post.html', {'posts':posts})
        
def post_reading(request, slug):
    # this function is not complate
    post = Post.objects.get(slug=slug)
    return render(request, 'posts/post_reading.html', {'post': post})
    



def add_post(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            post_title = request.POST['post_title']
            slug = request.POST['slug']
            heading = request.POST['heading']
            paragraph_one = request.POST['paragraph_one']
            paragraph_two = request.POST['paragraph_two']
            paragraph_three = request.POST['paragraph_three']
            paragraph_four = request.POST['paragraph_four']
            image = request.POST['image']
            creater = request.POST['creater']
            post_create = Post(post_title=post_title, slug=slug,
                               heading=heading, image=image, creater=creater, paragraph_one=paragraph_one, paragraph_two=paragraph_two, paragraph_three=paragraph_three, paragraph_four=paragraph_four)
            post_create.save()
            return redirect('postPage')
        else:
            return redirect('postPage')
    else:
        return render(request, 'posts/add_post.html',)


def update_post(request):
    pass



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
