
from models import (
    Coleoncore, Article, Name, Image, Status, Price, Description,
    Store, Purchase_date, Arrival_date, Set, Amount,
    Delivery_price, Author, Artist, Saga, Language, Custom
)

class CollectionHandler:
    default_column_mapping = {
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

    # Creates an ampty article (maybe later i add some options to create whith data but for now i dnt need to)
    def create_article(self):
        article = Article.objects.create(coleoncore=self.collection)
        for column in self.columns:
            model_class = self.default_column_mapping.get(column)
            if model_class:
                model_class.objects.create(article_id=article)
        return article

    #Creates a collection 
    #This is a class method and returns a CollectionHandler object
    @classmethod
    def create_collection(user, title, columns=None): 
        coleoncore = Coleoncore.objects.create(
            user=user,
            title=title,
            columns=columns if columns else None  # If no columns are passed then the model use his defaults
        )
        handler = CollectionHandler(coleoncore) #Calls to the constructor
        handler.create_article()
        return handler

