from django.db import models

# Create your models here.
class Settings(models.Model):
	"""(Settings description)"""
	key = models.CharField(blank=False, max_length=100)
	value = models.CharField(blank=True, max_length=100)

	def __unicode__(self):
		return u"%s" % self.key

class Job(models.Model):
	"""(Job description)"""
	name = models.CharField(blank=True, max_length=100)
	config = models.TextField(blank=True)
	mainprogram = models.CharField(blank=True, max_length=100)
	reqRuns = models.IntegerField(blank=True, null=True)
	completeRuns = models.IntegerField(blank=True, null=True)
	def __unicode__(self):
		return u"%s" % self.name
		
class JobFile(models.Model):
	"""(JobFile description)"""
	jobfile = models.FileField(upload_to=jobfile)
	clientPath = models.CharField(blank=True, max_length=100)
	job = models.ForeignKey(Job)
	def __unicode__(self):
		return u"%s-%s" % (self.jobfile,self.job.name,)

class JobResult(models.Model):
	"""(JobResult description)"""
	job = models.ForeignKey(Job)
	data = models.TextField(blank=True)

	def __unicode__(self):
		return u"%s-%s" % s(elf.job.name,self.pk,)
class JobResultLine(models.Model):
	"""(JobResultLine description)"""
	result = models.ForeignKey(JobResult)
	key = models.CharField(blank=True, max_length=100)
 	strVal = models.CharField(blank=True, max_length=100)
	floatVal = models.FloatField()
	def __unicode__(self):
		return u"%s-%s-%s" % (self.result.job.name,self.result.pk,self.key)
