"""tryjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from myapp.views import (homepage, homehtml,BootStrap,rawHtml,
    Product_object_list_view, product_Rawcreate_view,Product_update_view,product_delete_view,
                         prod_ModelForm_create_view,prod_ModelForm_CRUD_view,
                         ProductDjangoForm_view,ProductDjangoForm_CRUD_view,
                        caluate_view,
                        snippetListView,
                        search
                         )
from RestAPIExample.views import CryptoHome,price
from FormsCustomize.views import FormWidgets_view,CarsModelForm_view,CarsModelFormDisplay_view,\
    ChoiceForm_view,ProductFormValidate_view, FormValidateTest_view,create,list,modelformsetFactory

from django.conf import settings
from django.conf.urls.static import static
from django_filters.views import FilterView  #django pre-defined filter
from myapp.filter import UserFilter  # custom filter

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage, name='homepage'),
    path('hhome/', homehtml, name='hhome'),
    path('Bstrap/', BootStrap, name='bstrap'),
    path('rawhtml/', rawHtml, name='rawhtml'),
    path('ProdRawCreate/', product_Rawcreate_view, name='ProdRawCreate'),
    path('ProdList/', Product_object_list_view, name='ProdList'),
    path('ProdList/Produpdate/<int:my_id>/', Product_update_view, name='ProdRawUpdate'),
    path('ProdDelete/<int:my_id>/', product_delete_view, name='ProdRawDelete'),
    #handing CRUD operation with one view
    # ModelForm
    path('ProdMFCreate/', prod_ModelForm_create_view, name='ProdMFCreate'),
    path('ProdMFCRUD/', prod_ModelForm_CRUD_view, name='ProdMFCRUD'),
    # Django Forms
    path('ProdDFCreate/', ProductDjangoForm_view, name='ProdDFCreate'),
    path('ProdDFCRUD/', ProductDjangoForm_CRUD_view, name='ProdDFCRUD'),
    path('PTRCalc/', caluate_view, name='PTRCalc'),
    # formsCustomize application
    path('FormWidgets/', FormWidgets_view, name='Formwidgets'),
    # static (css,js,img..)
    path('StaticMedia/', CarsModelForm_view, name='StaticMedia'),
    # media files
    path('StaticMediaRead/', CarsModelFormDisplay_view, name='StaticMediaRead'),
    # form widgets & form validations
    path('ChoiceField/', ChoiceForm_view, name='ChoiceField'),
    path('FormValidate/', ProductFormValidate_view, name='FormValidate'),
    path('FormValidate2/', FormValidateTest_view, name='FormValidate2'),
    # class Based View
    path('CBVExamples/', include('CBVExamples.urls')),
    #Tabular Form and Child Master forms
    path('MarksTab/', modelformsetFactory, name='MarksTab'), #tabular form
    path('childMasterCreate/', create, name='childMasterCreate'), #master master relationship form
    path('Slist/', list, name='slist'),
    # Rest API examples
    path("CryptoHome/", CryptoHome, name="CryptoHome"),
    path("Cryptoprice/", price, name="Cryptoprice"),
    #filter forms
    path('snippetList/', snippetListView.as_view(), name="snippetList"),
    path('search/', search, name='search'),
    path('searchC/', FilterView.as_view(filterset_class=UserFilter,template_name='myapp/user_list.html'), name='searchC'),
    ]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)