from django.urls import path


urlpatterns = [
    path('', TaskView.as_view(), name='task_list_url'),
]