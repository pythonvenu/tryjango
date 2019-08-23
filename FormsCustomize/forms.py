from django import forms
from .models import Car
from myapp.models import Product
from django.contrib.auth.models import User
from .myformsCommonValidations import SpecialCharCheck
from datetime import datetime, timedelta, date
from .models import Student, Marks,ItemDetails

class ItemForm(forms.ModelForm):
    class Meta:
        model = ItemDetails
        fields = [
        'itemname',
        'itemDesc',
        'itemPrice'
        ]

        labels = {
            'itemname': 'Item Name',
            'itemDesc': 'Item Description',
            'itemPrice': 'Price',
        }

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student

        fields = [
            'name',
            'gender',
            'age',
        ]

        labels = {
            'name': 'Name',
            'gender':'Gender',
            'age':'Age',
        }


class MarksForm(forms.ModelForm):
    class Meta:
        model = Marks

        fields = [
            'class_name',
            'english',
            'nepali',
        ]

        widgets = {
            'class_name': forms.TextInput(attrs={'class': 'formset-field'}),
            'english': forms.TextInput(attrs={'class': 'formset-field'}),
            'nepali': forms.TextInput(attrs={'class': 'formset-field'})
        }


    # attr settting from static file
class CommentForm(forms.Form):
    name = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'fieldRequired'}))
    url = forms.URLField()
    comment = forms.CharField(widget=forms.TextInput(attrs={'size': '40'}))

class cars_model_form(forms.ModelForm):
    class  Meta:
        model=Car
        fields = '__all__'

BIRTH_YEAR_CHOICES = ['1980', '1981', '1982']
FAVORITE_COLORS_CHOICES = [
('blue', 'Blue'),
('green', 'Green'),
('black', 'Black'),
]

class ChoiceForm(forms.Form):
    birth_year = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
    favorite_colors = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=FAVORITE_COLORS_CHOICES,
    )

    # form validations
class ProductFormValidateForm(forms.ModelForm):

    title 	= forms.CharField(label='Title :', widget=forms.TextInput(attrs={"placeholder" : "your title"}))
    #email	= forms.EmailField()
    description = forms.CharField(required=False,
                                    widget=forms.Textarea(
                                    attrs={"placeholder" : "your Description ",
                                            'class': 'fieldRequired',
                                            "id" : "my new id for text area",
                                            "rows" : 20,
                                            "cols" : 120

                                          }
                                ))
    price = forms.DecimalField(initial=199.00)

    class Meta:
        model = Product
        fields = ['title', 'description', 'price']

    def clean_title(self, *args, **kwargs):   # syntax for filed validate is clean_<fildName>
        title = self.cleaned_data.get("title")
        print('title validation :', title)
        if  'CFE1' == title:
            print('inside :', title)
            raise forms.ValidationError("title is not correct value", "101")
        if  title in ["CFE", "ABC"]:
            raise forms.ValidationError("title is not correct value1" , "102")
        elif SpecialCharCheck(title):
            raise forms.ValidationError("Title Shouldnot contains Special Charaacters ", "103")
        return title


class FormValidateTest(forms.Form):
    DATE_INPUT_FORMATS = ('%d-%m-%Y', '%Y-%m-%d')

    email = forms.EmailField()
    username = forms.CharField(required=True, max_length=255, widget=forms.TextInput())
    password = forms.CharField(max_length=255, widget = forms.PasswordInput)
    password_repeat = forms.CharField(max_length=255, widget = forms.PasswordInput)
    DOB = forms.DateField(input_formats=DATE_INPUT_FORMATS)

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already exists" ,90001)
        return email

    def clean_DOB(self):
        dob = self.cleaned_data['DOB']
        print('typeofdob', type(dob))

        if dob > date.today():
            raise forms.ValidationError("Dob canot be future" ,90002)
        return dob

    def clean_username(self):
        data = self.cleaned_data['username']
        if not data.islower():
            raise forms.ValidationError("Usernames should be in lowercase")
        if '@' in data or '-' in data or '|' in data:
            raise forms.ValidationError("Usernames should not have special characters.")
        return data

    def clean(self):
        form_data = self.cleaned_data
        if form_data['password'] != form_data['password_repeat']:
            self._errors["password"] = ["Password do not match"]  # Will raise a error message
            del form_data['password']

        if SpecialCharCheck(form_data['password']):
            print("passworkd contaings special valid")
            return form_data
        else:
            print("passworkd doesnot containg special character")
            self._errors["password"] = ["Password doesnot contain Special character"]
            del form_data['password']
        return form_data
