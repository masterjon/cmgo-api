import datetime
import facebook
import requests
from json import dumps
from urllib import parse
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from django.views.generic import TemplateView
from django.http import HttpResponse, JsonResponse
from django.conf import settings
from tweepy import OAuthHandler
from tweepy import API
# from rest_framework.generics import ListAPIView
# from django.db.models import Count

from . import serializers, models
PLACEHOLDER_IMG = "http://placehold.it/300x300"

CONST_USER_FACEBOOK = settings.CONST_USER_FACEBOOK
EXTENDED_TOKEN_FACEBOOK = settings.EXTENDED_TOKEN_FACEBOOK

CONST_USER_TWITTER = settings.CONST_USER_TWITTER
CONSUMER_KEY_TWITTER = settings.CONSUMER_KEY_TWITTER
CONSUMER_SECRET_TWITTER = settings.CONSUMER_SECRET_TWITTER
ACCESS_TOKEN_TWITTER = settings.ACCESS_TOKEN_TWITTER
ACCESS_TOKEN_SECRET_TWITTER = settings.ACCESS_TOKEN_SECRET_TWITTER


class SlideViewSet(ModelViewSet):
    queryset = models.Slide.objects.all()
    serializer_class = serializers.SlideSerializer


class Social(TemplateView):
    template_name = 'social.html'

    def get_context_data(self, **kwargs):
        context = super(Social, self).get_context_data(**kwargs)
        fb = feed_facebook(10)
        tw = feed_twitter(16)
        print(tw)
        # fi = feed_instragram(10)
        lists = list(fb) + list(tw)  # + list(fi)
        feeds = sorted(lists, key=lambda k: k['created_time'], reverse=True)
        context["posts"] = feeds
        return context
# API_URL = "https://graph.facebook.com/v3.0"
# USER_TOKEN="EAAGAhk69Nm8BAP0VLcoZBDml9qcpGjJnzntY3BKoqQbTgUVZBS1fYZBmSpierMxgrDhwvpQatlaUK3hYgn7WXbyTcLCmRHu1jwFBpBt8xXXlQeZBZB8NMDhMZC9w6y6rfINFAikMZAZCl3DWcUu2KSONdoYKs5WJeZAIc6vYKfG05Ki0twnTo6N9M3kqsq2diRYyqZCbb9WxJpFAZDZD"
# response = requests .get("{}/oauth/access_token?grant_type=fb_exchange_token&client_id={}&client_secret={}&fb_exchange_token=#{}").format(API_URL,"422789311706735","5a3eeec7c2a89adab4e2b14c4e093132",USER_TOKEN)
# UU= "{}/oauth/access_token?grant_type=fb_exchange_token&client_id={}&client_secret=#{}&fb_exchange_token=#{}".format(API_URL,"422789311706735","5a3eeec7c2a89adab4e2b14c4e093132",USER_TOKEN)


def feed_facebook(count):
    graph = facebook.GraphAPI(EXTENDED_TOKEN_FACEBOOK)
    profile = graph.get_object(CONST_USER_FACEBOOK)
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
        
    return comments


def feed_twitter(count):
    auth = OAuthHandler(CONSUMER_KEY_TWITTER, CONSUMER_SECRET_TWITTER)
    auth.set_access_token(ACCESS_TOKEN_TWITTER, ACCESS_TOKEN_SECRET_TWITTER)
    api = API(auth)
    feed = api.user_timeline(screen_name=CONST_USER_TWITTER, count=count, page=1, include_rts=True, tweet_mode="extended")
    tweets = []
    for i, t in enumerate(feed):
        if t.in_reply_to_status_id is None:
            
            try:
                tweet = {
                    "text": t.full_text,
                    "text_encoded": t.full_text,
                    "type": "tweet",
                    "created_time": t.created_at,
                    "link": "https://twitter.com/" + CONST_USER_TWITTER + "/status/" + str(t.id),
                    "link_encoded": parse.quote_plus("https://twitter.com/" + CONST_USER_TWITTER + "/status/" + str(t.id)),
                    "user": {"name": t.user.name, "screen_name": t.user.screen_name, "profile_image": t.user.profile_image_url}
                }
                print("-------------------------------------\n\n")
               
                print(t.id)
                print(t.full_text)
                if "media" in t.entities:
                    if t.entities['media'][0]['type'] == 'photo':
                        print(t.entities['media'][0]['media_url_https'])
                        tweet["image"] = t.entities['media'][0]['media_url_https']
                    else:
                        pass
                tweets.append(tweet)

            except Exception as e:
                pass
    
    return tweets


def get_picture_facebook(request):
    data = 'fail'
    if request.is_ajax():
        post_id = request.POST.get('post_id', 0)
        
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
        
    return HttpResponse(dumps(data), 'application/json')




def facebook_callback(request):
    code = request.GET.get('code')
    APP_ID = '422789311706735'
    APP_SECRET = '5a3eeec7c2a89adab4e2b14c4e093132'

    if not code:
        return JsonResponse({'error': 'No code provided'}, status=400)

    # Paso 1: Intercambiar el code por un short-lived token
    token_url = 'https://graph.facebook.com/v12.0/oauth/access_token'
    params = {
        'client_id': APP_ID,
        'redirect_uri': 'http://localhost:8000/facebook/callback/',  # debe coincidir con el registrado
        'client_secret': APP_SECRET,
        'code': code,
    }

    r = requests.get(token_url, params=params)
    data = r.json()

    if 'access_token' not in data:
        return JsonResponse({'error': 'No access token in response', 'response': data}, status=400)

    short_lived_token = data['access_token']

    # Paso 2: Intercambiarlo por un long-lived token
    extend_url = 'https://graph.facebook.com/v12.0/oauth/access_token'
    params = {
        'grant_type': 'fb_exchange_token',
        'client_id': APP_ID,
        'client_secret': APP_SECRET,
        'fb_exchange_token': short_lived_token,
    }

    r = requests.get(extend_url, params=params)
    extended_data = r.json()

    return JsonResponse(extended_data)