from django.db import models



class Worksubmit(models.Model):
	uniqueID=models.CharField(max_length=70,null=True)
	work_from=models.TimeField(null=True)
	Work_Description=models.CharField(max_length=70,null=True)
	work_to=models.TimeField(null=True)

	def __str__(self):
		return str(self.uniqueID)


