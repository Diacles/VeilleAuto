import requests

class Notion():
    def __init__(self, unToken):
        self.token = unToken
    
    def ajouteArticleBDD(self, titre, datePublication, auteur, resume, url):
        urlRequete = "https://api.notion.com/v1/pages"
        headers = {
            "accept": "application/json",
            "Notion-Version": "2022-06-28",
            "content-type": "application/json",
            "Authorization": self.token
        }

        payload = {
            "parent": {
                "type":"database_id",
                "database_id":"b4bfeedd2a4147708ea5970bae0ce7d1"
            },
            "properties": {
                "Titre": {
                    "title":[{
                        "text": {
    	    			"content": titre
                        }
                    }]
    	    	},
                "Date": {
                    "rich_text":[{
                        "text": {
    	    			"content": datePublication
                        }
                    }]
    	    	},        
                "Auteur": {
                    "rich_text":[{
                        "text": {
    	    			"content": auteur
                        }
                    }]
    	    	},
                "Contenu": {
                    "rich_text":[{
                        "text": {
    	    			"content": resume
                        }
                    }]
    	    	},
                "URL": {
                    "rich_text":[{
                        "text": {
    	    			"content": url
                        }
                    }]
    	    	}
            }
        }

        return requests.post(urlRequete, json=payload, headers=headers)