from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView, FormView
from django.views.generic.detail import DetailView
from django.db.models import Avg, Count, Min, Sum, IntegerField, Case, When, Value, F
from django.db.models.functions import ExtractWeek, ExtractYear, ExtractMonth
from django.urls import reverse, reverse_lazy
from core.models import Contact, Test
from core.forms import ContactForm, TestForm
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from bootstrap_modal_forms.generic import BSModalReadView, BSModalCreateView, BSModalDeleteView, BSModalFormView, BSModalUpdateView
from django.contrib.auth.models import User

class TestCreateView(BSModalCreateView):
	template_name = 'core/test_create.html'
	form_class = TestForm
	model = Test
	def get_success_url(self):
		return reverse('contact_list')

class modelFieldsInfo(TemplateView):
	template_name = 'core/model_fields_info.html'

# @method_decorator(login_required, name='dispatch')
class StatisticsListView(ListView):
	template_name = 'core/statistics_list.html'
	model = Contact

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)

		if self.request.user.is_authenticated:
			userid = self.request.user.id
		else:
			userid = User.objects.filter(groups__name__in=['demo']).values_list('id', flat=True).first()
			context['contact_demo_text'] = 'This is a DEMO page - signup or login to start logging your own approaches'

		context['performance'] = Contact.objects \
		.filter(created_by_id=userid) \
		.annotate(approach_count=Count('close')) \
		.annotate(close_count=Sum(Case(When(close='yes', then=1),
	        default=Value(0),
	        output_field=IntegerField()
	    ))) \
		.annotate(date_count=Sum(Case(When(date='yes', then=1),
	        default=Value(0),
	        output_field=IntegerField()
	    ))) \
		.annotate(lay_count=Sum(Case(When(lay='yes', then=1),
	        default=Value(0),
	        output_field=IntegerField()
	    ))) \
	    .aggregate(
	    	close_count_total=Sum('close_count'),
	    	approach_count_total=Sum('approach_count'),
	    	date_count_total=Sum('date_count'),
	    	lay_count_total=Sum('lay_count')
	    )

		context['summary_week']  = Contact.objects \
		.filter(created_by_id=userid) \
    	.annotate(week_number=ExtractWeek('date_approach')) \
		.values('week_number') \
		.annotate(approach_count=Count('close')) \
		.annotate(close_count=Sum(Case(When(close='yes', then=1),
	        default=Value(0),
	        output_field=IntegerField()
	    ))) \
		.annotate(date_count=Sum(Case(When(date='yes', then=1),
	        default=Value(0),
	        output_field=IntegerField()
	    ))) \
		.annotate(lay_count=Sum(Case(When(lay='yes', then=1),
	        default=Value(0),
	        output_field=IntegerField()
	    ))) \
		.order_by('-week_number')

		context['summary_day'] = Contact.objects \
		.filter(created_by_id=userid) \
		.values('date_approach') \
		.annotate(approach_count=Count('close')) \
		.annotate(close_count=Sum(Case(When(close='yes', then=1),
	        default=Value(0),
	        output_field=IntegerField()
	    ))) \
		.annotate(date_count=Sum(Case(When(date='yes', then=1),
	        default=Value(0),
	        output_field=IntegerField()
	    ))) \
		.annotate(lay_count=Sum(Case(When(lay='yes', then=1),
	        default=Value(0),
	        output_field=IntegerField()
	    ))) \
		.order_by('-date_approach')

		return context

# @method_decorator(login_required, name='dispatch')
class ContactListView(ListView):
	template_name = 'core/contact_list.html'
	model = Contact

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)

		if self.request.user.is_authenticated:
			userid = self.request.user.id
		else:
			userid = User.objects.filter(groups__name__in=['demo']).values_list('id', flat=True).first()

		context['contact_list'] = Contact.objects \
		.filter(created_by_id=userid) \
		.order_by('-date_approach', '-time_approach')

		return context

# @method_decorator(login_required, name='dispatch')
class ContacReadView(BSModalReadView):
    model = Contact
    template_name = 'core/contact_read.html'

# @method_decorator(login_required, name='dispatch')
class ContactCreateView(BSModalCreateView):
	template_name = 'core/contact_create.html'
	form_class = ContactForm
	model = Contact
	def form_valid(self, form):
		form.instance.created_by = self.request.user
		return super().form_valid(form)

	def get_success_url(self):
		return reverse('contact_list')

# @method_decorator(login_required, name='dispatch')
class ContactUpdateView(BSModalUpdateView):
	template_name = 'core/contact_update.html'
	model = Contact
	form_class = ContactForm
	def get_success_url(self):
		return reverse('contact_list')

# @method_decorator(login_required, name='dispatch')
class ContactDeleteView(BSModalDeleteView):
	template_name = 'core/contact_delete.html'
	model = Contact
	success_message = 'Approach successfully deleted.'
	def get_success_url(self):
		return reverse('contact_list')
		
