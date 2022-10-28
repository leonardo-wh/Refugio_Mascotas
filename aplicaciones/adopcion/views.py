from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, UpdateView

from aplicaciones.adopcion.models import Persona, Solicitud
from aplicaciones.adopcion.forms import PersonaForm, SolicitudForm

# Create your views here.

def index_adopcion(request):
	return HttpResponse("pag principal de la app adopcion")


def solicitud_view(request):
	if request.method=='POST':
		form = SolicitudForm(request.POST)
		form2 = PersonaForm(request.POST)
		if form.is_valid() and form2.is_valid():
			solicitud = form.save(commit=False)
			solicitud.persona = form2.save()
			solicitud.save()
			return redirect('adopcion:solicitud_listardef')
	else:
		form=SolicitudForm()
		form2=PersonaForm()
	return render(request, 'adopcion/solicitud_form.html', {'form':form, 'form2':form2})

def solicitud_list(request):
	solicitud = Solicitud.objects.all().order_by('id')
	contexto = {'solicitudes':solicitud}
	return render(request, 'adopcion/solicitud_list.html', contexto)



def solicitud_edit(request, pk):
	solicitud = Solicitud.objects.get(id=pk) 
	persona = Persona.objects.get(id=solicitud.persona_id) 

	if request.method == 'GET':
		form = SolicitudForm(instance=solicitud)
		form2 = PersonaForm(instance=persona)
	else:
		form = SolicitudForm(request.POST, instance=solicitud)
		form2 = PersonaForm(request.POST, instance=persona)
		if form.is_valid() and form2.is_valid():
			solicitud = form.save(commit=False)
			solicitud.persona = form2.save()
			solicitud.save()
		return redirect('adopcion:solicitud_listardef')
	return render(request, 'adopcion/solicitud_form.html', {'form':form, 'form2':form2})

def solicitud_delete(request, pk):
	solicitud = Solicitud.objects.get(id=pk)
	if request.method == 'POST':
		solicitud.delete()

		return redirect('adopcion:solicitud_listardef')
	return render(request, 'adopcion/solicitud_delete.html', {'adopcion':solicitud})

















class SolicitudList(ListView):
	model = Solicitud
	template_name = 'adopcion/solicitud_list.html'

class SolicitudCreate(CreateView):
	model = Solicitud
	template_name = 'adopcion/solicitud_form.html'
	form_class = SolicitudForm
	second_form_class = PersonaForm
	success_url = reverse_lazy('adopcion:solicitud_listar')

	def get_context_data(self, **kwargs):
		context = super(SolicitudCreate, self).get_context_data(**kwargs)
		if 'form' not in context:
			context['form'] = self.form_class(self.request.GET)
		if 'form2' not in context:
			context['form2'] = self.second_form_class(self.request.GET)
		return context

	def post(self, request, *args, **kwargs):
		self.object = self.get_object
		form = self.form_class(request.POST)
		form2 = self.second_form_class(request.POST)
		if form.is_valid() and form2.is_valid():
			solicitud = form.save(commit=False)
			solicitud.persona = form2.save()
			solicitud.save()
			return HttpResponseRedirect(self.get_success_url())
		else: 
			return self.render_to_response(self.get_context_data(form=form, form2=form2))


class SolicitudUpdate(UpdateView):
	model = Solicitud
	
	second_model = Persona
	template_name = 'adopcion/solicitud_form.html'
	form_class = SolicitudForm
	second_form_class = PersonaForm
	success_url = reverse_lazy('adopcion:solicitud_listar')

	def get_context_data(self, **kwargs):
		context = super(SolicitudUpdate, self).get_context_data(**kwargs)
		pk = self.kwargs.get('pk', 0)
		solicitud = self.model.objects.get(id=pk)
		persona = self.second_model.objects.get(id=solicitud.persona_id)

		if 'form' not in context:
			context['form'] = self.form_class()
		if 'form2' not in context:
			context['form2'] = self.second_form_class(instance=persona)
		context['id']=pk
		return context

	def post(self, request, *args, **kwargs):
		self.object = self.get_object
		id_solicitud = kwargs['pk']
		solicitud= self.model.objects.get(id=id_solicitud)
		persona = self.second_model.objects.get(id=solicitud.persona_id)
		form = self.form_class(request.POST, instance=solicitud)
		form2 = self.second_form_class(request.POST, instance=persona)
		if form.is_valid() and form2.is_valid():
			form.save()
			form2.save()
			return HttpResponseRedirect(self.get_success_url())
		else:
			return HttpResponseRedirect(self.get_success_url())


class SolicitudDelete(DeleteView):
	model = Solicitud
	template_name = 'adopcion/solicitud_delete.html'
	success_url = reverse_lazy('adopcion:solicitud_listar')