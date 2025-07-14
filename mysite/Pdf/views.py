from django.shortcuts import render

# Create your views here.

def accept_data(request):
    return render(request,'pdf/accept_data.html')