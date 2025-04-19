
from coleoncore.models import (
    Coleoncore, Article, Name, Image, Status, Price, Description,
    Store, Purchase_date, Arrival_date, Set, Amount,
    Delivery_price, Author, Artist, Saga, Language, Custom
)

class CollectionHandler:
    default_columns = {
        "name": Name,
        "image": Image,
        "status": Status,
        "price": Price,
        "description": Description,
        "store": Store,
        "purchase_date": Purchase_date,
        "arrival_date": Arrival_date,
        "set": Set,
        "amount": Amount,
        "delivery_price": Delivery_price,
        "author": Author,
        "artist": Artist,
        "saga": Saga,
        "language": Language,
        "custom": Custom
    }

    #THIS is the constructor magic method
    def __init__(self, coleoncore_instance):
        self.coleoncore = coleoncore_instance
        self.columns = self.coleoncore.columns.split(":")
        self.articles=self.load_articles()
        #print("==============================")
        #print(self.columns)

    def __str__(self):
        return f"CollectionHandler for '{self.coleoncore.title}' (columns: {self.columns})"

    def __repr__(self):
        return f"<CollectionHandler id={self.coleoncore.id} title={self.coleoncore.title} columns={self.columns}>"


    # Creates an empty article (maybe later i add some options to create whith data but for now i dnt need to)
    def create_article(self):
        article = Article.objects.create(coleoncore=self.coleoncore)
        for column in self.columns:
            model_class = self.default_columns.get(column)
            if model_class:
                model_class.objects.create(article_id=article)
        return article



    #Creates a collection 
    #This is a static method and returns a CollectionHandler object
    @staticmethod
    def create_collection(user, title): 
        coleoncore = Coleoncore.objects.create(
            user=user,
            title=title,
        )
        handler = CollectionHandler(coleoncore) #Calls to the constructor that returns the instance of the object
        return handler
    
    #This is a way to create an article in a collection without having to create a Handler beforehand, this is to save recourses
    @classmethod
    def new_article(cls,coleoncore_instance): 
        article_json={}
        columns = coleoncore_instance.columns.split(":")
        #print("columns=================")
        #print(columns)
        article = Article.objects.create(coleoncore=coleoncore_instance)
        article_json["id"]=article.id
        for column in columns:
            model_class = cls.default_columns.get(column)
            if model_class:
                o=model_class.objects.create(article_id=article)
                #print(o.value)
                article_json[column]=cls.format_article(o,column)
        return article_json
    

#==============================





    def load_articles(self):
        articles = []
        for article in self.coleoncore.articles.all().order_by("created_at"):
            data = {}
            data["id"]=article.id
            for column in self.columns:
                model_class = self.default_columns.get(column) #This gets the model of the table to know ehre to look for the article
                if model_class:
                    related_obj = getattr(article, column) #This gets the OBJECT from a specific column related to a specific article
                    if related_obj:
                        data[column]=self.format_article(related_obj,column)
            articles.append(data)
        return articles


    @staticmethod
    def format_article(related_obj,column):
        currency_symbols = {
            'USD': '$',
            'EURO': '€',
            'YEN': '¥',
            'GBP': '£',
            'AUD': 'A$',
            'CAD': 'C$'
        }

        if column in ("delivery_price", "price") and hasattr(related_obj, "currency"):
            symbol = currency_symbols.get(getattr(related_obj, "currency", ""), "")
            return {"value":related_obj.value,"currency":symbol}
        else:
            return related_obj.value