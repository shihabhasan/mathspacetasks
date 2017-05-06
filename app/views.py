from django.shortcuts import render
import sys, subprocess

from rest_framework.views import APIView
from rest_framework.response import Response

from app.dice_probabilty import dice_probability
from app.walking_robot import walking_robot
from app.city_number import city_number


def home(request):
   return render(request, 'index.html')


def manual(request):
   return render(request, 'help.html')

def contact(request):
   return render(request, 'contact.html')

def thanks(request):
   name=request.POST['name']
   email=request.POST['email']
   subject=request.POST['subject']
   message=request.POST['message']
   command = "echo 'Name: '"+name+"'\nEmail: '"+email+"'\nMessage: '"+message+" | mutt -s 'MathSpaceTasks Query: '"+subject+" -- pharm.shihab@gmail.com"
   subprocess.call(command, shell=(sys.platform!="Linux"))
   return render(request, 'thanks.html', { 'name': name })


# -----------Task 1 app-----------------------------
def task1_app(request):
   result=walking_robot()
   context = {'result':result}
   return render(request, 'task1_app.html', context)


# -----------Task 2 app-----------------------------

def task2_app(request):
   if request.method == 'GET':
      return render(request, 'task2_app.html')
   if request.method == 'POST':
      n = request.POST.get('task2_input')
      try:
         probability=dice_probability(int(n))
         result = 'The probability for n = {0}:\n {1}'.format(n, probability)
         context = {'output_text':' Output Solution', 'result': result}
         return render(request, 'task2_app.html', context)
      except ValueError as error:
         context = {'result': error}
         return render(request, 'task2_app.html', context)
      except TypeError as error:
         context = {'result': error}
         return render(request, 'task2_app.html', context)
      except NoneType as error:
         context = {'result': error}
         return render(request, 'task2_app.html', context)


# -----------Task 3 app-----------------------------

def task3_app(request):
   if request.method == 'GET':
      return render(request, 'task3_app.html')
   if request.method == 'POST':
      city_name = request.POST.get('task3_input').lower()
      try:
         city_digit=city_number(city_name)
         result = 'The number for {0}:\n {1}'.format(city_name, city_digit)
         context = {'output_text':' Output Solution', 'result': result}
         return render(request, 'task3_app.html', context)
      except ValueError as error:
         context = {'result': error}
         return render(request, 'task3_app.html', context)
      except TypeError as error:
         context = {'result': error}
         return render(request, 'task3_app.html', context)
      except NoneType as error:
         context = {'result': error}
         return render(request, 'task3_app.html', context)


# -----------ERROR HANDLER-----------------------------

def handler500(request):
   context = {'ValueError': response.status_code}
   return render(request, '500.html', context)
   response.status_code = 500
   return response

# -----------API----------------------------
class ApiView(APIView):
    def get(self, request):
        param='mathspacetasks.shihabhsan.com/api/task{id}/{parameter}'
        context = {'Usage': param}
        return Response(context)
class Task1ApiView(APIView):
    def get(self, request):
         result = walking_robot()
         context = {'result': result}
         return Response(context)

class Task2ApiView(APIView):
    def get(self, request, n):
        try:
            probability=dice_probability(int(n))
            result = 'The probability for n = {0}:\n {1}'.format(n, probability)
            context = {'Output Solution': result}
        except ValueError as error:
            context = {'result': str(error)}
        except TypeError as error:
            context = {'result': str(error)}
        except NoneType as error:
            context = {'result': str(error)}
        return Response(context)

class Task3ApiView(APIView):
    def get(self, request, city_name):
        try:
            city_name=city_name.lower()
            city_digit = city_number(city_name)
            result = 'The number for {0}: {1}'.format(city_name, city_digit)
            context = {result}
        except ValueError as error:
            context = {'result': str(error)}
        except TypeError as error:
            context = {'result': str(error)}
        except NoneType as error:
            context = {'result': str(error)}
        return Response(context)