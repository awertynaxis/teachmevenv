# Create your views here.
from rest_framework import generics
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DayArchiveView, TodayArchiveView
from .models import Tasks, Room
from .serializers import RoomSerializer


class RoomListView(generics.ListCreateAPIView):
    serializer_class = RoomSerializer
    queryset = Room.objects.not_archived()


class RoomDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = RoomSerializer
    queryset = Room.objects.all()


def welcome(request):
    return render(request, template_name='welcome.html')


class ListRegistrationView(LoginRequiredMixin, ListView):
    model = Tasks
    template_name = 'show_registration.html'

    def get_queryset(self):
        return Tasks.objects.filter(user=self.request.user)


class Login(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = 'show_registration'


class ListTaskView(LoginRequiredMixin, ListView):
    model = Tasks
    template_name = 'show_task_detail.html'

    def get_queryset(self):
        id_s = self.kwargs.get('pk')
        return Tasks.objects.filter(id=id_s)


class ListCompletedView(LoginRequiredMixin, ListView):
    model = Tasks
    template_name = 'show_completed_details.html'

    def get_queryset(self):
        return Tasks.objects.filter(completed=True, user=self.request.user).all()


class ListUnCompletedView(LoginRequiredMixin, ListView):
    model = Tasks
    template_name = 'show_completed_details.html'

    def get_queryset(self):
        return Tasks.objects.filter(completed=False, user=self.request.user).all()


class CreateRegistrationView(CreateView):
    model = User
    template_name = 'registration.html'
    fields = ('email', 'password', 'username', 'first_name', 'last_name')

    def get_success_url(self):
        return reverse('welcome')


class CreateTaskView(LoginRequiredMixin, CreateView):
    model = Tasks
    template_name = 'createtasks.html'
    fields = ('title', 'description', 'date_created', 'date_completed', 'until_date', 'user')

    def get_success_url(self):
        return reverse('show_registration')


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Tasks
    fields = ('title', 'description', 'date_created', 'date_completed', 'until_date', 'completed')
    template_name = 'updatetask.html'

    def get_success_url(self):
        return reverse('show_registration')


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Tasks
    success_url = reverse_lazy('show_registration')
    template_name = 'deletetask.html'

    def get_object(self):
        id_s = self.kwargs.get('pk')
        return Tasks.objects.filter(id=id_s).first()


class TaskDayArchiveView(LoginRequiredMixin, DayArchiveView):
    date_field = 'date_created'
    allow_future = True
    template_name = 'archive_task_date.html'

    def get_queryset(self):
        return Tasks.objects.filter(user=self.request.user).all()


class TaskTodayArchiveView(LoginRequiredMixin, TodayArchiveView):
    allow_empty = True
    date_field = 'until_date'
    template_name = 'today.html'

    def get_queryset(self):
        return Tasks.objects.filter(user=self.request.user).all()


list_make_view = ListRegistrationView.as_view()
list_registration_view = CreateRegistrationView.as_view()
list_createtask_view = CreateTaskView.as_view()
update_task_view = TaskUpdateView.as_view()
delete_task_view = TaskDeleteView.as_view()
archive_task_date_view = TaskDayArchiveView.as_view(day_format='%d', month_format='%m', year_format='%Y')
archive_task_today_view = TaskTodayArchiveView.as_view()
list_task_view = ListTaskView.as_view()
list_completed_view = ListCompletedView.as_view()
list_uncompleted_view = ListUnCompletedView.as_view()
login_view = Login.as_view()
list_room_view = RoomListView.as_view()
details_room_view = RoomDetailView.as_view()
