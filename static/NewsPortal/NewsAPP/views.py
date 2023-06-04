from django.shortcuts import render

# Create your views here.

def MoviesInfo(request):
    my_dict={
        'head_msg':'Movies Information',
        'sub_msg1':'Sonali slowly gettin Cured',
        'sub_msg2':'Bahubali 3 is just planning',
        'sub_msg3':'Salman khan Ready to marriage',
    }
    return render(request, 'newsapp/news.html',my_dict)
def SportsNews(request):
    my_dict={
        'head_msg':'Sports Information',
        'sub_msg1':'Anushka Sharma Firing Like Anything',
        'sub_msg2':'Kohli Updating in game anything can happend',
        'sub_msg3':'Worst proformance by India-Sehwag',
    }
    return render(request, 'newsapp/news.html',my_dict)

def PoliticsInfo(request):
    my_dict={
        'head_msg':'Policts Information',
        'sub_msg1':'Ache Din aa Gaya',
        'sub_msg2':'Rupee Value Now 1$:70Rs',
        'sub_msg3':'In India Single Paisa Black Money No More',
    }
    return render(request, 'newsapp/news.html',my_dict)

def Durga_News(request):
    return render(request, 'newsapp/index.html')