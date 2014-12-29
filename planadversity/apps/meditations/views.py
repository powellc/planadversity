import json
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, FormView
from django.views.generic import DetailView, ListView, View
from django.core import serializers
from django.core.urlresolvers import reverse
from django.template.loader import render_to_string

from .models import Meditation, Topic, Technology, Event, Buzz
from workers.models import Worker
from .forms import MeditationForm, TopicForm, EventForm, TechnologyForm, BuzzForm
from .utils import send_email
from braces import views


class JsonView(views.CsrfExemptMixin,
               views.JsonRequestResponseMixin,
               views.JSONResponseMixin, View):
    pass


class MeditationUpdateView(views.LoginRequiredMixin, UpdateView):
    model = Meditation
    form_class = MeditationForm


class MeditationDetailView(JsonView, DetailView):
    model = Meditation


class MeditationListJSONView(JsonView, ListView):
    model = Meditation
    json_dumps_kwargs = {u"indent": 2}

    def get(self, request, *args, **kwargs):
        context = serializers.serialize('json',
                                        self.get_queryset().all())

        return self.render_json_response(context)


'''
class MeditationJoinView(JsonView, views.LoginRequiredMixin):
    """ A view that checks the request object for an 
    authenticated user and, if found, adds them to the 
    project member group.
    """
    def get(self, request, *args, **kwargs):
        user = self.request.user
        html = ''
        fragments = {}
        success = False
        project = Meditation.objects.get(slug=kwargs['slug'])
        if user.is_authenticated() and not user in project.members.all():
            project.members.add(user)
            project.save()
            success = True
            html = "<p class='leave-button' ><a href='{0}' class='btn btn-danger ajax' data-replace='.leave-button'><i class='fa fa-times'></i> Leave project</a></p>".format(reverse('project-leave', args=[project.slug]))
            fragments['.member-thumbs'] = render_to_string('honey/_member_list.html', {'members': project.members.all()})
        return self.render_json_response(
            {'user': user.username, 'html': html, 'fragments': fragments})



class MeditationLeaveView(JsonView, views.LoginRequiredMixin):
    """ A view that checks the request object for an 
    authenticated user and, if found, adds them to the 
    project member group.
    """
    def get(self, request, *args, **kwargs):
        user = self.request.user
        html = ''
        fragments = {}
        success = False
        project = Meditation.objects.get(slug=kwargs['slug'])
        if user.is_authenticated() and user in project.members.all():
            project.members.remove(user)
            project.save()
            html = "<p class='join-button' ><a href='{0}' class='btn btn-success ajax' data-replace='.join-button'><i class='fa fa-plus'></i> Join project</a></p>".format(reverse('project-join', args=[project.slug]))
            success = True
            fragments['.member-thumbs'] = render_to_string('honey/_member_list.html', {'members': project.members.all()})
        return self.render_json_response(
            {'user': user.username, 'html': html, 'fragments': fragments})
'''


class MeditationListView(JsonView, ListView):
    model = Meditation
    form_class = MeditationForm

