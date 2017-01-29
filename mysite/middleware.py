from myapp.models import *

class ReferMiddleware():
	"""docstring for ReferMiddleware"""
	def process_request(self, request):
		referencia = request.GET.get('ref')
		try:
			obj = Codigos.objects.get(referencia=referencia)
		except:
			obj = None

		if obj:
			request.session['code_id_ref'] = obj.id_code