import datetime as dt
from random import randint

from django.views.generic import TemplateView, ListView

from rest_framework.generics import ListCreateAPIView

from .serializers import HistoryLogSerializer
from .models import HistoryLog


class HistoryApiView(ListCreateAPIView):
    serializer_class = HistoryLogSerializer
    queryset = HistoryLog.objects.all()


class LogHistoryMixin:

    def log(self, result):
        HistoryLog.objects.create(
            datetime=dt.datetime.now().isoformat(),
            url=self.request.path,
            result=result,
        )


class NumbersView(LogHistoryMixin, TemplateView):
    template_name = "numbers.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        rand_data = randint(0, 100)
        context["number"] = rand_data
        context['title'] = 'numbers'
        self.log(rand_data)
        return context


class RangeView(LogHistoryMixin, TemplateView):
    template_name = 'range.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if 'length' in kwargs:
            rand_numb_range = [randint(1, 100) for _ in range(int(kwargs['length']))]
        else:
            rand_numb_range = [randint(1, 100) for _ in range(randint(1, 100))]
        context['rand_numb_range'] = rand_numb_range
        context['title'] = 'numbers/range'
        self.log(rand_numb_range)
        return context


class HistoryView(ListView):
    paginate_by = 10
    model = HistoryLog
    template_name = 'history.html'
