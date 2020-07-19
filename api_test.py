# -*- coding: utf-8 -*-
"""Just imports for libraries
"""
from summarizer import Summarizer
import time
import re
import nltk
import spacy

"""Timer for the debuging
"""
"""
start_time = time.time()
"""


"""Downloads so nltk won't scream at you
"""
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('punkt')
nltk.download('words')

"""A file opener for debuging
"""
"""
with open('input.txt', 'r',encoding="utf8") as file:
    body = file.read().replace('\n', '')
"""


def summarizer(argumet,ratio_t=0.5):
    """
    

    Parameters
    ----------
    argumet : String
        The text from the conversation/meeting. It will be processed
    ratio_t : float, optional
        It specifies how much of the original text we wish to keep. 
        The default is 0.5.

    Returns
    -------
    full : String
        The summary of our text(argument variable).
    dates : String
        The key dates from the text(argument variable).

    """
    model = Summarizer()
    result = model(argumet,ratio=ratio_t,min_length=60, max_length=160)
    full = ''.join(result)
    dates1 = re.findall(r'\d+\S\d+\S\d+', argumet)
    dates2 = re.findall(r'[A-Z]\w+\s\d+', argumet)
    dates = dates1+ dates2
    return full,dates



def summarize_elements(argumet,summarizer_ext=False):
    """
    

    Parameters
    ----------
    argumet : String
        The text from the conversation/meeting. It will be processed
    summarizer_ext : Boolean, optional
        If True will summarize further the keynotes on Organizations and people.
        The default is False.

    Returns
    -------
    org_tuple : List
        Pair of organization and key notes.
    people_tuple : List
        Pair of people and key notes.
    organization : List
        List of organizations mentioned.
    people : List
        List of people mentioned.

    """
    a_list = nltk.tokenize.sent_tokenize(argumet)
    nlp = spacy.load('en_core_web_sm')
    doc = nlp(argumet)
    
    organization = []
    people = [] 

    for entity in doc.ents:
        if entity.label_ == "ORG":
            organization.append(entity.text)
        if entity.label_ == "PERSON":
            people.append(entity.text)

    org_tuple = []
    people_tuple = []
    sent = ""
    for org in organization:
        for element in a_list:
            if org in element:
                sent = sent + " " + element 
        org_tuple.append([org,sent])
    
    for pep in people:
        for element in a_list:
            if pep in element:
                sent = sent + " " + element 
        people_tuple.append([pep,sent])
                
    if summarizer_ext:
        for index in range(len(org_tuple)):
            org_tuple[index][1],_ = summarizer(org_tuple[index][1])
        for index in range(len(people_tuple)):
            people_tuple[index][1],_ = summarizer(people_tuple[index][1])
    return org_tuple,people_tuple,organization,people


def text_writer(file,body):
    """

    Parameters
    ----------
    argument : String
        The file destination for the receit.
    body : String
        The text from the conversation/meeting.

    Returns
    -------
    None.

    """
    with open(file, "w", encoding="utf-8") as f:
        a,b,c,d=summarize_elements(body,summarizer_ext=True)
        result,date = summarizer(body)
        f.write("Summary: \n")
        f.write(result)
        f.write('\n')
        f.write("Dates: \n")
        for match in date:
            f.write(match)
            f.write('\n')
        f.write('\n')
            
        f.write("Organizations: \n")
        for org in c:
            f.write(org)
        f.write('\n')
            
        f.write("People: \n")
        for pep in d:
            f.write(org)
        f.write('\n')
            
        f.write("Organizations + Statement: \n")
        for org,stat in a:
            f.write(org)
            f.write('\n')
            f.write(stat)
            f.write('\n')
        
        f.write("People + Statement: \n")
        for pep,stat in b:
            f.write(pep)
            f.write('\n')
            f.write(stat)
            f.write('\n')
        
        f.close()
        
"""The print for the time debuging
"""    
"""
print("--- %s BERT seconds ---" % (time.time() - start_time))
"""