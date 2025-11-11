from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

from catalog.froms import BookForm
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

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            new_book = Book(
                title=form.cleaned_data['title'],
                author=form.cleaned_data['author'],
                published_date=form.cleaned_data['published_date'],
                isbn=form.cleaned_data['isbn']
            )
            new_book.save()
            return HttpResponse("Book added successfully!")
    else:
        form = BookForm()
    return render(request, 'add_book.html', {'form': form})

def add_book_model_form(request):
    from .forms import BookModelForm
    if request.method == 'POST':
        form = BookModelForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Book added successfully using ModelForm!")
    else:
        form = BookModelForm()
    return render(request, 'add_book.html', {'form': form})