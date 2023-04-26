from django.shortcuts import render
from .models import Site
# Create your views here.
def home(request):
    sites=Site.objects.all()
    return render(request,'app/sitedetail.html',locals())