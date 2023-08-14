from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from . forms import singUpForm
from . models import Post



def homePage(request):
    # checking if the use is login
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
    Posts = Post.objects.all()
    return render(request, 'posts/post.html', {'Posts':Posts})
        
def post_reading(request):
    # this is function not complate
    Posts = Post.objects.all()
    return render(request, 'posts/post_reading.html', {'Posts':Posts})



def add_post(request):
    if request.method == 'POST':
        post_title = request.POST['post_title']
        content = request.POST['content']
        image = request.POST['image']
        creater = request.POST['creater']
        post_create = Post(post_title=post_title,
                           content=content, image=image, creater=creater)
        post_create.save()
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
