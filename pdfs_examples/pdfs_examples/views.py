from django.http import HttpResponse
from django.views.generic import View
from django.template.loader import get_template

from .utils import render_to_pdf 

class GeneratePdf(View):
    def get(self, request, *args, **kwargs):
        context = {
            'invoice_id': 123456,
            'customer_name': 'Ricardo Milos',
            'amount': '1981.99',
            'today': 'Today',
        }
        html = render_to_pdf(context)
        return HttpResponse(html)