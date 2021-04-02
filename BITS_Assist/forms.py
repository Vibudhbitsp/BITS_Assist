from django import forms
from django.contrib.auth.models import User
from BITS_Assist.models import answers


class UserAnswerForm(forms.ModelForm):
    
    class Meta:
        model = answers
        fields = ['content']
        type = 'submit'