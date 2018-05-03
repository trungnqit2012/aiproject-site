from django.shortcuts import render
from .models import Item
from django.template import  RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse
import re
import json
from urllib.request import urlopen

# Create your views here.
def index(request):
    
	# try:
	# 	product = Item.objects.all()[:3]
	# 	context = {
	# 		'top_product': product,
	# 	}
	# except Product.DoesNotExist:
	# 	raise Http404("Product does not exist")
	return get_location(request)

def get_location(request):
    url = 'http://ipinfo.io/json'
    response = urlopen(url)
    data = json.load(response)
    IP=data['ip']
    org=data['org']
    city = data['city']
    country=data['country']
    region=data['region']
    return HttpResponse('IP : %s <br/>Region : %s  <br/>Country : %s <br/>City : %s  <br/>Org : %s' % (IP,region,country,city,org))