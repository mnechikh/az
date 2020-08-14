from django.shortcuts import render
from django.template.response import TemplateResponse
from project_app.models import appointments
from django.views.generic.base import TemplateView
from django.views.generic import DetailView
from .forms import appointmentForm
from django.shortcuts import redirect
from django.shortcuts import get_list_or_404, get_object_or_404
import bootstrap3
from django.contrib.auth.decorators import login_required

# Create your views here.



class appointmentsdetail(DetailView):
	template_name = 'appointment_files/view_appointment.html'
	model = appointments
@login_required
def appoint_remove(request, pk):
    appointments_model = get_object_or_404(appointments, pk=pk)
    appointments_model.delete()
    return redirect('view')

@login_required
def schedule(request):
	return render(request, 'appointment_files/schedule.html')
@login_required
def appointment(request):
	return render(request, 'appointment_files/appointment.html')
@login_required
def view(request):
	data = appointments.objects.all()
	return TemplateResponse(request, 'appointment_files/view.html' , {"data": data})

@login_required
def post_new(request):
	if request.method == "POST":
		form = appointmentForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.save()
			return redirect('appointmentsdetail',pk=post.pk)
	else:
		form=appointmentForm()
		return render(request, 'appointment_files/appointments_form.html',{'form':form})

def contact(request):
	if request.method == "POST":
		message_name = request.POST['message-name']
		message_email = request.POST['message-email']
		message = request.POST['message']

		#send email
		send_mail(
			message_name,# subject
			message,# message
			message_email,# from
			['mnechikh@yahoo.com'],# to
		)

		return render(request, 'contact.html', {'message_name': message_name})

	else:
		return render(request, 'contact.html', {})

def about(request):
	return render(request, 'about.html', {})

def pricing(request):
	return render(request, 'pricing.html', {})

def service(request):
	return render(request, 'service.html', {})

def home(request):
	return render(request, 'home.html', {})






