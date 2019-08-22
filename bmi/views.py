from django.shortcuts import render
from django.http import HttpResponse
from .models import BMI
from django.forms import modelform_factory
from django.shortcuts import redirect
from django.urls import reverse

# Create your views here.

def index(request):
    number1 = request.GET.get("number1", "")
    number2 = request.GET.get("number2", "")

    if not number1.isnumeric():
        number1 = 0

    if not number2.isnumeric():
        number2 = 0

    sum = float(number1) + float(number2)
    return render(request, 'bmi/index.html', {"no1":number1, "no2":number2, "sum":sum})

def bmi_list(request):
    object_list = BMI.objects.all()
    return render(request, "bmi/bmi_list.html", {"object_list":object_list})

def bmi_enter(request):
    BMIForm = modelform_factory(BMI, fields=['height','weight'])
    form = BMIForm()

    if request.method == "POST":
        form = BMIForm(request.POST)
        if form.is_valid():
            instance = form.save()
            return redirect(reverse("list"))
    else:
        form = BMIForm()
    return render(request, "bmi/bmi_create.html", {'form':form})

def bmi_update(request, pk):
    BMIForm = modelform_factory(BMI, fields=['height','weight'])
    instance = BMI.objects.get(pk=pk)

    form = BMIForm()
    if request.method == "POST":
        form = BMIForm(request.POST, instance=instance)
        if form.is_valid():
            instance = form.save()
            return redirect(reverse("list"))
    else:
        form = BMIForm(instance=instance)
    return render(request, "bmi/bmi_update.html", {'form':form})

def bmi_detail(request, pk):
    object = BMI.objects.get(pk=pk)
    return render(request, "bmi/bmi_detail.html", {"object":object})

def bmi_delete(request, pk):
    object = BMI.objects.get(pk=pk)
    object.delete()
    return redirect(reverse("list"))