from django.shortcuts import render


def test_project(request):
    return render(request, 'test.html')