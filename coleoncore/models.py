from django.db import models
from django.contrib.auth.models import User

#The coleoncore model is used to represent the collections of a user
#It stores the name of the collection, it's description and relevant dates (for ordering later)
#Each collection (coleoncore) is assocciated to a specific user.
class Coleoncore(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='collections')
    title = models.CharField(max_length=50)  # Name of the collection
    description = models.TextField(blank=True) # Description, mostrly for when the collection is shared
    date = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True) # for putting on the top of the list the last modified collection

    def __str__(self):
        return self.title

#The article model represent the articles within a collection
#From this articles are stored the relevant dates and the ID of the article
#Each article is assocciated with a specific collection.
class Article(models.Model):
    coleoncore = models.ForeignKey(Coleoncore, on_delete=models.CASCADE, related_name='articles')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Article {self.pk} in {self.coleoncore.title}" #Here's somethin cool ;) that is a f-string used to dinamicaly include values (is aso really small!!!)

#COLUMNS this are default models that represent the default columns that the app provides for the user
#Each table stores a specific column for a specific article in a specific collection

#selfex
class ArticleName(models.Model):
    article_ID = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='names') #The realted_name is so that later we an do article.names
    value = models.CharField(max_length=100)                                                #For now i don't think i' gonna support having many default columns so this could be named "name" but i'll leave it for future Guille to decide

#Price can have a speific currency or not from the available currencys
class ArticlePrice(models.Model):
    class Available_currencys(models.TextChoices):
        USD = 'USD','US Dollar'
        EUR = 'EURO','Euro'
        JPY = 'YEN','Yen'
        GBP = 'GBP','Pound'
        AUD = 'AUD','Australian Dollar'
        CAD = 'CAD','Canadian Dollar'
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='prices')
    value = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(
        max_length=5, 
        choices=Available_currencys.choices,
        default=Available_currencys.USD,
        null=True
    )

#Status can be MISSING, OBTAINED or ON_DEIVERY, representing the diferent statuses of a specific article
class ArticleStatus(models.Model):
    class Available_status(models.TextChoices):
        MISSING = 'missing', 'Missing'
        ON_DELIVERY = 'on_delivery', 'On Delivery'
        OBTAINED = 'obtained', 'Obtained'
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='prices')
    value = models.CharField(
        max_length=20, 
        choices=Available_status.choices,
        default=Available_status.MISSING,
    )

#selfex
class ArticleDescription(models.Model):
    article_ID = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='names') 
    value = models.TextField(max_length=100)  






"""     name = models.CharField(max_length=100,null=True) # self explanatory
    description = models.TextField(blank=True, null=True) # self explanatory
    purchase_date = models.DateField(null=True, blank=True) # Date of purchase, can act as arrival date if the latter is not chosen
    arrival_date = models.DateField(null=True, blank=True) # Date of arrival, can be chosen only if purchase date is chosen
    store = models.CharField(max_length=100, blank=True, null=True) # self explanatory
    state = models.CharField( # the state of an article can be missing, on delivery or obtained
        max_length=20,
        choices=ArticleState.choices,
        default=ArticleState.MISSING,
        null=True
    )
    image = models.URLField(blank=True, null=True)  # Images of articles may only be in the form of links (at the moment)
    number = models.PositiveIntegerField(null=True, blank=True)  # number, don't really know here to go with this right now, might make it not nullable
    set_name = models.CharField(max_length=100, blank=True, null=True) # if a sate name is added, when entering another one the previous one should be recomended
    amount = models.PositiveIntegerField(default=0, null=True) # amount of the article in state
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True) # self explanatory
    delivery_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True) # self explanatory
    custom = models.JSONField(default=dict, blank=True,null=True)  # Custom fields are stored in json
 """