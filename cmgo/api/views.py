import datetime
import facebook
import requests
from json import dumps
from urllib import parse
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from django.views.generic import TemplateView
from django.http import HttpResponse
# from rest_framework.generics import ListAPIView
# from django.db.models import Count

from . import serializers, models
PLACEHOLDER_IMG = "http://placehold.it/300x300"
EXTENDED_TOKEN_FACEBOOK = "EAAGAhk69Nm8BAMThqoV8sjGdeNs4ALgjGzdmpQaLin1g88VRZAb2CsXVTSmo6mnZBZAmNQvU2OxYdoqkiNvuYR4mDsOlEEsR0EdbtsWmEoXj2Y3nmbwidFukao4xY7ZCoLqT9drbZAHGg8GW4ZBfKvTEqACVlwoS7eY5EDsPHIV557aQOGBkGitJes3nvU9y4ZD"


class SlideViewSet(ModelViewSet):
    queryset = models.Slide.objects.all()
    serializer_class = serializers.SlideSerializer


class Social(TemplateView):
    template_name = 'social.html'

    def get_context_data(self, **kwargs):
        context = super(Social, self).get_context_data(**kwargs)
        fb = feed_facebook(10)
        # tw = feed_twitter(10)
        # fi = feed_instragram(10)
        lists = list(fb)  # + list(tw) + list(fi)
        feeds = sorted(lists, key=lambda k: k['created_time'], reverse=True)
        context["posts"] = feeds
        return context


def feed_facebook(count):
    graph = facebook.GraphAPI(EXTENDED_TOKEN_FACEBOOK)
    profile = graph.get_object("ConsejoGinecologia")
    posts = graph.get_connections(profile['id'], 'posts')
    max_pages = 1
    paging = 0
    comments = []
    counter = 0

    for post in posts['data']:
        if counter <= count:
            try:
                c = {}
                c['id'] = post["id"]
                date = datetime.datetime.strptime(post["created_time"], '%Y-%m-%dT%H:%M:%S+0000')
                c["created_time"] = date
                c["message"] = post["message"]
                c['text_encoded'] = post["message"]
                c["type"] = "facebook"
                c["image"] = PLACEHOLDER_IMG
                c['link'] = ""
                c['link_encoded'] = ""
            except Exception as e:
                print(str(e))
            else:
                counter += 1
                comments.append(c)
        print(post)
    return comments


def get_picture_facebook(request):
    data = 'fail'
    if request.is_ajax():
        post_id = request.POST.get('post_id', 0)
        print(post_id)
        url = "https://graph.facebook.com/v3.1/" + post_id + "?fields=full_picture,permalink_url&access_token=" + EXTENDED_TOKEN_FACEBOOK
        r = requests.get(url)
        r_json = r.json()
        full_picture = ''
        link = ''
        if 'full_picture' in r_json:
            full_picture = r_json["full_picture"]
        if 'permalink_url' in r_json:
            link = str(r_json["permalink_url"])

        data = {"id": post_id, "picture": full_picture, "link": link}
        print(data)
    return HttpResponse(dumps(data), 'application/json')
