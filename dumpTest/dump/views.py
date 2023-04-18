from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Test, Question, Choice

# Create your views here.
def index(request):
    test_list = Test.objects.all()
    context = {
        'test_list' : test_list,
    }
    return render(request, 'dump/index.html', context)

def test(request, test_id):
    return HttpResponse(f'test id: {test_id}')

def test_question(request, test_id, question_id):
    return HttpResponse(f'test id: {test_id}, question_id: {question_id}')

def result(request, result):
    return HttpResponse("")