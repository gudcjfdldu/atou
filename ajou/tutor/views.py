from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout

from django.contrib.auth import login as auth_login

from tutor.models import UserProfile

error_dict = {

    'register-required': 'you have to register account',

    'match-password': 'please match both password',

    'same-username': 'already have been same username',

    'account-disabled': 'The password is valid, but the account the has been disabled!',

    'input-mustbeset': 'The given username and password must be set',

    'input-incorrect': 'The username and password incorrect',

}

def index(request):
    if request.method == 'GET':
        return render(request, 'tutor/index.html')


def login_handler(request):
    if request.method == 'GET':
        if request.user.is_authenticated():
            return HttpResponseRedirect(reverse('index'))
        
    elif request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                auth_login(request, user)
                return HttpResponseRedirect(reverse('index'))
            error_code = 'account-disabled'
        else:
            error_code = 'input-incorrect'
        context = {'error_message': error_dict[error_code]}
        return render(request, 'tutor/signup.html', context)
    if request.GET.get('error_code', ''):
        error_code = request.GET.get('error_code')
    else:
        return render(request, 'tutor/index.html')
    context = {'error_message': error_dict[error_code]}
    return render(request, 'tutor/index.html', context)  


def logout_handler(request):
    if request.method == 'GET':
        logout(request)
        return HttpResponseRedirect(reverse('index'))


def register(request):
    if request.method == 'GET':
        return render(request, 'tutor/signup.html')

    elif request.method == 'POST':
        name = request.POST.get('name', '')
        if name == '':
            context = {'error_message': error_dict['input-mustbeset']}
            print 'name'
            return render(request, 'tutor/signup.html', context)
        
        number = request.POST.get('number', '')
        if number == '':
            context = {'error_message': error_dict['input-mustbeset']}
            print 'number'
            return render(request, 'tutor/signup.html', context)
          
        major = request.POST.get('major', '')
        if major == '':
            context = {'error_message': error_dict['input-mustbeset']}
            
            print 'major' 
	    return render(request, 'tutor/signup.html', context)

        email = request.POST.get('email', '')
        if email == '':
            context = {'error_message': error_dict['input-mustbeset']}
            print 'email'
            return render(request, 'tutor/signup.html', context)       

        user_object_list = User.objects.all()
        username = request.POST.get('username', '')
        if username == '':
            context = {'error_message': error_dict['input-mustbeset']}
            print 'username'
            return render(request, 'tutor/signup.html', context)
        for user in user_object_list:
            if user.username == username:
                print 'same username'
                context = {'error_message': error_dict['same-username']}
                return render(request, 'tutor/signup.html', context)
        password = request.POST.get('password', '')
        confirm_password = request.POST.get('confirm', '')
        if password != confirm_password:
            print 'match password'
            context = {'error_message': error_dict['match-password']}
            return render(request, 'tutor/signup.html', context)
        else:
            user = User.objects.create_user(username, email, password)
            UserProfile.objects.create(name=name, number=number, major=major,  user=user, email=user.email)
            return HttpResponseRedirect(reverse('index'))



def board_teacher(request):
    if request.method == 'GET':
        return render(request, 'tutor/teacher.html')


def board_student(request):
    if request.method == 'GET':
        return render(request, 'tutor/student.html')
