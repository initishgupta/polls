# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.template import Context, loader
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.shortcuts import render





def index(request):
    template = loader.get_template("index.html")
    return HttpResponse(template.render())
    #return render_to_response('index.html', locals())



def leftSidebar(request):
    #dataSet = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}


    title1 = """Clinton Calls On Star Power While Trump Goes It Alone",
      "abstract": "With four days to go until the election, Hillary Clinton campaigned with a shifting crowd of friends, supporters, family and celebrities.  By contrast, Mr. Trump, abandoned by his party’s biggest names, has become a lonely figure before adoring crowds.'"""
    url = 'http://www.nytimes.com/2016/11/05/us/politics/campaign-trump-clinton.html'
    title_with_url = "<a href=" + url + ">" + title1 + "</a>"

    dataSet = [title_with_url]


    news = ['News 1', 'News 2']
    #template = loader.get_template("left-sidebar.html")
    #return HttpResponse(template.render())
    #return render_to_response('left-sidebar.html', locals())
    #return render(request, 'left-sidebar.html', context)
    return render(request,'left-sidebar.html', {"restaurants": dataSet})

def rightSidebar(request):
        #template = loader.get_template("left-sidebar.html")
        #return HttpResponse(template.render())
        return render_to_response('right-sidebar.html', locals())
