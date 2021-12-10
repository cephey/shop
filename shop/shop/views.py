import random
import uuid
import json

from django.http import HttpResponse
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = str(random.randint(10, 20))
        return context


def index_view(request, *args, **kwargs):
    name = str(uuid.uuid4())
    content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Title</title>
    </head>
    <body>
    
    {request.META}
    
    </body>
    </html>
    """
    # content = json.dumps(request.META)
    return HttpResponse(content)
