from django import forms

class IntegerRecordForm(forms.Form):
	value = forms.IntegerField(label='Значение')

class FloatRecordForm(forms.Form):
	value = forms.FloatField(label='Значение')