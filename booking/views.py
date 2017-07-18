from django.shortcuts import render

def client_list(request):
    return render(request, 'booking/client_list.html', {})
