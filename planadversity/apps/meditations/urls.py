from django.conf.urls import patterns, url
from .views import (MeditationListView, MeditationDetailView, MeditationCreateView, 
                    MeditationUpdateView, MeditationListJSONView, MeditationJoinView,
                    MeditationLeaveView)


# custom views
urlpatterns = patterns(
    '',
    url(r'^meditation/add/',
        view=MeditationCreateView.as_view(),
        name="project-create"),

    url(r'^meditations/(?P<slug>[-\w]+)/edit/',
        view=MeditationUpdateView.as_view(),
        name="project-update"),

    url(r'^meditations.json',
        view=MeditationListJSONView.as_view(),
        name="project-list-json"),

    url(r'^meditations/(?P<slug>[-\w]+)/',
        view=MeditationDetailView.as_view(),
        name="project-detail"),

    #url(r'^meditations.csv',
    #    view=MeditationListCSVView.as_view(),
    #    name="project-list-csv"),

    url(r'^meditations/$',
        view=MeditationListView.as_view(),
        name="project-list"),

    url("^$", 
        BuzzListView.as_view(template_name='homepage.html'), 
        name="homepage")
)
