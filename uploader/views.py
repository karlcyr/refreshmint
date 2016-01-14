from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.generic import FormView, DetailView, ListView
from .forms import DataFileForm, EditDataForm
from .models import Sourcefile
import csv, re

def tableize(inputfile):
	fileiter = inputfile.splitlines()	
	output = ""
	for line in fileiter:
		line = re.sub(r"^", "<tr><td>", line)
		line = re.sub(r"$", "</td></tr>", line)
		line = line.replace(',','</td><td>').replace('"','')
		output = output + line

	return output

def edit_data(request):
	if request.method == 'POST':
		post_text = request.POST.get('editdata')
		return HttpResponse(tableize(post_text))
	else:
		return HttpResponse('Invalid Request Type')
		

class UploadFileView(FormView):
	template_name = 'uploader/add/index.html'
	form_class = DataFileForm

	def form_valid(self, form):
			datafile = Sourcefile(datafile=self.get_form_kwargs().get('files')['datafile'])
			datafile.save()
			self.id = datafile.id

			return HttpResponseRedirect(self.get_success_url())

	def get_success_url(self):
		return reverse('datafile', kwargs={'pk': self.id})

class DataFileDetailView(DetailView):
	model = Sourcefile
	template_name = 'uploader/datafile.html'
	context_object_name = 'datafile'

	def  get_context_data(self, **kwargs):
		context = super(DataFileDetailView, self).get_context_data(**kwargs)
		source_file = super(DataFileDetailView, self).get_object()
		source_file.parseddata = source_file.readfile()
		source_file.save()

		context['filename'] = source_file.name
		context['htmldata'] = tableize(source_file.readfile())
		context['csvdata'] = source_file.parseddata
		context['form'] = EditDataForm()

		return context


class DataFileIndexView(ListView):
	model = Sourcefile
	template_name = 'uploader/datafile_view.html'
	context_object_name = 'datafiles'
	queryset = Sourcefile.objects.all()
