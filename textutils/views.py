# i have create this file irfan 
from django.http import HttpResponse
from django.shortcuts import render 

def index(request):
	return render(request,'index.html')

def analyze(request):
	# Get the text
	# check checkbox value
	djtext = request.POST.get('text','default')
	removepunc = request.POST.get('removepunc','off')
	fullcaps = request.POST.get('fullcaps','off')
	newlineremover = request.POST.get('newlineremover','off')
	spaceremover = request.POST.get('spaceremover','off')
	extraspaceremover = request.POST.get('extraspaceremover','off')
	charcount = request.POST.get('charcount','off')
	# check which box is on
	if(removepunc == 'on'):
		punctuation='''!@#$%^&*(){[|}];:'''
		analyzed=""
		for char in djtext:
			if char not in punctuation:
				analyzed += char
		params = {'purpose':'Remove punctuation','analyzed_text':analyzed}
		#return render(request,'analyze.html',params)
		djtext = analyzed
	if(fullcaps=='on'):
		analyzed = ""
		for char in djtext:
			analyzed += char.upper()
		params = {'purpose':'chance upper case','analyzed_text':analyzed}

		#return render(request,'analyze.html',params)
		djtext = analyzed

	if(newlineremover=='on'):
		analyzed = ""
		for char in djtext:
			if char !="\n" and char !="\r":
				analyzed += char
		params = {'purpose':'Removed new lines','analyzed_text':analyzed}
		#return render(request,'analyze.html',params)
		djtext = analyzed
	if(spaceremover== 'on'):
		analyzed = ""
		for char in djtext:
			if char == " ":
				pass
			else:
				analyzed += char
		params = {'purpose':'Romoved Space','analyzed_text':analyzed}
		#return render(request,'analyze.html',params)
		djtext = analyzed
	if(extraspaceremover== 'on'):
		analyzed = ""
		for index,  char in enumerate(djtext):
			if not(djtext[index] ==  " " and djtext[index+1]==" "):
				analyzed += char
		params = {'purpose':'Extra Romoved Space','analyzed_text':analyzed}
		#return render(request,'analyze.html',params)
		djtext = analyzed
	if(charcount== 'on'):
		analyzed = ""
		for char in djtext:
			analyzed += char
		analyzed = f"char counter is {len(analyzed)}"
		params = {'purpose':'char counter','analyzed_text':analyzed}
		#return render(request,'analyze.html',params)

	if(charcount!= 'on' and extraspaceremover!= 'on' and spaceremover!= 'on'and newlineremover!='on' and fullcaps!='on' and removepunc != 'on'):
		return HttpResponse('Error')
	return render(request,'analyze.html',params)

def about(request):
	return render(request,'about.html')

def contact(request):
	return render(request,'contact.html')
