from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView, FormView
from django.views.generic.detail import DetailView
from django.db.models import Avg, Count, Min, Sum
from django.db.models.functions import ExtractWeek, ExtractYear, ExtractMonth
from django.urls import reverse, reverse_lazy
from core.models import Contact
from datetime import datetime


class StatisticsListView(ListView):
	'''
	Statistics:
	- n approaches
	- n closes
	- n dates
	- n lays
	'''

	model = Contact
	template_name = 'core/statistics_list.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)

		context['summary_week'] = Contact.objects \
    	.annotate(week_number=ExtractWeek('date_approach')) \
		.values('week_number') \
		.annotate(approach_count=Count('close')) \
		.annotate(close_count=Sum('close')) \
		.annotate(date_count=Sum('date')) \
		.order_by('-week_number')

		context['summary_day'] = Contact.objects \
		.values('date_approach') \
		.annotate(approach_count=Count('close')) \
		.annotate(close_count=Sum('close')) \
		.annotate(date_count=Sum('date')) \
		.order_by('-date_approach')

		return context

class ContactListView(ListView):
	model = Contact

class ContactCreateView(CreateView):
	model = Contact
	fields = '__all__'
	success_message = 'Success: Contact was added.'
	def get_success_url(self):
		return reverse('contact_list')

class ContactUpdateView(UpdateView):
	model = Contact
	fields = '__all__'
	success_message = 'Success: Contact was updated.'
	def get_success_url(self):
		return reverse('contact_list')

class ContactDeleteView(DeleteView):
	model = Contact
	success_message = 'Success: Contact was deleted.'
	def get_success_url(self):
		return reverse('contact_list')
