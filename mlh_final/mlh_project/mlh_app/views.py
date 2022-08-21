from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm
from .models import Blog

# The code below is to display the User Registration Page and capture the details in the database
def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)

                return redirect('login')

        context = {'form': form}
        return render(request, 'travel/register.html', context)

# The code below is to display the User Login Page and do validations as well
def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username OR password is incorrect')

        context = {}
        return render(request, 'travel/login.html', context)

# The code below is to allow the user to logout
def logoutUser(request):
    logout(request)
    return redirect('login')


# @login_required(login_url='login')
# def main_page(request):
#     blog_rows = Blog.objects.all()
#
#     context = {'blog_data': blog_rows}
#     return render(request, 'travel/main_page.html', context)
#
# @login_required(login_url='login')
# def insert(request):
#     blog_record = Blog(name=request.POST['name'], topic=request.POST['topic'], description=request.POST['description'])
#     blog_record.save()
#     return redirect('/')


from django.shortcuts import render, redirect
from .models import *
from .forms import *


# Create your views here.
@login_required(login_url='login')
def home(request):
    forums = forum.objects.all()
    count = forums.count()
    discussions = []
    for i in forums:
        discussions.append(i.discussion_set.all())

    context = {'forums': forums,
               'count': count,
               'discussions': discussions}
    return render(request, 'travel/home.html', context)

@login_required(login_url='login')
def asia(request):

    forums = forum.objects.all()
    count = forums.count()
    discussions = []
    forums = forums.filter(topic='Asia')

    context = {'forums': forums,
               'count': count,
               'discussions': discussions}
    return render(request, 'travel/asia.html', context)

@login_required(login_url='login')
def africa(request):

    forums = forum.objects.all()
    count = forums.count()
    discussions = []
    forums = forums.filter(topic='Africa')

    context = {'forums': forums,
               'count': count,
               'discussions': discussions}
    return render(request, 'travel/africa.html', context)

@login_required(login_url='login')
def northAmerica(request):

    forums = forum.objects.all()
    count = forums.count()
    discussions = []
    forums = forums.filter(topic='North America')

    context = {'forums': forums,
               'count': count,
               'discussions': discussions}
    return render(request, 'travel/northAmerica.html', context)

@login_required(login_url='login')
def southAmerica(request):
    forums = forum.objects.all()
    count = forums.count()
    discussions = []
    forums = forums.filter(topic='South America')

    context = {'forums': forums,
               'count': count,
               'discussions': discussions}
    return render(request, 'travel/southAmerica.html', context)

@login_required(login_url='login')
def antarctica(request):

    forums = forum.objects.all()
    count = forums.count()
    discussions = []
    forums = forums.filter(topic='Antarctica')

    context = {'forums': forums,
               'count': count,
               'discussions': discussions}
    return render(request, 'travel/antarctica.html', context)

@login_required(login_url='login')
def europe(request):
    forums = forum.objects.all()
    count = forums.count()
    discussions = []
    forums = forums.filter(topic='Europe')

    context = {'forums': forums,
               'count': count,
               'discussions': discussions}
    return render(request, 'travel/europe.html', context)

@login_required(login_url='login')
def oceania(request):
    techlist = forum.topic

    forums = forum.objects.all()
    count = forums.count()
    discussions = []
    forums = forums.filter(topic='Oceania')

    context = {'forums': forums,
               'count': count,
               'discussions': discussions}
    return render(request, 'travel/oceania.html', context)

@login_required(login_url='login')
def addInForum(request):
    form = CreateInForum()
    if request.method == 'POST':
        form = CreateInForum(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'travel/addInForum.html', context)

@login_required(login_url='login')
def addInDiscussion(request):
    form = CreateInDiscussion()
    if request.method == 'POST':
        form = CreateInDiscussion(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'travel/addInDiscussion.html', context)

from django.shortcuts import render
from .forms import UploadFileForm
from django.views.decorators.csrf import ensure_csrf_cookie

@login_required(login_url='login')
def upload_display_video(request):

    if request.method == 'POST':
        print(f"***** upload_display_video :{request.FILES}")
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            print(f"##### file if form.is_valid: {file.name}")
            handle_uploaded_file(file)
            return render(request, "travel/upload-display-video.html", {'filename': file.name})
    else:
        form = UploadFileForm()
    return render(request, 'travel/upload-display-video.html', {'form': form})

def handle_uploaded_file(f):
    with open(f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

@login_required(login_url='login')
def points(request):

    forums = forum.objects.all()
    count = forums.count()
    discussions = []

    context = {'forums': forums,
               'count': count,
               'discussions': discussions}
    return render(request, 'travel/points.html', context)

