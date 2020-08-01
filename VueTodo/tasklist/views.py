from django.shortcuts import render
from django.views.generic import View


class TaskView(View):

    def get(self, request):
        return render(request, 'tasklist/list.html', context={'name': 'Stepanov'})