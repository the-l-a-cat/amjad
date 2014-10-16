from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import get_object_or_404, render
from django.conf import settings
import os


from xls import sheets, lift


def index(request):
    template = loader.get_template('front/index.html')
    context = RequestContext (request)

    # return HttpResponse("Hello, kitty.")
    return HttpResponse(template.render(context))

# def api(request, **kwargs):
def api(request, *args):
    if args[0] == "a1":
        return HttpResponse ("\n".join(["{", "'lala':'fa'", "}"]))
    elif args[0] == "lift_sheet":
        return HttpResponse (lift (sheets (os.path.join(settings.STATIC_ROOT, args[1]) )[int(args[2])]))
    # return HttpResponse('lalafa')

def js(request, js):
    return HttpResponse (
            loader.get_template (
                os.path.join ( 'front/js'
                             , js)
                                ) . render (RequestContext (request))
                        )
            
