from django import forms

class EmailSendForm(forms.Form):
 name=forms.CharField()
 email=forms.EmailField()
 to=forms.EmailField()
 comments=forms.CharField(required=False,widget=forms.Textarea)

from bloga.models import Commentm
class CommentsForm(forms.ModelForm):
 class Meta:
  model=Commentm
  fields=('name','email','body')