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
    # if kwargs['function_name'] == "a1":
    #     return HttpResponse(lift(sheets(kwargs['function_args'])[0]))
    # if args[0] == "a1":
        # return HttpResponse (lift(sheets(os.path.join(settings.STATIC_ROOT, 'refmart.xlsx'))[0]))
    return HttpResponse ("\n".join(["{", "'lalafa':'lalafa'", "}"]))
    # return HttpResponse('lalafa')

def js(request, js):
    return HttpResponse (
            loader.get_template (
                os.path.join ( 'front/js'
                             , js)
                                ) . render (RequestContext (request))
                        )
            
