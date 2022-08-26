from django import forms
from .configs import CNT_CHOICES

class IntegerRecordForm(forms.Form):
	content_type = forms.ChoiceField(widget=forms.HiddenInput(), required=True, choices=CNT_CHOICES)
	value = forms.IntegerField(
				label='Значение',
				widget=forms.NumberInput(
					attrs={'class':'form-control', 'placeholder':'Введіть значення', 
							'autocomplete':'off'}
					)
				)

class FloatRecordForm(forms.Form):
	content_type = forms.ChoiceField(widget=forms.HiddenInput(), required=True, choices=CNT_CHOICES)
	value = forms.FloatField(
				label='Значение',
				widget=forms.NumberInput(
					attrs={'class':'form-control', 'placeholder':'Введіть значення', 
							'autocomplete':'off'}
					)
				)

class TextRecordForm(forms.Form):
	content_type = forms.ChoiceField(widget=forms.HiddenInput(), required=True, choices=CNT_CHOICES)
	value = forms.CharField(
				label='Сообщение', 
				max_length=400,
				widget=forms.Textarea(
					attrs={'class':'form-control', 'placeholder':'Введіть значення', 
							'rows': 2, 'autocomplete':'off'}
					)
				)


class RecordDemoForm(forms.Form):
	# choice field example
	choices = [
		('Вентилятор', 'Вентилятор'),
		('Приточний клапан', 'Приточний клапан'),
		('Тунельний клапан', 'Тунельний клапан'),
		('Лінія освітлення', 'Лінія освітлення'),
		('Лінія годування', 'Лінія годування'),
		('Щит силовий', 'Щит силовий'),
		('Щит керування', 'Щит керування'),
		('Датчик тиску', 'Датчик тиску'),
		('Інші датчики', 'Інші датчики'),
		('Обігрівачі', 'Обігрівачі'),
		('Лічильник води', 'Лічильник води'),
		('Інше', 	'Інше'),
	]
	actuator = forms.ChoiceField(label='Список', choices=choices,
		widget=forms.Select(
			attrs={'class':'form-control', 'placeholder':'Оберіть механізм', 
					'autocomplete':'off'}
			)
		)

	value = forms.FloatField(label='Число',
		widget=forms.NumberInput(
			attrs={'class':'form-control', 'placeholder':'введіть число...', 
					'autocomplete':'off'}
			)
		)

	text = forms.CharField(label='Текст', max_length=400,
		widget=forms.Textarea(
			attrs={'class':'form-control', 'placeholder':'введыть текст...', 
					'rows': 3, 'autocomplete':'off'}
			)
		)

	choices = [
		('Варіант 1', 'Варіант 1'),
		('Варіант 2', 'Варіант 2'),
		('Варіант 3', 'Варіант 3'),
	]
	radio = forms.ChoiceField(label='Оберіть варіант', choices=choices,
		widget=forms.RadioSelect(
			attrs={'class':'fix-forms form-check-input pl-5'}
		)
	)

	file = forms.FileField(label='Додайте файл', required=False,
		widget=forms.ClearableFileInput(
			attrs={'class':'form-control-file border mb-4'} 
		)
	)

	b1 = forms.BooleanField(label='Перевірка виконана', initial=False, required=False,
		widget=forms.CheckboxInput(
			attrs={'class':'fix-forms form-check-input ml-2'} 
		)
	)
	b2 = forms.BooleanField(label='Обляднання в нормі', initial=False, required=False,
		widget=forms.CheckboxInput(
			attrs={'class':'fix-forms form-check-input ml-2'} 
		)
	)
