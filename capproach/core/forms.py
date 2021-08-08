from django import forms
from bootstrap_modal_forms.forms import BSModalModelForm
from core.models import Contact
from tempus_dominus.widgets import DatePicker, TimePicker, DateTimePicker

class ContactForm(BSModalModelForm):
	class Meta:
		model = Contact
		fields = '__all__'

class ContactFormExtra(BSModalModelForm):
	date_approach = forms.DateField(widget=DatePicker())