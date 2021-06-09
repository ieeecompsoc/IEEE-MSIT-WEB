from django.shortcuts import render, redirect
from django.contrib import messages
from .models import shorturl
import random, string


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
            return redirect(url_to_redirect)
        except shorturl.DoesNotExist:
            return render(request, "dashboard.html", {'error':"error"})
    
def randomgen():
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(6))

def generate(request):
    if request.method=='POST':
        pass
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

def function(request,u_id =None):
    object = shorturl.objects.get(id=u_id)
    object.delete()
    return redirect('/s')