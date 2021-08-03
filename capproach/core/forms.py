from django import forms
from bootstrap_modal_forms.forms import BSModalModelForm
from core.models import Contact

class ContactForm(BSModalModelForm):
	class Meta:
		model=User
		fields='__all__'