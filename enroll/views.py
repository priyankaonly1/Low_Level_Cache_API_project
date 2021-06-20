from django.shortcuts import render
from django.core.cache import cache
# Create your views here.

def home(request):
    mv = cache.get('movie','has_expired')
    if mv == 'has_expired':
        cache.set('movie','The Manjhi', 30)
        mv = cache.get('movie')

    return render(request, 'enroll/course.html', {'fm':mv})