from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, Http404
from django.urls import reverse
from django.template.loader import render_to_string



months_dict = {
    'january': 'Learn Linux',
    'february': 'Learn Networking',
    'march': 'Learn Pyhton',
    'april': 'Learn Bash',
    'may': 'Learn Opreating System',
    'june': 'Learn Information Gathering',
    'july': 'Learn OSINT',
    'august': 'Learn Security',
    'september': 'Learn Owasp Top 10',
    'october': 'Learn Web Security',
    'november': 'Learn Windows',
    'december': 'Learn Active Directory'
}

def index(request):
    # items = ""
    months = list(months_dict.keys())
    # for month in months:
    #     capitilized_month = month.capitalize()
    #     month_path = reverse('month-challenge', args=[month])
    #     items += f"<li><a href=\"{month_path}\">{capitilized_month}</li>"
    # response_data = f"<ul>{items}</ul>"
    return render(request, 'challanges/index.html',{'months':months, })



def monthlychallengesbynum(request, month):
    months = list(months_dict.keys())
    if month > len(months):
        return HttpResponseNotFound("not found")
    redirect_month = months[month - 1]
    redirect_path = reverse('month-challenge', args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthlychallenges(request, month):
    try:
        challenge_text = months_dict[month]
        return render(request, 'challanges/challenges.html',{'challenges':challenge_text,'month':month})
    except:
        respose = render_to_string("404.html")
        return HttpResponseNotFound(respose)
