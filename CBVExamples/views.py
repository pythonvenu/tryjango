from django.shortcuts import render, get_object_or_404,reverse
from django.views.generic import (ListView, DetailView,CreateView,UpdateView,DeleteView)
from .models import Article,Course
from .forms import ArticleModelForm,MyCourseForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View

# Create your views here.
class ArticleListView(ListView):
	template_name = 'article_list.html'
	queryset = Article.objects.all()

class ArticleDetailView(DetailView):
	template_name = 'CBVExamples/article_detail.html'
	queryset = Article.objects.all()


@method_decorator(login_required, name='dispatch')
class ArticleCreateView(CreateView):
	template_name = 'CBVExamples/article_create.html'
	form_class = ArticleModelForm
	queryset = Article.objects.all()


class ArticleUpdateView(UpdateView):
    template_name = 'CBVExamples/article_create.html'
    form_class = ArticleModelForm

    def get_object(self):
        _id = self.kwargs.get("id")  # kwargs which are passed from the url
        print('_id:', _id)
        return get_object_or_404(Article, id=_id)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)


class ArticleDeleteView(DeleteView):
    template_name = 'CBVExamples/article_delete.html'

    def get_object(self):
        _id = self.kwargs.get("id")  # kwargs which are passed from the url
        print('_id:', _id)
        return get_object_or_404(Article, id=_id)

    def get_success_url(self):  # successfull delete it will route to the article_list view. if your comment ths it throws error
        return reverse('article:article-list')


#Functional Base views to Class Based VIews
class CourseView(View):
    template_name = 'about.html'
    #GET method
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})

# HTTP MEthods  functional based view
def MyFbv(request, *args, **kwargs):
    return render(request, 'about.html', {})

#RAW detail Class Based View examples

class CourseView(View):
    template_name = 'CBVExamples/course_details.html'  # default template
    # GET method
    def get(self, request, id=None, *args, **kwargs):
        obj = Course.objects.all()
        context = {"object" : obj}
        print('object', obj)
        context = {}
        if id is not None:
            print('id :', id)
            obj = get_object_or_404(Course, id=id)
            print('obj:', obj)
            context = {"object" : obj}
        return render(request, self.template_name, context)

#RAW list clas based View

class CourseListView(View):
    template_name = 'CBVExamples/course_list.html'
    queryset =  Course.objects.all()

    def get(self, request, *args, **kwargs):
        context = {"object_list" : self.queryset}
        return render(request, self.template_name, context)

class MyListView(CourseListView):
    queryset = Course.objects.filter(id=1)

class CourseObjectMixin(object): # here object is python object, we can replace this function where get_object is used which reduce the redundency
    model = Course
    lookup = 'id'
    def get_object(self):
        _id = self.kwargs.get(self.lookup)
        obj = None
        if _id is not None:
            obj = get_object_or_404(Course, id=_id)
        return obj

#RAW create Class Based Views

class CourseCreateView(CourseObjectMixin,View):
    template_name = 'CBVExamples/course_create.html'  #default template
    #GET method
    def get(self, request, *args, **kwargs):
        # GET method
        form = MyCourseForm()
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        # GET method
        form = MyCourseForm(request.POST)
        if form.is_valid():
            form.save()  # save model form data into DB
        context = {'form': form}
        return render(request, self.template_name, context)

#Raw Update Class Based View
class CourseUpdateView(CourseObjectMixin,View):
    template_name = 'CBVExamples/course_update.html'  # default template
    """
    def get_object(self):
        _id = self.kwargs.get("id")
        obj = None
        print('_id:', _id)
        if _id is not None:
            obj = get_object_or_404(Course, id=_id)
        return obj
    """

    # GET method
    def get(self, request, id=None, *args, **kwargs):
        # GET method
        context = {}
        obj = self.get_object()
        print('obj', obj)
        if obj is not None:
            form = MyCourseForm(instance=obj)
        context = {'form': form, 'object': obj}
        return render(request, self.template_name, context)

    def post(self, request, id=None, *args, **kwargs):
        # GET method
        context = {}
        obj = self.get_object()
        print('obj:', obj)
        if obj is not None:
            form = MyCourseForm(request.POST, instance=obj)
            print('update done1', form)
            if form.is_valid():
                form.save()
                print('obj:', obj)
            context['object'] = obj
            context['form'] = form
        return render(request, self.template_name, context)

#Raw Delete Class Based View
class CourseDeleteView(CourseObjectMixin,View):
    template_name = 'CBVExamples/course_delete.html'  # default template
    """
    def get_object(self):
        _id = self.kwargs.get("id")
        obj = None
        print('_id:', _id)
        if _id is not None:
            obj = get_object_or_404(Course, id=_id)
        return obj
    """
    # GET method
    def get(self, request, id=None, *args, **kwargs):
        # GET method
        context = {}
        obj = self.get_object()
        print('obj', obj)
        if obj is not None:
            form = MyCourseForm(instance=obj)
        context = {'form': form, 'object': obj}
        return render(request, self.template_name, context)

    def post(self, request, id=None, *args, **kwargs):
        # GET method
        context = {}
        obj = self.get_object()
        print('obj:', obj)
        if obj is not None:
            obj.delete()
            context['object'] = None
        return render(request, self.template_name, context)