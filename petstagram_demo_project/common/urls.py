from django.urls import path

from petstagram_demo_project.common.views import landing_page

urlpatterns = [
    path('', landing_page, name='index'),
    # path('testing2/', testing_view, name='testing_view'),
]
