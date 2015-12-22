from django.db import models
import os, csv

# Create your models here.
class Sourcefile(models.Model):
	uploaddate = models.DateTimeField(auto_now_add=True, editable=True)
	datafile = models.FileField(upload_to='datafiles/%Y/%m/%d')
	parseddata = models.TextField(null=True, blank=True)

	def name(self):
        	return os.path.basename(self.datafile.name)

	def __str__(self):
		return self.name

	def readfile(self):
		with open(self.datafile.path) as fp:
			fileiter = fp.read().splitlines()
			readfile = ''
			for line in fileiter:
				readfile = readfile + line + '\n'
			return readfile


