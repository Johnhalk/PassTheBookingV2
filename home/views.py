from django.shortcuts import render, get_object_or_404, redirect

def home_list(request):
    return render(request, 'home/home_list.html', {})
