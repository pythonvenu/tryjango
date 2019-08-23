from django.shortcuts import render,redirect
from .forms import CommentForm, cars_model_form, ChoiceForm,ProductFormValidateForm,FormValidateTest
from .models import Car,Student,Marks,ItemDetails
from .forms import StudentForm, MarksForm,ItemForm
from django.forms import modelformset_factory
from django.db import transaction, IntegrityError
# Create your views here.
from django.contrib.auth.decorators import login_required
from django.forms import modelformset_factory

# tabular form

def modelformsetFactory(request):

    cformset = modelformset_factory(ItemDetails, form=ItemForm,extra=5)
    formset = cformset(request.POST or None,
                       queryset=ItemDetails.objects.all()
                       )

    if request.method == 'POST':
        formset = cformset(request.POST or None)
        if formset.is_valid():
            formset.save()
        formset = cformset(queryset=ItemDetails.objects.none())
    context = {'formset':formset}
    print('formset', formset)

    return render(request, 'FormWidgets/ItemDetails.html', context)

#Child master relation form
def create(request):
    context = {}
    MarksFormset = modelformset_factory(Marks, form=MarksForm,extra=5)
    form = StudentForm(request.POST or None)
    formset = MarksFormset(request.POST or None, queryset= Marks.objects.none(), prefix='marks')
    if request.method == "POST":
        if form.is_valid() and formset.is_valid():
            try:
                with transaction.atomic():
                    student = form.save(commit=False)
                    student.save()

                    for mark in formset:
                        data = mark.save(commit=False)
                        data.student = student
                        data.save()
            except IntegrityError:
                print("Error Encountered")

        return redirect('Slist')

    context['formset'] = formset
    context['form'] = form
    return render(request, 'multi_forms/create.html', context)

def list(request):
	datas = Student.objects.all()
	return render(request, 'multi_forms/list.html', {'datas':datas})


def FormWidgets_view(request):
    form = CommentForm(request.POST)
    #print(form)
    if form.is_valid():
        print('is valid')
        form.save()
        form = CommentForm()
    contaxt = {
        'form': form
    }

    return render(request, "FormWidgets/FormWidgets.html", contaxt)

def CarsModelForm_view(request):
    form = cars_model_form(request.POST, request.FILES)
    print('formdata', form)
    print('file', request.FILES)
    if form.is_valid():
        print('is valid')
        form.save_m2m()
        form = CommentForm()
    contaxt = {
        'form': form
    }

    return render(request, "FormWidgets/Media.html", contaxt)

def CarsModelFormDisplay_view(request):
    obj = Car.objects.all()
    contaxt = {
        'obj': obj
    }

    return render(request, "FormWidgets/CarMOdelDetails.html", contaxt)

def ChoiceForm_view(request):
    form = ChoiceForm()
    if form.is_valid():
        form.save()
        form = CommentForm()
    contaxt = {
        'form': form
    }
    return render(request, "FormWidgets/ChoiceField.html", contaxt)


def ProductFormValidate_view(request):

    form = ProductFormValidateForm(request.POST)
    print(form)
    if form.is_valid():
        form.save()
        form = ProductFormValidateForm()
    contaxt = {
        'form': form
    }

    return render(request, "FormWidgets/Product_Create_formValidate.html", contaxt)


def FormValidateTest_view(request):
    form = FormValidateTest()
    if request.method == 'POST':
        form = FormValidateTest(request.POST)
        if form.is_valid():
            print('formdata', form.cleaned_data)
            form.clean()
            #form.save()
            form = FormValidateTest()
    contaxt = {
        'form': form
    }
    return render(request, "FormWidgets/FormValidateExample2.html", contaxt)

