from django.shortcuts import render
from .models import Comments

def show_comments(request):
    return render(request, 'messages/index.html', {'comments':Comments.objects.all()})
