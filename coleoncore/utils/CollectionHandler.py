
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
    

    #==============================
    def load_articles(self):
        articles = []
        for article in self.coleoncore.articles.all().order_by("created_at"):
            data = {"id": article.id}
            for column in self.columns:
                model_class = self.default_columns.get(column) #This gets the name of the table to know ehre to look for the article
                if model_class:
                    print("==============================")
                    related_obj = getattr(article, column)
 
                    print(related_obj)



            #print(article)

        return articles



"""             
                                    related_field_name = model_class._meta.model_name  
                    related_items = getattr(article, related_field_name).all()

                
                    if related_items.exists():
                        data[column] = related_items.first()  # assuming one-to-one semantics per column
                    else:
                        data[column] = None
            articles.append(data) 
"""