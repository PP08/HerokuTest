from django.shortcuts import render
from .forms import BookForm
# Create your views here.

def hompage(request):
    if  request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save()
            return render(request, 'mysite/hompage.html', {'book': book})
    else:
        form = BookForm()
    return render(request, 'mysite/hompage.html', {'form': form})