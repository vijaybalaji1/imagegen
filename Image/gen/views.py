from django.shortcuts import render
import os
import openai

def imagegen(b):
        openai.api_key = 'sk-proj-6aLdogK43j1dHLzEg5aqT3BlbkFJh24ngMs3cB8fyzmPRDC4' # your api key
        openai.Model.list()
        c=openai.Image.create(
            prompt=b,
            n=6,
            size="1024x1024")
        return c.data

def index(request):
    url1="";url2="";url3="";url4="";url5="";url6=str()
    check = False
    valid = str()
    context = {}
    if request.method == "POST":
        b = request.POST['topic']
        print(b)
        lw = b.lower()
        s = lw.strip()
        try:
            if s == "pradeepa" or "pradeepa" in s:
                c = imagegen("Fighting Brother sister in Cartoon")
            elif s == "nandhini" or "nandhini" in s:
                c= imagegen("1 boy 2 girls siblings in cartoon")
            elif s == "mukesh" or "mukesh" in s:
                c= imagegen("Small Boy with two elder sisters eating in cartoon")
            else:
                c = imagegen(b)
            c1 = dict(c[0])
            c2 = dict(c[1])
            c3 = dict(c[2])
            c4 = dict(c[3])
            c5 = dict(c[4])
            c6 = dict(c[5])
            url1 = c1['url']
            url2 = c2['url']
            url3 = c3['url']
            url4 = c4['url']
            url5 = c5['url']
            url6 = c6['url']
            print(url2)
            check = True
        except:
            valid = "Can't display your request for Safety Reason"
        context = {'url1':url1,'url2':url2,'url3':url3,'url4':url4,'url5':url5,'url6':url6,'check':check,'valid':valid}
    else:
        print("passed")
        pass
    return render(request,"index.html",context)