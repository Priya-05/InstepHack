# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 13:37:00 2020

@author: mihne
"""

import speech_recognition as sr
r = sr.Recognizer()

def audio_txt(path):
    hellow=sr.AudioFile(path)
    with hellow as source:
        audio = r.record(source)
    try:
        s = r.recognize_google(audio)
        return s
    except Exception as e:
        print("Exception: "+str(e))