from django.shortcuts import render

# Create your views here.
def friends_registr(request):
    return render(request, 'friends_reg/friends.html')