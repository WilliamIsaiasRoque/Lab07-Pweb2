from django.http import HttpResponse
from django.views.generic import View
from django.template.loader import get_template

from .utils import render_to_pdf 

class GeneratePdf(View):
    def get(self, request, *args, **kwargs):
        template = get_template('pdf/invoice.html')
        context = {
            'invoice_id': 123456,
            'customer_name': 'Ricardo Milos',
            'amount': 1981.99,
            'today': 'Today',
        }
        html = template.render(context)
        pdf = render_to_pdf('pdf/invoice.html', context)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "Invoice_%s.pdf" %("666")
            content = "inline; filename=\"%s\"" %(filename)
            download = request.GET.get("download")
            if download:
                content = "attachment; filename=\"%s\"" %(filename)
            response['Content-Disposition'] = content    
            return response 
        return HttpResponse("Not found")