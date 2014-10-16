from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import get_object_or_404, render
import os


from xls import sheets, lift


def index(request):
    template = loader.get_template('front/index.html')
    context = RequestContext (request)

    # return HttpResponse("Hello, kitty.")
    return HttpResponse(template.render(context))

def api(request, *args):
    return HttpResponse("meow")

def js(request, js):
    return HttpResponse (
            loader.get_template (
                os.path.join ( 'front/js'
                             , js)
                                ) . render (RequestContext (request))
                        )
            
