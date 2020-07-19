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
with open('wayneOlsenText.txt', 'r',encoding="utf8") as file:
    body = file.read().replace('\n', '')
"""


def summarizer(argumet,ratio_t=0.5,summarizer_ext=False):
    """


    Parameters
    ----------
    argumet : String
        The text from the conversation/meeting. It will be processed
    ratio_t : float, optional
        It specifies how much of the original text we wish to keep.
        The default is 0.5.
    summarizer_ext : Boolean, optional
        If True will summarize further the keynotes on Organizations and people.
        The default is False.

    Returns
    -------
    full : String
        The summary of our text(argument variable).
    dates : DataObject
        The key dates from the text(argument variable).
    date_tuple: List
        Contains a pair of dates and the associated text for them

    """
    model = Summarizer()
    result = model(argumet,ratio=ratio_t,min_length=60, max_length=160)
    full = ''.join(result)
    dates1 = re.findall(r'\d+\S\d+\S\d+', argumet)
    dates2 = re.findall(r'[A-Z]\w+\s\d+', argumet)
    dates = dates1 + dates2
    a_list = nltk.tokenize.sent_tokenize(argumet)
    date_tuple = []
    sent = ""
    for dat in dates:
        dat = str(dat)
        for element in a_list:
            if dat in element:
                sent = sent + " " + element
        date_tuple.append([dat,sent])
    if summarizer_ext:
        for index in range(len(date_tuple)):
                date_tuple[index][1] = model(date_tuple[index][1])
    return full,dates,date_tuple



def summarize_elements(argumet,ratio=0.5,summarizer_ext=False):
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
            org_tuple[index][1],_,_ = summarizer(org_tuple[index][1],ratio)
        for index in range(len(people_tuple)):
            people_tuple[index][1],_,_ = summarizer(people_tuple[index][1],ratio)
    return org_tuple,people_tuple,organization,people


def text_writer(file,body,title):
    """

    Parameters
    ----------
    argument : String
        The file destination for the receit.
    body : String
        The text from the conversation/meeting.
    title : String
        The title of the meeting.

    Returns
    -------
    None.

    """
    with open(file, "w", encoding="utf-8") as f:
        a,b,c,d=summarize_elements(body,0.1,summarizer_ext=True)
        result,date,e = summarizer(body,0.1,summarizer_ext=True)
        f.write("#Meeting: ")
        f.write(title)
        f.write("\n")
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

        f.write("Dates + Statement: \n")
        for date,stat in e:
            f.write(date)
            f.write('\n')
            f.write(stat)
            f.write('\n')

        f.close()
        
def file_maker(title,a,b,c,d,result,date,e):
    """

    Parameters
    ----------
    argument : String
        The file destination for the receit.
    body : String
        The text from the conversation/meeting.
    title : String
        The title of the meeting.

    Returns
    -------
    None.

    """
    big_string=""
    big_string = big_string + "#Meeting: "
    big_string = big_string +title
    big_string = big_string +"\n"
    big_string = big_string +"Summary: \n"
    big_string = big_string +result
    big_string = big_string +'\n'
    big_string = big_string +"Dates: \n"
    for match in date:
        big_string = big_string + str(match)
        big_string = big_string +'\n'
    big_string = big_string +'\n'

    big_string = big_string +"Organizations: \n"
    for org in c:
        big_string = big_string +org
    big_string = big_string +'\n'

    big_string = big_string +"People: \n"
    for pep in d:
        big_string = big_string +org
    big_string = big_string +'\n'

    big_string = big_string +"Organizations + Statement: \n"
    for org,stat in a:
        big_string = big_string +org
        big_string = big_string +'\n'
        big_string = big_string +stat
        big_string = big_string +'\n'

    big_string = big_string +"People + Statement: \n"
    for pep,stat in b:
        big_string = big_string +pep
        big_string = big_string +'\n'
        big_string = big_string +stat
        big_string = big_string +'\n'

    big_string = big_string +"Dates + Statement: \n"
    for date,stat in e:
        big_string = big_string +date
        big_string = big_string +'\n'
        big_string = big_string +stat
        big_string = big_string +'\n'

    return big_string
        
#text_writer("out2.md",body,"EfiMeets")   
"""The print for the time debuging
"""
"""
print("--- %s BERT seconds ---" % (time.time() - start_time))
"""
