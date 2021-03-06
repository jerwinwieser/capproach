from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Contact(models.Model):
	AGE_CHOICES = [(i,i) for i in range(15, 50)]
	DURATION_CHOICES = [('Short', 'Short'), ('Medium', 'Medium'), ('Long', 'Long')]
	INTERACTION_CHOICES = [(i,i) for i in range(1, 11)]
	LOOKS_CHOICES = [(i,i) for i in range(1, 11)]
	BOOLEAN_CHOICES = [('yes', 'Yes'),('no', 'No')]
	GROUP_SIZE_CHOICES = [(i,i) for i in range(1, 10)]
	date_approach = models.DateField(default=timezone.now)
	location = models.CharField(max_length=30, blank=False)
	group_size = models.IntegerField(blank=True, null=True, choices=GROUP_SIZE_CHOICES, default=1)
	name = models.CharField(max_length=30, blank=False)
	age = models.IntegerField(blank=True, null=True, choices=AGE_CHOICES, default=22)
	nationality = models.CharField(max_length=30, blank=True, null=True)
	duration = models.CharField(max_length=30, choices=DURATION_CHOICES, default='Medium', blank=True, null=True)
	interaction = models.IntegerField(blank=True, null=True, choices=INTERACTION_CHOICES, default=7)
	looks = models.IntegerField(blank=True, null=True, choices=LOOKS_CHOICES, default=7)
	close = models.CharField(max_length=30, choices=BOOLEAN_CHOICES, default='yes', blank=True)
	reply = models.CharField(max_length=30, choices=BOOLEAN_CHOICES, default='no', blank=True)
	date = models.CharField(max_length=30, choices=BOOLEAN_CHOICES, default='no', blank=True)
	lay = models.CharField(max_length=30, choices=BOOLEAN_CHOICES, default='no', blank=True)
	comments = models.TextField(blank = True, max_length=300)
	created_at = models.DateTimeField(editable=False, default=timezone.now)
	updated_at = models.DateTimeField(editable=False, default=timezone.now)
	created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, editable=False)

	def __str__(self):
		return self.name


class Test(models.Model):
	name = models.CharField(max_length=30)