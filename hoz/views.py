from django.shortcuts import render

def main(request):
    return render(request, 'hoz/main.html', {})

def furniture(request):
    return render(request, 'hoz/furniture.html', {})

def mattress(request):
    return render(request, 'hoz/mattress.html', {})
