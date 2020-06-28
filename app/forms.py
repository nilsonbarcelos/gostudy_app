from django import forms
from .models import Course

# Use form validation from model
class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        exclude = ('user', )
        fields = '__all__'