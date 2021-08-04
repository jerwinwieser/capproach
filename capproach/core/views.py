from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView, FormView
from django.views.generic.detail import DetailView
from django.db.models import Avg, Count, Min, Sum, IntegerField, Case, When, Value, F
from django.db.models.functions import ExtractWeek, ExtractYear, ExtractMonth
from django.urls import reverse, reverse_lazy
from core.models import Contact
from core.forms import ContactForm
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from bootstrap_modal_forms.generic import BSModalReadView, BSModalCreateView, BSModalDeleteView, BSModalFormView, BSModalUpdateView


@method_decorator(login_required, name='dispatch')
class StatisticsListView(ListView):
	'''
	Statistics:
	- n approaches
	- n closes
	- n dates
	- n lays
	'''

	template_name = 'core/statistics_list.html'
	model = Contact

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)

		user = self.request.user

		context['summary_week'] = Contact.objects \
		.filter(created_by=user) \
    	.annotate(week_number=ExtractWeek('date_approach')) \
		.values('week_number') \
		.annotate(approach_count=Count('close')) \
		.annotate(close_count=Sum(Case(When(close=True, then=1),
	        default=Value(0),
	        output_field=IntegerField()
	    ))) \
		.annotate(date_count=Sum(Case(When(date=True, then=1),
	        default=Value(0),
	        output_field=IntegerField()
	    ))) \
		.annotate(lay_count=Sum(Case(When(lay=True, then=1),
	        default=Value(0),
	        output_field=IntegerField()
	    ))) \
		.order_by('-week_number')

		context['summary_day'] = Contact.objects \
		.filter(created_by=user) \
		.values('date_approach') \
		.annotate(approach_count=Count('close')) \
		.annotate(close_count=Sum(Case(When(close=True, then=1),
	        default=Value(0),
	        output_field=IntegerField()
	    ))) \
		.annotate(date_count=Sum(Case(When(date=True, then=1),
	        default=Value(0),
	        output_field=IntegerField()
	    ))) \
		.annotate(lay_count=Sum(Case(When(lay=True, then=1),
	        default=Value(0),
	        output_field=IntegerField()
	    ))) \
		.order_by('-date_approach')

		return context

@method_decorator(login_required, name='dispatch')
class ContactListView(ListView):
	template_name = 'core/contact_list.html'
	model = Contact

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)

		user = self.request.user

		context['contact_list'] = Contact.objects \
		.filter(created_by=user) \
		.order_by('-date_approach', '-time_approach')

		return context

@method_decorator(login_required, name='dispatch')
class ContacReadView(BSModalReadView):
    model = Contact
    template_name = 'core/contact_read.html'

@method_decorator(login_required, name='dispatch')
class ContactCreateView(BSModalCreateView):
	template_name = 'core/contact_create.html'
	form_class = ContactForm
	model = Contact
	def form_valid(self, form):
		form.instance.created_by = self.request.user
		return super().form_valid(form)

	def get_success_url(self):
		return reverse('contact_list')

@method_decorator(login_required, name='dispatch')
class ContactUpdateView(BSModalUpdateView):
	template_name = 'core/contact_update.html'
	model = Contact
	form_class = ContactForm
	def get_success_url(self):
		return reverse('contact_list')

@method_decorator(login_required, name='dispatch')
class ContactDeleteView(BSModalDeleteView):
	template_name = 'core/contact_delete.html'
	model = Contact
	def get_success_url(self):
		return reverse('contact_list')
		
