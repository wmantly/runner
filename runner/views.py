import base64, json
from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponse, JsonResponse
from runner.helper import SuperSecureInterpreter

class index(View):
	def get(self, request):
		return JsonResponse({"message": "no gets"})

	def post(self, request):
		pandoras_box = SuperSecureInterpreter(request.POST.get('code'),language=request.POST.get('language'))
		pandoras_box.open()
		context = {'code': pandoras_box.code_string, 'res': pandoras_box.result}

		return JsonResponse({'res': pandoras_box.result})
