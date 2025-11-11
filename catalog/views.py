from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from .models import book

# Create your views here.
def hellow_world(request):
    now  = datetime.now()
    return HttpResponse(
        f'''
<html>
<body>
<h1>北商</h1>
<label>資管系</label>
<h3>{now}</h3>
</body>
</html>

        '''
    )

def index(request):
    return render(request, 'index.html')

def book_list(request):
    books = book.objects.all().order_by('title')
    return render(request, 'book_list.html', {'books': books})

def Book(request, pk):
    abook = book.objects.get(id=pk)
    return render(request, 'book.html', {'book': abook})
#444564564654