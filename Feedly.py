import requests
import json
import random
from Date import Date

class Feedly():
    def __init__(self, unServiceHost, unToken):
        self.service_host = unServiceHost
        self.token = unToken
        self.date = Date()


    def getLesFlux(self):
        headers = {'Authorization': 'OAuth '+self.token}
        quest_url=self._get_endpoint('v3/subscriptions')
        res = requests.get(url=quest_url, headers=headers)
        return res.json()

    def getLesFluxTries(self, lesFlux):
        lesFluxTries = []
        compteur = 0

        for unFlux in lesFlux:
            if(unFlux['categories'][0]['label'] == 'AI'):
                lesFluxTries.append(unFlux)
                compteur += 1

        return lesFluxTries

    def getIdFlux(self, lesFlux):
        lesIdFlux = []

        for unFlux in lesFlux:
            lesIdFlux.append(unFlux['id'])

        return lesIdFlux

    def getLesIdArticles(self, idFlux, debutFourchette):
        headers = {'Authorization': 'OAuth '+self.token}
        quest_url=self._get_endpoint('/v3/streams/ids')
        params = dict(
                      streamId=idFlux,
                      newerThan=debutFourchette,
                      )
        lesArticles = requests.get(url=quest_url, params=params,headers=headers)

        return lesArticles.json()

    def getLesArticles(self, idFlux, debutFourchette):
        headers = {'Authorization': 'OAuth '+self.token}
        quest_url=self._get_endpoint('v3/streams/contents')
        params = dict(
                      streamId=idFlux,
                      newerThan=debutFourchette,
                      )
        lesArticles = requests.get(url=quest_url, params=params,headers=headers)

        return lesArticles.json()

    def getUrlArticle(self, unArticle):
        url = unArticle['alternate'][0]['href']

        return url

    def getInfoArticle(self, tabIdArticle):
        headers = {'content-type': 'application/json',
                   'Authorization': 'OAuth '+self.token
        }
        quest_url=self._get_endpoint('/v3/entries/.mget')
        params = dict(
                      entryId = tabIdArticle
                    )
        res = requests.post(url=quest_url, data=json.dumps(params), headers=headers)
        return res.json()
            
    def getArticleRandomHier(self, nomCollection):
        lesFlux = []
        lesArticles = []
        debutDate = self.date.getHierMs()
        finDate = self.date.getAjdMs()

        lesFlux = self.getLesFluxTries(nomCollection, self.getLesFlux())

        for unFlux in lesFlux:
            lesResultats = []
            lesResultats.append(self.getLesArticles(unFlux["id"], debutDate)['items'])

            for unResultat in lesResultats:
                for unArticle in unResultat:
                    if unArticle["published"] < finDate:
                        lesArticles.append(unArticle)
    
        return random.choice(lesArticles)
    
    def getTousLesArticleDeCollection(self, nomCollection):
        lesFlux = []
        lesArticles = []
        lesFlux = self.getLesFluxTries(nomCollection, self.getLesFlux())

        for unFlux in lesFlux:
            lesResultats = []
            lesResultats.append(self.getLesArticles(unFlux["id"])['items'])
            for unResultat in lesResultats:
                for unArticle in unResultat:
                    lesArticles.append(unArticle)

        return lesArticles

    def getTousLesArticleDeCollectionHier(self, nomCollection):
        lesFlux = []
        lesArticles = []
        debutDate = self.date.getHierMs()
        finDate = self.date.getAjdMs()
        lesFlux = self.getLesFluxTries(nomCollection, self.getLesFlux())

        for unFlux in lesFlux:
            lesResultats = []
            lesResultats.append(self.getLesArticles(unFlux["id"], debutDate)['items'])
            for unResultat in lesResultats:
                for unArticle in unResultat:
                    if unArticle["published"] < finDate:
                        lesArticles.append(unArticle)

        return lesArticles
    
    def _get_endpoint(self, path=None):
        url = "https://%s" % (self.service_host)

        if path is not None:
            url += "/%s" % path

        return url