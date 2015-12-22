from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=40)
    parent = models.ForeignKey('self', null=True, blank=True)
    def __str__(self):     
        if self.parent is None:
		return self.name
	else:
		return str(self.parent) + '>' + self.name	

    class Meta:
	verbose_name_plural = "Categories"

class Transaction(models.Model):
    date = models.DateField('transaction date')
    raw = models.CharField('raw description',max_length=200)
    friendly = models.CharField('friendly description',max_length=100, blank=True)
    amount = models.DecimalField(max_digits=10,decimal_places=2)
    category = models.ForeignKey(Category, null=True)
    def __str__(self):      
        return str(self.date) + ' ' + self.friendly

class Match_Rules(models.Model):
    matchtext = models.CharField('text to match',max_length=200)
    friendly = models.CharField('friendly description',max_length=100)
    def __str__(self):
	return self.matchtext


