from django.urls import re_path

from .views import NumbersView, RangeView, HistoryView, HistoryApiView


urlpatterns = [
    re_path(r'^$', NumbersView.as_view(), name='numbers'),
    re_path(r'^range/$', RangeView.as_view(), name='range'),
    re_path(r'^range/(?P<length>\d+)/$', RangeView.as_view(), name='length_range'),
    re_path(r'^history/', HistoryView.as_view(), name='history'),
    re_path('^rest-api-hist', HistoryApiView.as_view(), name='rest_api_hist'),
]
