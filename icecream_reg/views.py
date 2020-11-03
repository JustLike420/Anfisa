from django.shortcuts import render
from icecream.models import Icecream
# Create your views here.
def icecream_registr(request):
    if request.method == 'POST':
        icecream = request.POST['name']
        description = request.POST['description']
        b = Icecream(name=icecream, description=description)
        b.save()
    return render(request, 'icecream_reg/icecream.html')