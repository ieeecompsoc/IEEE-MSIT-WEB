from django.shortcuts import render, redirect
from django.contrib import messages
from .models import shorturl
from django.contrib.auth.decorators import login_required
from django.core.validators import URLValidator
import random, string

@login_required
def dashboard(request, query=None):
    if not query or query is None:
        urls = shorturl.objects.all()
        return render(request, 'dashboard.html', { 'urls' : urls })
    else:
        try:
            check=shorturl.objects.get(short_query=query)
            check.visits=check.visits+1
            check.save()
            url_to_redirect=check.original_url
            validate = URLValidator()
            try:
                validate(url_to_redirect)
                return redirect(url_to_redirect)
            except:
                return render(request, 'event.html')
        except shorturl.DoesNotExist:
            print('here')
            return render(request, "dashboard.html", {'error':"error"})

def randomgen():
    return ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(6))

def generate_url(request):
    if request.method=='POST':
        if request.POST['original'] and request.POST['short']:
           
            original=request.POST['original']
            short=request.POST['short']
            check=shorturl.objects.filter(short_query=short)
            if not check:
                shorturl.objects.create(original_url=original, short_query=short)
                return redirect('/s')
            else:
                messages.error(request, "Already Exists")
                return redirect('/s')
        elif request.POST['original']:
            original=request.POST['original']
            generated=False
            while not generated:
                short=randomgen()
                check=shorturl.objects.filter(short_query=short)
                if not check:
                    shorturl.objects.create(original_url=original, short_query=short)
                    return redirect('/s')
                else:
                    continue

        else:
            messages.error(request, "Empty Fields")
            return redirect("/s")
    else:
        return redirect('/s')

@login_required
def edit_url(request, u_id=None):
    if request.method == 'POST':
        if request.POST['original']:
            shorturl.objects.filter(id=u_id).update(original_url=request.POST['original'])
            messages.success(request, "Original Url Edited Successfully!!")
        return redirect('dashboard')
    else:
        url=shorturl.objects.get(id=u_id)
        return render(request, 'edit.html', {'url': url})


@login_required
def remove_url(request,u_id =None):
    url = shorturl.objects.get(id=u_id)
    url.delete()
    return redirect('/s')