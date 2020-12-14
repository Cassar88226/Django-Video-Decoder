import json
import requests
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse


# Create your views here.

from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login, logout
from .forms import SignupForm

# log in function
def log_in(request):
    _email = request.GET.get('_email', '')
    _pwd = request.GET.get('_pwd')
    user = authenticate(username=_email, password = _pwd)
    if user is not None: 
        login(request, user) 
        data = {
            'content' :'ok' 
        }
        
    else: 
        data = {
            'content' : 'unregistered'
        }
    return JsonResponse(data)
# log out function
def log_out(request):
    logout(request)
    return JsonResponse({'content':'ok'})

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})
class GetDroplets(TemplateView):
    template_name = 'droplets.html'
    def get_context_data(self):
        url = 'https://c43w8otvfe.execute-api.us-west-1.amazonaws.com/test/videodata'
        # r = requests.get(url)
        r = {"statusCode": 200, "headers": {"Content-Type": "application/json"}, "body": "{\"video_id\": \"VvvGy0QuLxc\", \"publishedAt\": \"2020-10-31T05:13:51Z\", \"search_kind\": \"youtube#searchResult\", \"search_etag\": \"bEfLw_otcEZRZhCAe3lW2_kIF9g\", \"video_kind\": \"youtube#video\", \"video_title\": \"\\u0c1c\\u0c17\\u0c28\\u0c4d \\u0c30\\u0c46\\u0c21\\u0c4d\\u0c21\\u0c3f \\u0c17\\u0c3e\\u0c30\\u0c3f \\u0c05\\u0c2a\\u0c4d\\u0c2a\\u0c41\\u0c32 \\u0c2a\\u0c4d\\u0c30\\u0c4b\\u0c17\\u0c4d\\u0c30\\u0c46\\u0c38\\u0c4d \\u0c15\\u0c3e\\u0c30\\u0c4d\\u0c21\\u0c41 \\u0c1a\\u0c41\\u0c38\\u0c4d\\u0c24\\u0c47 \\u0c37\\u0c3e\\u0c15\\u0c4d \\u0c05\\u0c35\\u0c4d\\u0c35\\u0c3e\\u0c32\\u0c4d\\u0c38\\u0c3f\\u0c02\\u0c26\\u0c47 - Pattabhi Ram Kommareddi | TDP |\", \"description\": \"\\u0c1c\\u0c17\\u0c28\\u0c4d \\u0c30\\u0c46\\u0c21\\u0c4d\\u0c21\\u0c3f \\u0c17\\u0c3e\\u0c30\\u0c3f \\u0c05\\u0c2a\\u0c4d\\u0c2a\\u0c41\\u0c32 \\u0c2a\\u0c4d\\u0c30\\u0c4b\\u0c17\\u0c4d\\u0c30\\u0c46\\u0c38\\u0c4d \\u0c15\\u0c3e\\u0c30\\u0c4d\\u0c21\\u0c41 \\u0c1a\\u0c41\\u0c38\\u0c4d\\u0c24\\u0c47 \\u0c37\\u0c3e\\u0c15\\u0c4d \\u0c05\\u0c35\\u0c4d\\u0c35\\u0c3e\\u0c32\\u0c4d\\u0c38\\u0c3f\\u0c02\\u0c26\\u0c47 - Pattabhi Ram Kommareddi | TDP | #TelugudesamOfficial ...\", \"channel_title\": \"Telugu Desam Party Official\", \"channel_id\": \"UCvMZV13-yh2sUQY2s0Y5hlg\", \"image_default_url\": \"https://i.ytimg.com/vi/VvvGy0QuLxc/default.jpg\", \"image_default_width\": \"120\", \"image_default_height\": \"90\", \"image_medium\": \"https://i.ytimg.com/vi/VvvGy0QuLxc/mqdefault.jpg\", \"image_medium_width\": \"320\", \"image_medium_height\": \"180\", \"image_high\": \"https://i.ytimg.com/vi/VvvGy0QuLxc/hqdefault.jpg\", \"image_high_width\": \"480\", \"image_high_height\": \"360\", \"tags\": [\"TelugudesamOfficial ...\"], \"video_url\": \"https://www.youtube.com/watch?v=VvvGy0QuLxc\", \"liveBroadcastContent\": \"none\", \"validity_status\": \"1\", \"eng_text\": \" A total of 11 thousand coats in the alone in a single year Jagan Mohan Reddy has been borrowed once in the Five Years of 2014 to 2014 since 2014 to 2014, but this Mahanati Telangana state with neighbors 26650 How much 27022 55127 31500 12 crore 31500 Tamil Nadu Karnataka 16 thousand 78 crores Kerala 23577 Although the influence of the coronary effect in all states 16,000 Karnataka Tamil Nadu 71000 Telangana Twenty-two twenty-e-eight finger, if you compared to the 55149 crores with the rest of the states, if you have two states in Tamil Nadu Telangana, the two states have been combined with the two states, but Andhra Pradesh The only 56 thousand coats have been charged in the two states of the bus, the thirteen districts of the thirteen districts that are in Andhra Pradesh in Andhra Pradesh Asking that every answer in the state is asking that the website is the first six months of 49 thousand 472 President state division of 16 thousand crores during the 2014 state Chief Minister Chandrababu's state will rule the state of 12 2019 that the financial deficit of our tenure will reduce approximately two thousand sixteen finger As the financial deficit has been reduced to the financial deficit of this financial deficit 45 thousand hundreds of four hundred The number of numbers in the state is more than all the states from all the states from all the states, even the number of people in the state to know the state and destroying the state in any way that the state is destroyed by the chief minister people understand and strongly understand the government\", \"telugu_text\": \" \\u0c05\\u0c15\\u0c4d\\u0c37\\u0c30\\u0c3e\\u0c32 \\u0c32\\u0c15\\u0c4d\\u0c37\\u0c3e 11 \\u0c35\\u0c47\\u0c32 \\u0c15\\u0c4b\\u0c1f\\u0c4d\\u0c32\\u0c41 \\u0c12\\u0c15\\u0c4d\\u0c15 \\u0c38\\u0c02\\u0c35\\u0c24\\u0c4d\\u0c38\\u0c30\\u0c02 \\u0c32\\u0c4b \\u0c1c\\u0c17\\u0c28\\u0c4d \\u0c2e\\u0c4b\\u0c39\\u0c28\\u0c4d \\u0c30\\u0c46\\u0c21\\u0c4d\\u0c21\\u0c3f \\u0c17\\u0c3e\\u0c30\\u0c41 \\u0c12\\u0c15\\u0c38\\u0c3e\\u0c30\\u0c3f \\u0c17\\u0c41\\u0c30\\u0c4d\\u0c24\\u0c41 \\u0c1a\\u0c47\\u0c38\\u0c41\\u0c15\\u0c41\\u0c02\\u0c1f\\u0c47 \\u0c10\\u0c26\\u0c41 \\u0c38\\u0c02\\u0c35\\u0c24\\u0c4d\\u0c38\\u0c30\\u0c3e\\u0c32 \\u0c24\\u0c46\\u0c32\\u0c41\\u0c17\\u0c41\\u0c26\\u0c47\\u0c36\\u0c02 \\u0c2a\\u0c3e\\u0c30\\u0c4d\\u0c1f\\u0c40 \\u0c2a\\u0c30\\u0c3f\\u0c2a\\u0c3e\\u0c32\\u0c28 \\u0c32\\u0c4b 2014 \\u0c28\\u0c41\\u0c02\\u0c1a\\u0c3f 2019 \\u0c35\\u0c30\\u0c15\\u0c41 \\u0c10\\u0c26\\u0c41 \\u0c38\\u0c02\\u0c35\\u0c24\\u0c4d\\u0c38\\u0c30\\u0c3e\\u0c32 \\u0c15\\u0c3e\\u0c32\\u0c3e\\u0c28\\u0c3f\\u0c15\\u0c3f \\u0c38\\u0c41\\u0c2e\\u0c3e\\u0c30\\u0c41\\u0c17\\u0c3e 25 \\u0c38\\u0c02\\u0c35\\u0c24\\u0c4d\\u0c38\\u0c30\\u0c3e\\u0c32\\u0c41 \\u0c2e\\u0c3e\\u0c24\\u0c4d\\u0c30\\u0c2e\\u0c47 \\u0c05\\u0c2a\\u0c4d\\u0c2a\\u0c41 \\u0c1a\\u0c47\\u0c2f\\u0c21\\u0c02 \\u0c1c\\u0c30\\u0c3f\\u0c17\\u0c3f\\u0c02\\u0c26\\u0c3f \\u0c15\\u0c3e\\u0c28\\u0c40 \\u0c08 \\u0c2e\\u0c39\\u0c3e\\u0c28\\u0c1f\\u0c3f \\u0c2a\\u0c4a\\u0c30\\u0c41\\u0c17\\u0c41 \\u0c09\\u0c28\\u0c4d\\u0c28\\u0c1f\\u0c41\\u0c35\\u0c02\\u0c1f\\u0c3f \\u0c24\\u0c46\\u0c32\\u0c02\\u0c17\\u0c3e\\u0c23 \\u0c30\\u0c3e\\u0c37\\u0c4d\\u0c1f\\u0c4d\\u0c30\\u0c02 \\u0c1a\\u0c47\\u0c38\\u0c3f\\u0c28\\u0c1f\\u0c41\\u0c35\\u0c02\\u0c1f\\u0c3f \\u0c2e\\u0c4a\\u0c24\\u0c4d\\u0c24\\u0c02 \\u0c05\\u0c2a\\u0c4d\\u0c2a\\u0c41 26650 \\u0c0e\\u0c02\\u0c24 27022 55127 31500 12 \\u0c15\\u0c4b\\u0c1f\\u0c4d\\u0c32\\u0c41 31500 \\u0c24\\u0c2e\\u0c3f\\u0c33\\u0c28\\u0c3e\\u0c21\\u0c41 \\u0c15\\u0c30\\u0c4d\\u0c23\\u0c3e\\u0c1f\\u0c15 16 \\u0c35\\u0c47\\u0c32 78 \\u0c15\\u0c4b\\u0c1f\\u0c4d\\u0c32\\u0c41 \\u0c15\\u0c47\\u0c30\\u0c33 23577 \\u0c05\\u0c28\\u0c4d\\u0c28\\u0c3f \\u0c30\\u0c3e\\u0c37\\u0c4d\\u0c1f\\u0c4d\\u0c30\\u0c3e\\u0c32\\u0c4d\\u0c32\\u0c4b \\u0c15\\u0c30\\u0c4b\\u0c28\\u0c3e \\u0c2a\\u0c4d\\u0c30\\u0c2d\\u0c3e\\u0c35\\u0c02 \\u0c24\\u0c40\\u0c35\\u0c4d\\u0c30\\u0c02\\u0c17\\u0c3e \\u0c09\\u0c28\\u0c4d\\u0c28\\u0c2a\\u0c4d\\u0c2a\\u0c1f\\u0c3f\\u0c15\\u0c40 \\u0c35\\u0c3f\\u0c32\\u0c35\\u0c3f\\u0c32\\u0c3e \\u0c35\\u0c3f\\u0c1a\\u0c4d\\u0c1a\\u0c32\\u0c35\\u0c3f\\u0c21\\u0c3f\\u0c17\\u0c3e \\u0c05\\u0c2a\\u0c4d\\u0c2a\\u0c41\\u0c32\\u0c41 \\u0c1a\\u0c47\\u0c2f\\u0c32\\u0c47\\u0c26\\u0c41 16,000 \\u0c15\\u0c30\\u0c4d\\u0c23\\u0c3e\\u0c1f\\u0c15 \\u0c24\\u0c2e\\u0c3f\\u0c33\\u0c28\\u0c3e\\u0c21\\u0c41 71000 \\u0c24\\u0c46\\u0c32\\u0c02\\u0c17\\u0c3e\\u0c23 \\u0c07\\u0c30\\u0c35\\u0c48 \\u0c30\\u0c46\\u0c02\\u0c21\\u0c41 \\u0c07\\u0c30\\u0c35\\u0c48 \\u0c0e\\u0c28\\u0c3f\\u0c2e\\u0c3f\\u0c26\\u0c3f \\u0c35\\u0c47\\u0c32\\u0c41 \\u0c2e\\u0c40\\u0c30\\u0c41 \\u0c2e\\u0c3e\\u0c24\\u0c4d\\u0c30\\u0c02 55149 \\u0c15\\u0c4b\\u0c1f\\u0c4d\\u0c32\\u0c41 \\u0c2e\\u0c3f\\u0c17\\u0c24\\u0c3e \\u0c30\\u0c3e\\u0c37\\u0c4d\\u0c1f\\u0c4d\\u0c30\\u0c3e\\u0c32\\u0c24\\u0c4b \\u0c2a\\u0c4b\\u0c32\\u0c3f\\u0c38\\u0c4d\\u0c24\\u0c47 \\u0c26\\u0c3e\\u0c26\\u0c3e\\u0c2a\\u0c41 \\u0c17\\u0c3e \\u0c2e\\u0c40\\u0c30\\u0c41 \\u0c30\\u0c46\\u0c02\\u0c21\\u0c3f\\u0c02\\u0c24\\u0c32\\u0c41 \\u0c05\\u0c2a\\u0c4d\\u0c2a\\u0c41 \\u0c1a\\u0c47\\u0c38\\u0c3f\\u0c28\\u0c1f\\u0c41\\u0c35\\u0c02\\u0c1f\\u0c3f \\u0c2a\\u0c30\\u0c3f\\u0c38\\u0c4d\\u0c25\\u0c3f\\u0c24\\u0c3f \\u0c24\\u0c2e\\u0c3f\\u0c33\\u0c28\\u0c3e\\u0c21\\u0c41 \\u0c24\\u0c46\\u0c32\\u0c02\\u0c17\\u0c3e\\u0c23 \\u0c30\\u0c46\\u0c02\\u0c21\\u0c41 \\u0c30\\u0c3e\\u0c37\\u0c4d\\u0c1f\\u0c4d\\u0c30\\u0c3e\\u0c32\\u0c41 \\u0c15\\u0c32\\u0c3f\\u0c17\\u0c3f\\u0c24\\u0c47 \\u0c08 \\u0c30\\u0c46\\u0c02\\u0c21\\u0c41 \\u0c30\\u0c3e\\u0c37\\u0c4d\\u0c1f\\u0c4d\\u0c30\\u0c3e\\u0c32\\u0c15\\u0c41 \\u0c15\\u0c32\\u0c3f\\u0c2a\\u0c3f \\u0c1a\\u0c47\\u0c38\\u0c3f\\u0c28 \\u0c24\\u0c2a\\u0c4d\\u0c2a\\u0c41 57 \\u0c35\\u0c47\\u0c32 \\u0c15\\u0c4b\\u0c1f\\u0c4d\\u0c32\\u0c41 \\u0c15\\u0c3e\\u0c28\\u0c40 \\u0c06\\u0c02\\u0c27\\u0c4d\\u0c30\\u0c2a\\u0c4d\\u0c30\\u0c26\\u0c47\\u0c36\\u0c4d \\u0c12\\u0c15\\u0c4d\\u0c15\\u0c1f\\u0c47 \\u0c26\\u0c3e\\u0c26\\u0c3e\\u0c2a\\u0c41 56 \\u0c35\\u0c47\\u0c32 \\u0c15\\u0c4b\\u0c1f\\u0c4d\\u0c32\\u0c41 \\u0c35\\u0c38\\u0c42\\u0c32\\u0c41 \\u0c1a\\u0c47\\u0c38\\u0c3f\\u0c28\\u0c1f\\u0c4d\\u0c32\\u0c41 \\u0c2c\\u0c38\\u0c4d\\u0c38\\u0c41 \\u0c30\\u0c46\\u0c02\\u0c21\\u0c41 \\u0c30\\u0c3e\\u0c37\\u0c4d\\u0c1f\\u0c4d\\u0c30\\u0c3e\\u0c32\\u0c4d\\u0c32\\u0c4b \\u0c1a\\u0c47\\u0c38\\u0c3f\\u0c28 \\u0c24\\u0c2a\\u0c4d\\u0c2a\\u0c41 \\u0c2e\\u0c40 \\u0c05\\u0c15\\u0c4d\\u0c15\\u0c15\\u0c3f \\u0c06\\u0c02\\u0c27\\u0c4d\\u0c30\\u0c2a\\u0c4d\\u0c30\\u0c26\\u0c47\\u0c36\\u0c4d\\u0c32\\u0c4b \\u0c09\\u0c28\\u0c4d\\u0c28\\u0c1f\\u0c41\\u0c35\\u0c02\\u0c1f\\u0c3f \\u0c2a\\u0c26\\u0c2e\\u0c42\\u0c21\\u0c41 \\u0c1c\\u0c3f\\u0c32\\u0c4d\\u0c32\\u0c3e\\u0c32 \\u0c06\\u0c02\\u0c27\\u0c4d\\u0c30 \\u0c2a\\u0c4d\\u0c30\\u0c26\\u0c47\\u0c36\\u0c4d \\u0c30\\u0c3e\\u0c37\\u0c4d\\u0c1f\\u0c4d\\u0c30\\u0c02\\u0c32\\u0c4b \\u0c09\\u0c28\\u0c4d\\u0c28\\u0c1f\\u0c41\\u0c35\\u0c02\\u0c1f\\u0c3f \\u0c2a\\u0c4d\\u0c30\\u0c24\\u0c3f \\u0c38\\u0c2e\\u0c3e\\u0c27\\u0c3e\\u0c28\\u0c02 \\u0c1a\\u0c46\\u0c2c\\u0c41\\u0c24\\u0c3e \\u0c05\\u0c28\\u0c3f \\u0c05\\u0c21\\u0c41\\u0c17\\u0c41\\u0c24\\u0c4b\\u0c02\\u0c26\\u0c3f \\u0c35\\u0c46\\u0c2c\\u0c4d\\u0c38\\u0c48\\u0c1f\\u0c4d \\u0c2e\\u0c4a\\u0c26\\u0c1f\\u0c3f \\u0c06\\u0c30\\u0c41 \\u0c28\\u0c46\\u0c32\\u0c32 \\u0c15\\u0c3e\\u0c32\\u0c3e\\u0c28\\u0c3f\\u0c15\\u0c3f \\u0c28\\u0c32\\u0c2d\\u0c48 \\u0c10\\u0c26\\u0c41 \\u0c05\\u0c15\\u0c4d\\u0c37\\u0c30\\u0c3e\\u0c32 49\\u0c35\\u0c47\\u0c32 472 \\u0c2a\\u0c4d\\u0c30\\u0c46\\u0c38\\u0c3f\\u0c21\\u0c46\\u0c02\\u0c1f\\u0c4d \\u0c30\\u0c3e\\u0c37\\u0c4d\\u0c1f\\u0c4d\\u0c30 \\u0c35\\u0c3f\\u0c2d\\u0c1c\\u0c28 \\u0c38\\u0c2e\\u0c2f\\u0c02\\u0c32\\u0c4b 16 \\u0c35\\u0c47\\u0c32 \\u0c15\\u0c4b\\u0c1f\\u0c4d\\u0c32 \\u0c30\\u0c3e\\u0c37\\u0c4d\\u0c1f\\u0c4d\\u0c30 \\u0c06\\u0c30\\u0c4d\\u0c25\\u0c3f\\u0c15 2014 \\u0c30\\u0c3e\\u0c37\\u0c4d\\u0c1f\\u0c4d\\u0c30 \\u0c2e\\u0c41\\u0c16\\u0c4d\\u0c2f\\u0c2e\\u0c02\\u0c24\\u0c4d\\u0c30\\u0c3f \\u0c1a\\u0c02\\u0c26\\u0c4d\\u0c30\\u0c2c\\u0c3e\\u0c2c\\u0c41 \\u0c30\\u0c3e\\u0c37\\u0c4d\\u0c1f\\u0c4d\\u0c30\\u0c3e\\u0c28\\u0c4d\\u0c28\\u0c3f \\u0c2a\\u0c30\\u0c3f\\u0c2a\\u0c3e\\u0c32\\u0c3f\\u0c02\\u0c1a\\u0c47 12 2019 \\u0c2e\\u0c3e \\u0c2a\\u0c26\\u0c35\\u0c40\\u0c15\\u0c3e\\u0c32\\u0c02 \\u0c2a\\u0c42\\u0c30\\u0c4d\\u0c24\\u0c3f \\u0c38\\u0c2e\\u0c2f\\u0c3e\\u0c28\\u0c3f\\u0c15\\u0c3f \\u0c06\\u0c30\\u0c4d\\u0c25\\u0c3f\\u0c15 \\u0c32\\u0c4b\\u0c1f\\u0c41 \\u0c26\\u0c3e\\u0c26\\u0c3e\\u0c2a\\u0c41 \\u0c30\\u0c46\\u0c02\\u0c21\\u0c41 \\u0c35\\u0c47\\u0c32 \\u0c2a\\u0c26\\u0c39\\u0c3e\\u0c30\\u0c41 \\u0c35\\u0c47\\u0c32\\u0c41 \\u0c09\\u0c28\\u0c4d\\u0c28\\u0c26\\u0c3e\\u0c28\\u0c4d\\u0c28\\u0c3f \\u0c38\\u0c41\\u0c2e\\u0c3e\\u0c30\\u0c41 14,000 \\u0c24\\u0c17\\u0c4d\\u0c17\\u0c3f\\u0c02\\u0c1a\\u0c17\\u0c32\\u0c35\\u0c41 \\u0c06 \\u0c35\\u0c3f\\u0c27\\u0c02\\u0c17\\u0c3e \\u0c06\\u0c30\\u0c4d\\u0c25\\u0c3f\\u0c15 \\u0c32\\u0c4b\\u0c1f\\u0c41 \\u0c24\\u0c17\\u0c4d\\u0c17\\u0c3f\\u0c38\\u0c4d\\u0c24\\u0c47 \\u0c1c\\u0c30\\u0c3f\\u0c17\\u0c3f\\u0c02\\u0c26\\u0c3f \\u0c08 \\u0c2f\\u0c4a\\u0c15\\u0c4d\\u0c15 \\u0c06\\u0c30\\u0c4d\\u0c25\\u0c3f\\u0c15 \\u0c38\\u0c02\\u0c35\\u0c24\\u0c4d\\u0c38\\u0c30\\u0c02\\u0c32\\u0c4b\\u0c28\\u0c47 \\u0c06\\u0c30\\u0c4d\\u0c25\\u0c3f\\u0c15 \\u0c32\\u0c4b\\u0c1f\\u0c41 45 \\u0c35\\u0c47\\u0c32 \\u0c28\\u0c3e\\u0c32\\u0c41\\u0c17\\u0c41 \\u0c35\\u0c02\\u0c26\\u0c32\\u0c41 \\u0c08 \\u0c2a\\u0c30\\u0c3f\\u0c38\\u0c4d\\u0c25\\u0c3f\\u0c24\\u0c3f \\u0c28\\u0c41\\u0c02\\u0c1a\\u0c3f \\u0c05\\u0c28\\u0c4d\\u0c28\\u0c3f \\u0c30\\u0c3e\\u0c37\\u0c4d\\u0c1f\\u0c4d\\u0c30\\u0c3e\\u0c32 \\u0c15\\u0c02\\u0c1f\\u0c47 \\u0c0e\\u0c15\\u0c4d\\u0c15\\u0c41\\u0c35\\u0c17\\u0c3e \\u0c2e\\u0c28\\u0c02 \\u0c1a\\u0c47\\u0c38\\u0c47 \\u0c09\\u0c26\\u0c4d\\u0c26\\u0c47\\u0c36\\u0c02 \\u0c32\\u0c47\\u0c26\\u0c3e \\u0c24\\u0c2a\\u0c4d\\u0c2a\\u0c41\\u0c32\\u0c41 \\u0c1a\\u0c47\\u0c38\\u0c3f\\u0c28\\u0c2a\\u0c41\\u0c21\\u0c41 \\u0c30\\u0c3e\\u0c37\\u0c4d\\u0c1f\\u0c4d\\u0c30\\u0c02\\u0c32\\u0c4b \\u0c28\\u0c46\\u0c02\\u0c2c\\u0c30\\u0c4d\\u0c35\\u0c28\\u0c4d \\u0c38\\u0c4d\\u0c25\\u0c3e\\u0c28\\u0c3e\\u0c28\\u0c4d\\u0c28\\u0c3f \\u0c15\\u0c42\\u0c21\\u0c3e \\u0c06\\u0c02\\u0c27\\u0c4d\\u0c30 \\u0c2a\\u0c4d\\u0c30\\u0c1c\\u0c32\\u0c41 \\u0c15\\u0c42\\u0c21\\u0c3e \\u0c2a\\u0c4d\\u0c30\\u0c1c\\u0c32\\u0c41 \\u0c24\\u0c46\\u0c32\\u0c41\\u0c38\\u0c41\\u0c15\\u0c4a\\u0c28\\u0c3f \\u0c0f \\u0c35\\u0c3f\\u0c27\\u0c02\\u0c17\\u0c3e \\u0c30\\u0c3e\\u0c37\\u0c4d\\u0c1f\\u0c4d\\u0c30\\u0c3e\\u0c28\\u0c4d\\u0c28\\u0c3f \\u0c28\\u0c3e\\u0c36\\u0c28\\u0c02 \\u0c1a\\u0c47\\u0c38\\u0c4d\\u0c24\\u0c41\\u0c28\\u0c4d\\u0c28\\u0c3e\\u0c21\\u0c41 \\u0c05\\u0c2a\\u0c4d\\u0c2a\\u0c41\\u0c32 \\u0c0a\\u0c2c\\u0c3f\\u0c32\\u0c4b\\u0c15\\u0c3f \\u0c15\\u0c42\\u0c30\\u0c4d\\u0c1a\\u0c4b\\u0c2c\\u0c46\\u0c1f\\u0c4d\\u0c1f\\u0c41\\u0c15\\u0c41\\u0c28\\u0c4d\\u0c28\\u0c3e\\u0c21\\u0c41 \\u0c2e\\u0c41\\u0c16\\u0c4d\\u0c2f\\u0c2e\\u0c02\\u0c24\\u0c4d\\u0c30\\u0c3f \\u0c2a\\u0c4d\\u0c30\\u0c1c\\u0c32\\u0c41 \\u0c05\\u0c02\\u0c26\\u0c30\\u0c42 \\u0c05\\u0c30\\u0c4d\\u0c25\\u0c02 \\u0c1a\\u0c47\\u0c38\\u0c41\\u0c15\\u0c41\\u0c28\\u0c3f \\u0c17\\u0c1f\\u0c4d\\u0c1f\\u0c3f\\u0c17\\u0c3e \\u0c2a\\u0c4d\\u0c30\\u0c2d\\u0c41\\u0c24\\u0c4d\\u0c35\\u0c3e\\u0c28\\u0c4d\\u0c28\\u0c3f \\u0c28\\u0c3f\\u0c32\\u0c26\\u0c40\\u0c2f\\u0c3e\\u0c32\\u0c28\\u0c3f \\u0c0e\\u0c15\\u0c4d\\u0c15\\u0c41\\u0c35\\u0c35\\u0c41\\u0c24\\u0c4b\\u0c02\\u0c26\\u0c3f\"}"}
        #print(r)
        droplets = r
        #print(droplets)
        context = {
            'droplets': json.loads(droplets['body']),
        }

        #print(context)
        return context

        #return render(r,'droplets.html',context)





def submit(request):
        video_id = request.POST.get('video_id')
        publishedAt = request.POST.get('publishedAt')
        search_kind = request.POST.get('search_kind')
        search_etag = request.POST.get('search_etag')
        video_kind = request.POST.get('video_kind')
        video_title = request.POST.get('video_title')
        description = request.POST.get('description')
        channel_title = request.POST.get('channel_title')
        channel_id = request.POST.get('channel_id')
        image_default_url = request.POST.get('image_default_url')
        image_default_width = request.POST.get('image_default_width')
        image_default_height = request.POST.get('image_default_height')
        image_medium = request.POST.get('image_medium')
        image_medium_width = request.POST.get('image_medium_width')
        image_medium_height = request.POST.get('image_medium_height')
        image_high = request.POST.get('image_high')
        image_high_width = request.POST.get('image_high_width')
        image_high_height = request.POST.get('image_high_height')
        tags = request.POST.get('tags')
        new_title = request.POST.get('new_title')
        video_url = request.POST.get('video_url')
        liveBroadcastContent = request.POST.get('liveBroadcastContent')
        validity_status = request.POST.get('validity_status')
        notes = request.POST.get('notes')
        topics = request.POST.get('topics')
        speakers = request.POST.get('speakers')
        questions = request.POST.get('questions')
        summary = request.POST.get('summary')
        video_intended = request.POST.getlist('video_intended[]')
        related_departments = request.POST.get('related_departments')
        party_status = request.POST.getlist('party_status[]')
        target_parties = request.POST.get('target_parties')
        topic_scope= request.POST.get('topic_scope')

        english_text = request.POST.get('english_text')
        telugu_text = request_POST.get('telugu_text')

        #Step1: Notes and Topics Section Validation

        total_notes_topics = notes.split('#')
        notes_topics_list = []
        if(len(total_notes_topics)>0):
            for i in range(1,len(total_notes_topics)):
                notes_topics_list.append(total_notes_topics[i].split(":")[0])
                # print(notes_topics_list)

        total_topics = topics.split("#")
        topics_topics_list = []
        if(len(total_topics)>0):
            for j in range(1,len(total_topics)):
                topics_topics_list.append(total_topics[j].split(".")[0])
                # print(topics_topics_list)

        if(len(notes_topics_list) == len(topics_topics_list)):
            print("Step1: Total topics mentioned in topics section and notes section match! - {}".format(len(topics_topics_list)))
        else:
            print("Step1: Total topics mentioned in notes section and topics section DO NOT match - {} & {}".format(len(notes_topics_list), len(topics_topics_list)))


        flag = 0
        for k in range(len(notes_topics_list)):
            for l in range(len(topics_topics_list)):
                if(notes_topics_list[k].upper()==topics_topics_list[l].upper()):
                    print("Step1: {} matched".format(notes_topics_list[k]))
                    flag +=1
                else:
                    pass

        if(flag == len(notes_topics_list) and flag == len(topics_topics_list)):
            print("Step1: total topics listed in topics section match with topics listed in notes section")

        else:
            print("Step1: total topics listed in topics section DOESN't match with topics listed in notes section. Check spelling/format.")


        #Step2: Validate the notes section. Check for the text if it has it/he/she/ here/there

        notes_text = notes.splitlines()
        print(notes_text)
        data = {}
        new_data = {}
        text = []
        key_flag = 0
        value_flag = 1
        key = ''
        for n in range(len(notes_text)):
            if('#' in notes_text[n]):
                if(n == 0):
                    key = notes_text[n]
                else:
                    data = {
                        key:text
                    }
                    new_data.update(data)
                    print(new_data)
                    key = notes_text[n]
                    text = []
                # print("Key: {}".format(key))
            else:
                if(value_flag==n):
                    text.append(notes_text[n])
                    value_flag +=1
                    # print("Value in else: {}".format(text))
                else:
                    text.append(notes_text[n])
                    value_flag == n+1
                    # print("Value in else-else: {}".format(text))
        data = {
            key: text
        }
        new_data.update(data)
        print("Step2: Notes data validation: {} ".format(new_data))





        #Step3: Speakers section should be atleast 1. Even automated if required.
        if(len(speakers)>0):
            speakers_covered = []

            speaker_list = speakers.split("#")

            for m in range(1,len(speaker_list)):

                speakers_covered.append(speaker_list[m])

            print("Step3: Speakers length is greater than 0. {}".format(speakers))



        # Step4: Questions section should be atleast 1. Even automated if required.

        if (len(questions) > 0):

            questions_covered = []

            question_list= questions.split('#')

            for m in range(1, len(question_list)):

                questions_covered.append(question_list[m])

            print("Step4: Questions length is greater than 0. {}".format(questions))





        questions_text = questions.splitlines()
        print(questions_text)
        data = {}
        questions_data = {}
        text = []
        key_flag = 0
        value_flag = 1
        key = ''
        for n in range(len(questions_text)):
            if ('#' in questions_text[n]):
                if (n == 0):
                    key = questions_text[n]
                else:
                    data = {
                        key: text
                    }
                    questions_data.update(data)
                    print(questions_data)
                    key = questions_text[n]
                    text = []
                # print("Key: {}".format(key))
            else:
                if (value_flag == n):
                    text.append(questions_text[n])
                    value_flag += 1
                    # print("Value in else: {}".format(text))
                else:
                    text.append(questions_text[n])
                    value_flag == n + 1
                    # print("Value in else-else: {}".format(text))
        data = {
            key: text
        }
        questions_data.update(data)
        print("Step2: Notes data validation: {} ".format(questions_data))









        # Step5: Summary section should be atleast 1. Even automated if required.

        if (len(summary) > 0):
            summary_covered = []
            summary_list= summary.split('#')
            for m in range(1, len(summary_list)):
                summary_covered.append(summary_list[m])
            print("Step5: Summary length is greater than 0. {}".format(summary))




        summary_text = summary.splitlines()
        print(summary_text)
        data = {}
        summary_data = {}
        text = []
        key_flag = 0
        value_flag = 1
        key = ''
        for n in range(len(summary_text)):
            if ('#' in summary_text[n]):
                if (n == 0):
                    key = summary_text[n]
                else:
                    data = {
                        key: text
                    }
                    summary_data.update(data)
                    print(summary_data)
                    key = summary_text[n]
                    text = []

                # print("Key: {}".format(key))
            else:
                if (value_flag == n):
                    text.append(summary_text[n])
                    value_flag += 1
                    # print("Value in else: {}".format(text))
                else:
                    text.append(summary_text[n])
                    value_flag == n + 1
                    # print("Value in else-else: {}".format(text))
        data = {
            key: text
        }
        summary_data.update(data)
        print("Step2: Notes data validation: {} ".format(summary_data))       









        # Step6: Video_Intended section should be atleast 1.
        if (len(video_intended) > 0):
            print("Step6: Video_Intended length is greater than 0. {}".format(video_intended))



        # Step8: related_documents section should be atleast 1.
        if (len(related_departments) > 0):
            related_departments_covered = []
            related_departments_list = related_departments.split('#')
            for m in range(1, len(related_departments_list)):
                related_departments_covered.append(related_departments_list[m])
            print("Step8: related_departments length is greater than 0. {}".format(related_departments))

        # Step9: party_status section should be atleast 1.
        if (len(party_status) > 0):
            print("Step9: party_status length is greater than 0. {}".format(party_status))


        # Step10: targeted_parties section should be atleast 1.

        if (len(target_parties) > 0):

            target_parties_covered = []

            target_parties_list = target_parties.split('#')

            for m in range(1, len(target_parties_list)):

                target_parties_covered.append(target_parties_list[m])

            print("Step10: target_parties length is greater than 0. {}".format(target_parties))





        # Topic Scope
        topic_scope_topics = topic_scope.split('#')
        topic_scope_topics_list = []
        if (len(topic_scope_topics) > 0):
            for i in range(1, len(topic_scope_topics)):
                topic_scope_topics_list.append(topic_scope_topics[i].split(":")[0])


        topic_scope_text = topic_scope.splitlines()
        print(topic_scope_text)
        data = {}
        topic_scope_data = {}
        text = []
        key_flag = 0
        value_flag = 1
        key = ''
        for n in range(len(topic_scope_text)):
            if ('#' in topic_scope_text[n]):
                if (n == 0):
                    key = topic_scope_text[n]
                else:
                    data = {
                        key: text
                    }
                    topic_scope_data.update(data)

                    print(topic_scope_data)

                    key = topic_scope_text[n]

                    text = []

                # print("Key: {}".format(key))

            else:

                if (value_flag == n):

                    text.append(topic_scope_text[n])

                    value_flag += 1

                    # print("Value in else: {}".format(text))

                else:

                    text.append(topic_scope_text[n])

                    value_flag == n + 1

                    # print("Value in else-else: {}".format(text))

        data = {

            key: text

        }

        topic_scope_data.update(data)

        print("Step2: Notes data validation: {} ".format(topic_scope_data))








        context = {

            'video_id':video_id,

            'publishedAt':publishedAt,

            'search_kind':search_kind,

            'search_etag':search_etag,

            'video_kind':video_kind,

            'video_title':video_title,

            'description': description,

            'channel_title':channel_title,

            'channel_id':channel_id,

            'image_default_url':image_default_url,

            'image_default_width':image_default_width,

            'image_default_height':image_default_height,

            'image_medium':image_medium,

            'image_medium_width':image_medium_width,

            'image_medium_height':image_medium_height,

            'image_high':image_high,

            'image_high_width':image_high_width,

            'image_high_height':image_high_height,

            'tags':tags,

            'video_url':video_url,

            'new_title':new_title,

            'liveBroadcastContent':liveBroadcastContent,

            'validity_status':1,

            'notes':new_data,

            'topics':topics_topics_list,

            'speakers':speakers_covered,

            'questions':questions_data,

            'summary':summary_data,

            'video_intended':video_intended,

            'related_departments':related_departments_covered,

            'party_status':party_status,

            'target_parties':target_parties_covered,
	        'topic_scope':topic_scope_data,
	        'eng_text':english_text,
	        'telugu_text':telugu_text

        }



        context = {

            'context':context

        }



        #print(context)

        r = requests.post('https://c43w8otvfe.execute-api.us-west-1.amazonaws.com/test/updatevideodata', json=context)

        #print(r)

        if r.status_code == 200:

            return HttpResponse(r)

        return HttpResponse('Could not save data')









        

  
