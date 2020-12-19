import json
import requests
import datetime
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader


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
            user = form.save()
            user.is_active = False
            user.save()
            return redirect('/')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})
class GetDroplets(TemplateView):
    template_name = 'droplets.html'
    def get_context_data(self):
        url = 'https://c43w8otvfe.execute-api.us-west-1.amazonaws.com/test/videodata'
        channel_title = "JanaSena Party"
        publishedAt = datetime.datetime.today().strftime('%Y-%m-%d')
        context = {
            "channel_title":channel_title,
            "publishedAt":publishedAt,
        }
        r = requests.get(url,json = context)
        droplets = r.json()

        context = {
            'droplets': json.loads(droplets['body']),
        }

        return context


def query_data(request):
    publishedAt = request.POST.get('publishedAt')
    channel_title = request.POST.get('channel_title')
    url = 'https://c43w8otvfe.execute-api.us-west-1.amazonaws.com/test/videodata'
    context = {
        "channel_title":channel_title,
        "publishedAt":publishedAt,
    }
    r = requests.get(url,json=context)
    droplets = r.json()
    context = {
            'droplets': json.loads(droplets['body']),
            'publishedAt' :publishedAt,
            'channel_title':channel_title
    }
    return render(request, 'droplets.html', context)



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
        telugu_text = request.POST.get('telugu_text')

        print(notes)

        # Step1: Get Notes
        
        notes_data = json.loads(notes)

        # Step2: get topics

        topics_topics_list = topics.splitlines()

        #Step3: Speakers section should be atleast 1. Even automated if required.
        speakers_covered = speakers.splitlines()

        # Step4: Questions section should be atleast 1. Even automated if required.

        questions_data = json.loads(questions)

        # Step5: Summary section should be atleast 1. Even automated if required.
        summary_data = json.loads(summary)

        # Step6: Video_Intended section should be atleast 1.
        if (len(video_intended) > 0):
            print("Step6: Video_Intended length is greater than 0. {}".format(video_intended))



        # Step8: related_documents section should be atleast 1.
        related_departments_list = related_departments.splitlines()

        # Step9: party_status section should be atleast 1.
        if (len(party_status) > 0):
            print("Step9: party_status length is greater than 0. {}".format(party_status))


        # Step10: targeted_parties section should be atleast 1.
        target_parties_covered = target_parties.splitlines()





        # Topic Scope
        topic_scope_data = json.loads(topic_scope)

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

            'notes':notes_data,

            'topics':topics_topics_list,

            'speakers':speakers_covered,

            'questions':questions_data,

            'summary':summary_data,

            'video_intended':video_intended,

            'related_departments':related_departments_list,

            'party_status':party_status,

            'target_parties':target_parties_covered,
	        'topic_scope':topic_scope_data,
	        'eng_text':english_text,
	        'telugu_text':telugu_text

        }



        context = {

            'context':context

        }



        r = requests.post('https://c43w8otvfe.execute-api.us-west-1.amazonaws.com/test/updatevideodata', json=context)

        
        if r.status_code == 200:

            url = 'https://c43w8otvfe.execute-api.us-west-1.amazonaws.com/test/videodata'
            context = {
                "channel_title":channel_title,
                "publishedAt":publishedAt,
            }
            r = requests.get(url,json=context)
            droplets = r.json()
            publishedAt = publishedAt[0:10]
            context = {
                'droplets': json.loads(droplets['body']),
                "channel_title":channel_title,
                "publishedAt":publishedAt,
            }
            return render(request, 'droplets.html', context)

        return HttpResponse('Could not save data')









        

  
