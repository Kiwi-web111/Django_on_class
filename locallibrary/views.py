from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

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