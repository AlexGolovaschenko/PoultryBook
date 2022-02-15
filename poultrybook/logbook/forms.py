from django import forms
from .models import CNT_CHOICES

class IntegerRecordForm(forms.Form):
	content_type = forms.ChoiceField(widget=forms.HiddenInput(), required=True, choices=CNT_CHOICES)
	value = forms.IntegerField(label='Значение')

class FloatRecordForm(forms.Form):
	content_type = forms.ChoiceField(widget=forms.HiddenInput(), required=True, choices=CNT_CHOICES)
	value = forms.FloatField(label='Значение')

class TextRecordForm(forms.Form):
	content_type = forms.ChoiceField(widget=forms.HiddenInput(), required=True, choices=CNT_CHOICES)
	value = forms.CharField(label='Сообщение', max_length=200)