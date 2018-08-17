from django.shortcuts import render
from django.http.response import Http404
from django.core.exceptions import ObjectDoesNotExist
from .models import Board

def home(request):
    boards = Board.objects.all()
    return render(request, 'home.html', {'boards': boards})

def board_topics(request, pk):
    try:
        board = Board.objects.get(pk=pk)
    except ObjectDoesNotExist:
        raise Http404
    return render(request, 'topics.html', {'board': board})