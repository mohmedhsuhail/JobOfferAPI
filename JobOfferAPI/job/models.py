from django.db import models

class JobOffer(models.Model):
	company_name = models.CharField(max_length=120)
	company_email = models.EmailField()
	job_title = models.CharField(max_length=20)
	job_description = models.TextField()
	salary = models.PositiveIntegerField()
	created_at = models.DateTimeField(auto_now_add=True)
	available = models.BooleanField(default=False)

	def __str__(self):
		return f"{self.job_title} at {self.company_name}"