from django.http import HttpResponse, Http404
from django.shortcuts import render
from .models import Dataset

def main(request):
    datasets = Dataset.objects.all()
    context = {'datasets':datasets}
    return render(request, 'datasets/main.html', context)

def description(request, slug):
    try:
        dataset = Dataset.objects.get(slug=slug)
        context = {'dataset': dataset, }
    except Dataset.DoesNotExist:
        raise Http404("The requested dataset does not exist (yet?).")
    return render(request, 'datasets/description.html', context)

def testing_page(request):
    #return HttpResponse("Successful test.")# % id)
    datasets = Dataset.objects.all()
    context = {'datasets':datasets}
    return render(request, 'datasets/test_main.html', context)

