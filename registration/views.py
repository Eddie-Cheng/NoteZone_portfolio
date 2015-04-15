from django.conf import settings
# from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from registration.forms import RegisterForm, LoginForm, ForgotForm
from registration.models import Register


# Create your views here.
def submit(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            website = form.cleaned_data['website']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = Register.objects.filter(email__exact = email)
            if user:
                return render_to_response('failregister.html',)
            else:
                Register.objects.create(first_name=first_name,
                                        last_name=last_name,
                                        website=website,
                                        username=username,
                                        email=email,
                                        password=password)
                request.session['username'] = username
                request.session['email'] = email
                request.session['password'] = password
                return HttpResponseRedirect('/successful/')
    else:
        form = RegisterForm()
    return render_to_response('register.html', {'form':form},
                              context_instance=RequestContext(request))

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = Register.objects.filter(email__exact = email,
                                           password__exact = password)
            if user:
                response = HttpResponseRedirect('/successful_login/')
                request.session['email'] = email
                request.session['password'] = password
                response.set_cookie('email', email, 3600)
                return response
            else:
                return render_to_response('fail.html', {'form':form},
                                          context_instance=RequestContext(request))
    else:
        form = LoginForm()
    return render_to_response('login.html', {'form':form},
                              context_instance=RequestContext(request))

def successful(request):
    return render_to_response('successful.html',)

def successful_login(request):
    return render_to_response('successful_login.html',)

def forgot_password(request):
    if request.method == 'POST':
        form = ForgotForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            user = Register.objects.filter(username__exact = username,
                                           email__exact = email)
            if user:
                member = Register.objects.filter(email = email)
                if member:
                    for word in member:
                        password = word.password

                #send_mail(subject, messages, from_email, to_list, fail_silently=True)
                subject = 'NoteZones for ours member!'
                message = 'Hi, '+ username + '\nYour password: ' + password
                from_email = settings.EMAIL_HOST_USER
                to_list = [email, settings.EMAIL_HOST_USER]

                send_mail(subject,message,from_email,to_list,fail_silently=True)
                
                return HttpResponseRedirect('/successful_password/')
            else:
                return render_to_response('failmail.html', {'form':form},
                                          context_instance=RequestContext(request))
    else:
        form = ForgotForm()                                          
    return render_to_response('forgot_password.html', {'form':form},
                              context_instance=RequestContext(request))

def successful_password(request):
    return render_to_response('successful_password.html',)




