from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from registration.forms import LoginForm
from registration.models import Register

# Create your views here.
def home(request):
    if request.method == "POST":
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
                return render_to_response('fail_home.html', {'form':form},
                                          context_instance=RequestContext(request))
    else:
        form = LoginForm()
    return render_to_response('index.html', {'form':form},
                              context_instance=RequestContext(request))

def successful_login(request):
    return render_to_response('successful_login.html',)

def guide(request):
    if request.method == "POST":
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
                return render_to_response('fail_guide.html', {'form':form},
                                          context_instance=RequestContext(request))
    else:
        form = LoginForm()
    return render_to_response('guide.html', {'form':form},
                              context_instance=RequestContext(request))


