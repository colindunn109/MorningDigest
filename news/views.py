from django.shortcuts import render, redirect
from django.views import generic
from . import models

# WebScraping packages
import requests
requests.packages.urllib3.disable_warnings()
from bs4 import BeautifulSoup


#----webscrape for tech news on medium----
def techScrape(request):
    session = requests.Session()
    session.headers = {"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"}

    url = "https://medium.com/topic/technology"
    content = session.get(url,verify=False).content


    soup = BeautifulSoup(content, "html.parser")

    listings = soup.find_all('section',{'class':"m n o fe q d"})
    for item in listings:
        title = item.find_all('h3',{'class':'ai y cl bj cm bk dw fl fm d an dy cr'})[0].text
        desc = item.find_all('div',{'class':'dv d'})[0].text
        link = item.find('a').get('href')
        new_article = models.Article()
        new_article.title = title
        new_article.url = link
        new_article.summary = desc
        new_article.save()

    return redirect('/')

def RightPoliticsScrape(request):
    session = requests.Session()


#----Class views-----

class ArticleListView(generic.ListView):
    model = models.Article


class ArticleDetailView(generic.DetailView):
    context_object_name = "article_detail"
    template_name = "news/article_detail.html"
    model = models.Article
    fields = ('title','content','url')

class PoliticsArticleListView(generic.ListView):
    model = models.PoliticsArticle
