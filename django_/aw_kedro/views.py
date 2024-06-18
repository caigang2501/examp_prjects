from django.shortcuts import render
from django.utils import timezone
from .models import Submit

import tensorflow as tf
import numpy as np
import pandas as pd
import joblib
import pickle


from mtranslate import translate




# submit_list = Submit.objects.filter()

def tf_sentiment(request):
    try:
        post_string = request.POST["input_text_name"]
        emotion_rating = 123
        submit = Submit(text = post_string,rating = emotion_rating,time=timezone.now())
        submit.save()
        submit_list = Submit.objects.all()
        submit_list = reversed(submit_list)
        context = {"emotion_rating": emotion_rating,"input_text":post_string,"submit_list":submit_list}
    except:
        submit_list = Submit.objects.all()
        submit_list.delete()
        emotion_rating = ''
        context = {"emotion_rating": '',"editable_text":'',"submit_list":submit_list}
    return render(request, "ali.html", context)

def ali(request):
    context = {}
    return render(request, "ali.html",context)

def base(request):
    context = {}
    return render(request, "base.html",context)

def register(request):
    context = {}
    return render(request, "register.html",context)