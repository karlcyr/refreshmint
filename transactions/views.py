from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import FormView
from .forms import GetTransactionsForm

# Create your views here.
def index(request):
	return HttpResponse("Hello, world. You're at the transactions index.")

def view(request, transaction_id):
	return HttpResponse("You're looking at transaction %s." % transaction_id)

def edit(request, transaction_id):
	return HttpResponse("Editing transaction %s." % transaction_id)

def gettrans(request):
	transactionlist = request.POST.get('datafile', None)
	context = {
		'transactionlist' : transactionlist
	}
	return render(request, "transactions/gettrans.html", context)

#class GetTransView(FormView):
#	template_name = 'transactions/gettrans.html'
#	form_class = GetTransactionsForm
#
#	def form_valid(self, form):
#		rawfile = self.get_form_kwargs().get('files')['datafile']	
