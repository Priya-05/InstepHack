#!/usr/bin/env python
# coding: utf-8

# In[3]:


get_ipython().system('pip list')


# In[2]:


get_ipython().system('pip install pyaudio')


# In[7]:


import speech_recognition as sr
# initialize the recognizer
r = sr.Recognizer()


# In[62]:



with sr.Microphone() as source:
    print("Talk")
    audio_text = r.listen(source, timeout=30)
    print("Time over, thanks")
# recoginize_() method will throw a request error if the API is unreachable, hence using exception handling
    
    try:
        # using google speech recognition
        print("Text: "+r.recognize_google(audio_text))
    except:
         print("Sorry, I did not get that")


# In[34]:


get_ipython().system('pip install nltk')


# In[25]:


#Loading NLTK
import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')


# In[21]:


from nltk.tokenize import sent_tokenize


# In[22]:


text="Hello Mr. Smith, how are you doing today? The weather is great, and city is awesome.The sky is pinkish-blue. You shouldn't eat cardboard. By the way, we will be having meeting tomorow"
tokenized_text=sent_tokenize(text)
print(tokenized_text)


# In[28]:


for sent in tokenized_text:
    tokens=nltk.word_tokenize(sent)
    print(nltk.pos_tag(tokens))


# In[37]:


get_ipython().system('pip install dateparser')


# In[38]:


get_ipython().system('pip install parsedatetime')


# In[39]:


import dateparser


# In[40]:


if dateparser.parse('By the way, we will be having meeting tomorrow?') != None:
    print('yes')
else:
    print('No')


# In[47]:


get_ipython().system('pip install dateutil.parse')


# In[56]:


from dateutil.parser import parse

def is_date(string, fuzzy=False):
    """
    Return whether the string can be interpreted as a date.

    :param string: str, string to check for date
    :param fuzzy: bool, ignore unknown tokens in string if True
    """
    try: 
        parse(string, fuzzy=fuzzy)
        return True

    except ValueError:
        return False


# In[69]:


is_date('today')


# In[ ]:





# In[ ]:




