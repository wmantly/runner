import base64, json
from django.views.generic import View
from django.http import JsonResponse
import subprocess

class index(View):
	def get(self, request):
		return JsonResponse({"message": "no gets"})

	def post(self, request):
		code = base64.b64decode(request.POST.get('code').encode())
		code = 'export NODE_PATH=/var/www/runner/node_modules; {}'.format(code)
		res = base64.b64encode(subprocess.getoutput(code).encode())

		return JsonResponse({'res': res.decode()})
