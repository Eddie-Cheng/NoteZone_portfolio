from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from content.forms import DetailForm
from registration.models import Register
from content.models import Detail
from registration import views

# Create your views here.
def content(request):
    username = request.session['email']
    user = Register.objects.get(email=username)
    if request.method == 'POST':
        form = DetailForm(request.POST, request.FILES)
        if form.is_valid():
            sentence = form.cleaned_data['sentence']
            https = form.cleaned_data['https']
            anyfile = form.cleaned_data['anyfile']
            content = Detail()
            content.email = user
            content.sentence = sentence
            content.https = https
            content.anyfile = anyfile
            content.save()
    else:
        form = DetailForm()
    photo = Detail.objects.filter(email_id=user)
    return render_to_response('content.html',
                              {'form':form, 'username':user, 'photo':photo}, 
                              context_instance=RequestContext(request))

def detail_delete(request, pk):
    if request.method == 'POST':
        Detail.objects.get(pk=pk).delete()
        return HttpResponseRedirect('/content/')
    return render_to_response('content.html',
                              {'form':form, 'username':user, 'photo':photo},
                              context_instance=RequestContext(request))

def logout(request):
    del request.session['email']
    del request.session['password']
    return render_to_response('successful_logout.html',
                              context_instance=RequestContext(request))

def content_home(request):
    user = request.session['email']
    return render_to_response('content_home.html', {'username':user},
                              context_instance=RequestContext(request))

def content_guide(request):
    user = request.session['email']
    return render_to_response('content_guide.html', {'username':user},
                              context_instance=RequestContext(request))
