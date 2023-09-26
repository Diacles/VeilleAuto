from datetime import datetime, timedelta

class Date():

    def getDateAjd(self):
        today = datetime.now()
        annee = int(today.strftime("%Y"))
        mois = int(today.strftime("%m"))
        jour = int(today.strftime("%d"))
        ajd = datetime(annee, mois, jour)

        return ajd 

    def soustraireDate(self, date, nbJoursEnMoins):
        jourSoustrait = timedelta(nbJoursEnMoins)
        nvlDate = date - jourSoustrait

        return nvlDate
    
    def conversionDateTime(self, ms):
        return datetime.fromtimestamp(ms/1000)

    def conversionMs(self, date):
        dateMs = round(date.timestamp() * 1000)

        return dateMs

    def getAjdMs(self):
        ajd = self.getDateAjd()
        ajdMs = self.conversionMs(ajd)

        return ajdMs

    def getHierMs(self):
        ajd = self.getDateAjd()
        hier = self.soustraireDate(ajd, 1)
        hierMs = self.conversionMs(hier)

        return hierMs