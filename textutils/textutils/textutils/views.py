from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def analyse(request):
    #taking values from form tags
    djtext = request.POST.get('text','default')
    removepunc = request.POST.get('removepunc','off')
    removespace = request.POST.get('removespace','off')
    removenewline = request.POST.get('removenewline','off')
    fullcaps = request.POST.get('fullcaps','off')
    charcount = request.POST.get('charcount','off')

    punctuations = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''

    analysed = ""
    if removepunc == 'on':
        for char in djtext:
            if char not in punctuations:
                analysed = analysed + char
        param = {'anlysed': analysed}
        djtext = analysed

        # param = {'purpose' : 'Remove Punctuations', 'analysed' : analysed}

    if(removespace == 'on'):
        analysed = ''
        for index,char in enumerate(djtext):
            if djtext[index] == " " and djtext[index + 1] == " ":
                pass
            else:
                analysed = analysed + char
        param = {'anlysed': analysed}
        djtext = analysed

    if (removenewline == 'on'):
        analysed = ""
        for char in djtext:
            if char != '\n' and char != '\r':
                analysed = analysed + char
        # param = {'purpose': 'Remove Spaces', 'analysed': analysed}
        param = {'anlysed': analysed}
        djtext = analysed

    if (fullcaps == 'on'):
        analysed = ""
        for char in djtext:
            analysed = analysed + char.upper()
        # param = {'purpose': 'Remove Spaces', 'analysed': analysed}
        param = {'anlysed': analysed}
        djtext = analysed

    if (charcount == 'on'):
        analysed = ""
        for  char in djtext:
            analysed = analysed + char
            count = len(analysed)
        textmain = "Total Characters in Text : " + str(count)
        param = {'count': textmain}
        return render(request,'counter.html',param)

    # if(djtext == ""):
    #     return HttpResponse("Error ! Please Enter the Text in Textbox")

    if (removepunc != "on" and removespace!= "on" and removenewline!="on" and charcount!="on" and fullcaps != "on"):
        return HttpResponse("Error")

    return render(request, 'analyse.html', context=param)

