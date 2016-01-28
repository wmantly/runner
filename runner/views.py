import base64, json
from django.views.generic import View
from django.http import JsonResponse
import subprocess
from project.settings import NODE_PATH

class index(View):
	def get(self, request):
		return JsonResponse({"message": "no gets"})

	def post(self, request):
		code = base64.b64decode(request.POST.get('code').encode()).decode()
		code = 'export NODE_PATH={NODE_PATH}; {code}'.format(NODE_PATH=NODE_PATH,code=code)
		res = base64.b64encode(subprocess.getoutput(code).encode())

		return JsonResponse({'res': res.decode()})
