from django.shortcuts import render


def book_list(request):
    return render(request, 'book_list.html', {})
