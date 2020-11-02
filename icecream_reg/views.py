from django.shortcuts import render

# Create your views here.
def icecream_registr(request):
    return render(request, 'icecream_reg/icecream.html')