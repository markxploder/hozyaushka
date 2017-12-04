from django.shortcuts import render

def main(request):
    return render(request, 'hoz/main.html', {})

def furniture(request):
    return render(request, 'hoz/furniture.html', {})
