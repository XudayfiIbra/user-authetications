from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from . forms import singUpForm
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
    return render(request, 'posts/post.html')


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
