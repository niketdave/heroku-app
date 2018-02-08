from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from django.http import HttpResponse
from instagram import subscriptions
import json
# Create your views here.
@csrf_exempt
def process_tag_update(update):
    print ('Received a push: ', update)
reactor = subscriptions.SubscriptionsReactor()
reactor.register_callback(subscriptions.SubscriptionType.TAG, process_tag_update)

@csrf_exempt
def InstagramWebHookView(request):
    # GET method is used when validating the endpoint as per the Pubsubhubub protocol
    if request.method == 'GET':
        mode = request.GET.get('hub.mode')
        challenge = request.GET.get('hub.challenge')
        verify_token = request.GET.get('hub.verify_token')
        if challenge:
            return HttpResponse(challenge)
    # POST event is used to for the events notifications
    else:
        x_hub_signature = request.META.get('HTTP_X_HUB_SIGNATURE', '')
        raw_response = request.body
        try:
            reactor.process(settings.INSTAGRAM_CLIENT_SECRET, raw_response, x_hub_signature)
        except subscriptions.SubscriptionVerifyError:
            print ('Signature mismatch')
    return HttpResponse('gvhbkjnk')
