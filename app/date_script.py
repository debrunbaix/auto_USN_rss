from datetime import date, datetime

def get_today_date():
    today = date.today()
    return today

def convert_article_date(article_date_str):
    # Format de la date de l'article
    article_date_format = "%a, %d %b %Y %H:%M:%S %z"

    # Convertir la chaîne de date de l'article en objet datetime
    article_date = datetime.strptime(article_date_str, article_date_format)
    
    return article_date.date() 