from django.db import models
from django.utils import timezone

class Contact(models.Model):
	name = models.CharField(max_length=100)
	age = models.IntegerField(default=99)

	created_at = models.DateTimeField(editable=False, default=timezone.now)
	updated_at = models.DateTimeField(editable=False, default=timezone.now)
	# created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, editable=False)

	def __str__(self):
		return self.name