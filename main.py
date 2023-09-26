from Feedly import Feedly
from ChatGPT import ChatGPT
from Date import Date
from Notion import Notion
import json

with open('config.json') as configJSON:
    fichierConfig = json.load(configJSON)

date = Date()
feedly = Feedly(fichierConfig['feedly']['service_host'], fichierConfig['feedly']['token'])
chatGPT = ChatGPT(fichierConfig['chatGPT']['token'])
notion = Notion(fichierConfig['notion']['token'])
lesArticles = []

# Get every article from yesterday
lesArticles = feedly.getTousLesArticleDeCollectionHier('AI')

# Browse through the articles
for unArticle in lesArticles:
    # We take only necessary informations
    titre = unArticle["title"]
    datePublication = date.conversionDateTime(unArticle["published"]).strftime("%m/%d/%Y")
    auteur = unArticle["author"]
    url = unArticle["alternate"][0]["href"]
    resume = chatGPT.get_summary(url)

    # Informations are added into your Notion database
    print(notion.ajouteArticleBDD(titre, datePublication, auteur, resume, url))