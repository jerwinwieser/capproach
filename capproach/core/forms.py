from django import forms
from bootstrap_modal_forms.forms import BSModalModelForm
from core.models import Contact, Test
from tempus_dominus.widgets import DatePicker, TimePicker, DateTimePicker

class ContactForm(BSModalModelForm):
	class Meta:
		model = Contact
		fields = '__all__'

# class ContactFormExtra(forms.ModalForm):
# 	name = forms.CharField()
# 	# date_approach = forms.DateField(widget=DatePicker())

class TestForm(forms.Form):
	class Meta:
		model = Test
		field = '__all__'