from django import forms
from .models import Article,Course

class ArticleModelForm(forms.ModelForm):
	class Meta :
		model = Article
		fields = ['title', 'content', 'active']

class MyCourseForm(forms.ModelForm):
	class Meta:
		model = Course
		fields = ['title']