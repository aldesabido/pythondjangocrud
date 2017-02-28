from django.shortcuts import render, get_object_or_404,redirect
from django.utils.dateparse import parse_date
from django.db import models
from math import ceil,floor
from django.http import HttpResponse,JsonResponse,StreamingHttpResponse
from random import randint
from datetime import datetime,timedelta,date
from copy import copy
import math,json,time,datetime as idatetime,copy as icopy,decimal,ast,csv,os,copy,re
from django.core import serializers
from operator import itemgetter
from decimal import Decimal
from time import mktime
from django.utils.termcolors import colorize
from django.core.serializers.json import DjangoJSONEncoder
from django.utils.encoding import smart_str
from django.conf import settings
from collections import OrderedDict
from django.db.models.functions import Coalesce
from django.forms.models import model_to_dict


def post_data(request):
	post_params = json.loads(request.body.decode("utf-8")) if request.body.decode("utf-8") else {}
	return post_params

'''
	colored print in terminal
	str_to_print = The string that you want to print
	fg = color of the text (optional) (default to red)
	bg = background color of the text (optional) (default to white)
'''
def cprint(str_to_print, fg = "white", bg = "blue"):
	print(colorize(str_to_print, fg=fg, bg=bg))

def eprint(string, fg="white", bg="blue"):
	print ("======================================")
	print (colorize(string, fg=fg, bg=bg))
	print ("======================================")

def dprint(string):
	print ("======================================")
	print (string)
	print ("======================================")

'''
	Gets the current date and return depends on what format you want to return
'''

def current_date(to_return = None):
	if to_return == 'month':
		return datetime.today().month
	elif to_return == 'year':
		return datetime.today().year
	elif to_return == 'day':
		return datetime.today().day
	else:
		return datetime.today().date()


	
'''
	just call this function for testing stopper
	instead of calling raise ValueError('test'), just use raise_error() function
'''
def raise_error(msg = "Testing Stopper"):
	raise ValueError(msg)

def success_list(listt):
	listt = listt if listt else []
	return HttpResponse(json_encode(listt), status = 200)

def success_obj(listt):
	listt = listt if listt else {}
	return HttpResponse(json_encode(listt), status = 200)

def success(to_return = "Successfully saved."):
	return HttpResponse(to_return, status = 200)

def json_encode(listt):
	return json.dumps(list(listt))