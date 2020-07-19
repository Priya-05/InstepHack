

from flask import Flask, Response
from flask import request
from flask import render_template
import api_test as app_bert
import speech_recognition as sr
import smallwav as wav
import splitAudio as split
r = sr.Recognizer()

app = Flask(__name__,template_folder="templates")
plain_txt = ""

@app.route('/',methods=['POST','GET'])
def index():
    return render_template('index.html',org_tuple="",people_tuple="",
                           organization="",people="",sumary="",dates="",
                           date_tuple="",len1="",len2="",
                           len3="",len4="",len5="",
                           len6="")

@app.route('/file',methods=['POST','GET'])
def audio(): 
    if request.method == "POST":
        ratio = float(request.form['ratio'])
        file_information = request.files['file']
        file = split.get_large_audio_transcription(file_information)
        body = file
        a,b,c,d=app_bert.summarize_elements(body,ratio,summarizer_ext=True)
        result,date,e = app_bert.summarizer(body,ratio,summarizer_ext=True)
        global plain_txt
        plain_txt = app_bert.file_maker(str(file_information.name), a, b, c, d, result, date, e)
    return render_template('index.html',org_tuple=a,people_tuple=b,
                           organization=c,people=d,sumary=result,dates=date,
                           date_tuple=e,len1=len(a),len2=len(b),
                           len3=len(c),len4=len(d),len5=len(date),
                           len6=len(e))
 
@app.route('/getfile',methods=['POST','GET'])
def download():
    return Response(plain_txt,
                       mimetype="text/plain",
                       headers={"Content-Disposition":
                                    "attachment;filename=efinotes.md"})

if __name__ == '__main__':
    app.run(debug=True)