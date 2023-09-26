import openai

class ChatGPT():
    def __init__(self, unToken):
        self.token = unToken

    def get_summary(self, url):
        openai.api_key = self.token

        # Ajouter le titre de l'article et l'auteur pour une requête plus précise
        prompt = f"Résumez l'article '{url}' en quelques phrases."
        
        # Utiliser le modèle de langage le plus récent
        model_engine = "text-davinci-003"
        
        # Ajuster les paramètres de l'API pour améliorer la qualité des résumés
        completions = openai.Completion.create(
            engine=model_engine,
            prompt=prompt,
            max_tokens=500,
            n=1,
            stop=None,
            temperature=0.5,
        )
                
        # Récupérer la réponse de l'API et renvoyer le résumé
        message = completions.choices[0].text.strip()
        return message
