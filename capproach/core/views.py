from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView, FormView
from core.models import Contact
from django.urls import reverse, reverse_lazy


class ContactListView(ListView):
	model = Contact

class ContactCreateView(CreateView):
	model = Contact
	fields = '__all__'
	success_message = 'Success: Contact was added.'
	def get_success_url(self):
		return reverse('contact_list')

class ContactDeleteView(DeleteView):
	model = Contact
	success_message = 'Success: Contact was deleted.'
	def get_success_url(self):
		return reverse('contact_list')