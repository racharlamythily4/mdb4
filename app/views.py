from django.shortcuts import render

# Create your views here.
def mdb(request):
    return render(request,'mdb.html')

def carousel(request):
    return render(request,'carousel.html')

def dropdowns(request):
    return render(request,'dropdowns.html')

def collapse(request):
    return render(request,'collapse.html')

def backgroundimg(request):
    return render(request,'backgroundimg.html')
 