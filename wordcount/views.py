from django.http import HttpResponse
from django.shortcuts import render




def home(request):
	return render(request,'Home.html',{'HiThere': 'Its me Madhu'})

def products(request):
	return HttpResponse('<h1>welcome to our Products</h1>')
def count(request):
	fulltext=request.GET['fulltext']
	wordlist=fulltext.split()
	worddictionary = {}

	for word in wordlist:
		if word in worddictionary:
			#increase
			worddictionary[word] += 1
		else:
			# add to dict
			worddictionary[word] = 1


	
	return render(request,'count.html',{'fulltext':[fulltext,len(wordlist),worddictionary.items()]})
	
	