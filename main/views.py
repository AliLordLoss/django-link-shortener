# from django.http import JsonResponse


# Create your views here.
# def create_link(request):
#     if request.method == "POST":
#         print(request.POST)
#         if not request.POST['url']:
#             return JsonResponse({
#                 "error": "URL is a required field!"
#             })

#         return JsonResponse({
#             "short_url": request.build_absolute_uri('/'),
#             "redirects_to": request.POST['url']
#         })

# def redirect(request, short_url):
#     pass

from rest_framework import viewsets
from django.http import Http404, HttpResponseRedirect
from .serializers import LinkMapSerializer
from .models import LinkMap

class LinkMapViewSet(viewsets.ModelViewSet):
    queryset = LinkMap.objects.all()
    serializer_class = LinkMapSerializer

def redirect(request, url):
    try:
        link_map = LinkMap.objects.get(short_url=url)

        link_map.times_followed += 1        

        link_map.save()
        
        return HttpResponseRedirect(link_map.redirects_to)
        
    except:
        raise Http404()
