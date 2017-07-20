from django.shortcuts import render

def book_property_list(request):
    return render(request, 'book_property/Bookproperty_list.html', {})
