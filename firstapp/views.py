# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,render_to_response
from .models import firstmodel

# Create your views here.
def add_field(request):
    obj = firstmodel.objects.create(text_field='SECOND ENTRY')
    obj.save()
    return render_to_response('add_html.html')

def get_field(request):
    # obj = firstmodel.objects.filter(text_field='SECOND ENTRY').values_list()
    # val_list = []
    # for i in obj:
    #     val_list.append(i[0])
    #     print(i)
    # val = obj[0][0]
    # dict_val={}
    # dict_val['val_key']= val
    # dict_val['val_list_key']= val_list
    return render_to_response('get_html.html')

def update_field(request):
    obj = firstmodel.objects.get(id=2)
    print(obj.id)
    obj.text_field = 'value_updated'
    print(obj.text_field)
    obj.save()
    print(obj.text_field)
    val = obj.text_field
    dict_val={}
    dict_val['val_key']=val
    return render_to_response('update_html.html', dict_val)

def delete_field(request):
    obj = firstmodel.objects.get(id=3)
    print(obj.id)
    obj.delete()
    return render_to_response('delete_html.html')