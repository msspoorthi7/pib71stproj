from django import forms

# class studentform(forms.Form):
#     student_ID = forms.IntegerField()
#     student_name = forms.CharField()
#     course = forms.CharField()
#     jdate = forms.DateField()

from Hello.models import students

from django.forms import ModelForm
class studentform(ModelForm):
    class Meta:
        model = students
        # fields = 'all' or
        fields = ['student_ID','student_name','course','jdate']

# creating a form to add a student

form = studentform()
