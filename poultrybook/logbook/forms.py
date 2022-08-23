from django import forms
from .configs import CNT_CHOICES

class IntegerRecordForm(forms.Form):
	content_type = forms.ChoiceField(widget=forms.HiddenInput(), required=True, choices=CNT_CHOICES)
	value = forms.IntegerField(
				label='Значение',
				widget=forms.NumberInput(
					attrs={'class':'form-control', 'placeholder':'Введіть значення'}
					)
				)

class FloatRecordForm(forms.Form):
	content_type = forms.ChoiceField(widget=forms.HiddenInput(), required=True, choices=CNT_CHOICES)
	value = forms.FloatField(
				label='Значение',
				widget=forms.NumberInput(
					attrs={'class':'form-control', 'placeholder':'Введіть значення'}
					)
				)

class TextRecordForm(forms.Form):
	content_type = forms.ChoiceField(widget=forms.HiddenInput(), required=True, choices=CNT_CHOICES)
	value = forms.CharField(
				label='Сообщение', 
				max_length=400,
				widget=forms.Textarea(
					attrs={'class':'form-control', 'placeholder':'Введіть значення', 
							'rows': 2}
					)
				)