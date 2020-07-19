# EfiMeets - InstepHack
Problem Statement: Build a prototype to capture real time audio

    There has been a permanent shift towards a virtual workplace
    We should be getting the most out of our meetings
        - Summarization
        - Reminders
        - Keypoints
    No more screenshots, no more stopping meetings, just EfiMeet
    Now is a time where stakeholders need to be as attentive as possible
    EfiMeet knows that things happen and distractions are everywhere
    EfiMeet is here to show you that that’s all right

![alt text](https://github.com/Priya-05/InstepHack/blob/master/Screenshots/efinotes1.png)

Getting the Audio Data:
  - Using Microphone 
  -Using Chrome Tab Audio capture
Giving the text data:
  - Transcribes in PDF/Text form
  - Text summary in PDF/Text form

![alt text](https://github.com/Priya-05/InstepHack/blob/master/Screenshots/efinotes2.png)

Generating Text from audio:
  - It uses the Speech-recognizer python library and google recognizer to get the text from the file
Generate Summaries:
  - It uses BERT (Bidirectional Encoder Representations from Transformers developed by google) summarizer to generate meaningful summaries. 
  - It also uses BERT to extract certain information from the text(Text mining) 




![alt text](https://github.com/Priya-05/InstepHack/blob/master/Screenshots/efinotes3.png)

Model View Controller Architecture

MODEL:

    BERT, or Bidirectional Encoder Representations from Transformers, is a new method of pre-training language representations which obtains state-of-the-art       results on a wide array of Natural Language Processing (NLP) tasks.

    GitHub - https://github.com/google-research/bert
    
  ![alt text](https://github.com/Priya-05/InstepHack/blob/master/Screenshots/images/bert_images.jpeg)
  
  
View:

    HTML + Bootstrap
    
   ![alt text](https://github.com/Priya-05/InstepHack/blob/master/Screenshots/images/Unknown-1.png) ![alt text](https://github.com/Priya-05/InstepHack/blob/master/Screenshots/images/Unknown-2.png) 


Controller: 

    Flask - is a lightweight WSGI web application framework. It is designed to make getting started quick and easy, with the ability to scale up to complex applications.
    
    Flask Documentation - https://pymbook.readthedocs.io/en/latest/flask.html
        
        ![alt text](https://github.com/Priya-05/InstepHack/blob/master/Screenshots/images/Unknown.png)

![alt text](https://github.com/Priya-05/InstepHack/blob/master/Screenshots/efinotes4.png)

Backend:
 
   EfiMeets takes advantage of python's PYDUB and SpeechRecognition library and googles speech-to-text api
   
   ![alt text](https://github.com/Priya-05/InstepHack/blob/master/Screenshots/images/google%20cloud%20logo.jpg) 
   ![alt text](https://github.com/Priya-05/InstepHack/blob/master/Screenshots/images/Unknown.png)
    

