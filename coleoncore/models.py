from django.db import models
from django.contrib.auth.models import User

#The coleoncore model is used to represent the collections of a user
#It stores the name of the collection, it's description and relevant dates (for ordering later)
#Each collection (coleoncore) is assocciated to a specific user.
class Coleoncore(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='collections') #Related name is to later be able to call user.collections and get all of them (explained later)
    title = models.CharField(max_length=50)  # Name of the collection
    description = models.TextField(blank=True) # Description, mostrly for when the collection is shared
    created_at = models.DateTimeField(auto_now_add=True) #Date of creation
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



#DEFAULT COLUMNS this are default models that represent the default columns that the app provides for the user
#Each table stores a specific column for a specific article in a specific collection

#==NAME============
#selfex
class Name(models.Model):
    article_id = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='names') #The realted_name is so that later we an do article.names
    value = models.CharField(max_length=100,blank=True)                                                #For now i don't think i' gonna support having many default columns so this could be named "name" but i'll leave it for future Guille to decide

#==PRICE================
#Price can have a speific currency or not from the available currencys
class Price(models.Model):
    class Available_currencys(models.TextChoices):
        USD = 'USD','US Dollar'
        EUR = 'EURO','Euro'
        JPY = 'YEN','Yen'
        GBP = 'GBP','Pound'
        AUD = 'AUD','Australian Dollar'
        CAD = 'CAD','Canadian Dollar'
    article_id = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='prices')
    value = models.DecimalField(max_digits=10, decimal_places=2,blank=True,null=True)
    currency = models.CharField(
        max_length=5, 
        choices=Available_currencys.choices,
        default=Available_currencys.USD,
        null=True
    )

#==STATUS====================
#Status can be MISSING, OBTAINED or ON_DEIVERY, representing the diferent statuses of a specific article
class Status(models.Model):
    class Available_status(models.TextChoices):
        MISSING = 'missing', 'Missing'
        ON_DELIVERY = 'on_delivery', 'On Delivery'
        OBTAINED = 'obtained', 'Obtained'
    article_id = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='status')
    value = models.CharField(
        max_length=20, 
        choices=Available_status.choices,
        default=Available_status.MISSING,
    )

#==DESCRIPTION==================
class Description(models.Model):
    article_id = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='descriptions') 
    value = models.TextField(max_length=100, blank=True)  


#==STORE============
#selfex
class Store(models.Model):
    article_id = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='stores') 
    value = models.CharField(max_length=100,blank=True)     

#===DATE OF PURCHASE=========
# Date of purchase, can act as arrival date if the latter is not chosen
class Purchase_date(models.Model):
    article_id = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='purchase_dates') 
    value = models.DateField(blank=True,null=True)

#===DATE OF ARRIVAL========
# Date of arrival, can be chosen only if purchase date is chosen (maybe ?)
class Arrival_date(models.Model):
    article_id = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='arrival_dates') 
    value = models.DateField(blank=True,null=True)


class Image(models.Model):
    article_id = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='images') 
    value = models.URLField(blank=True,null=True) 

class Set(models.Model):
    article_id = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='sets') 
    value = models.CharField(max_length=100,blank=True) 

class Amount(models.Model):
    article_id = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='amounts') 
    value = models.PositiveIntegerField(default=0)


class Delivery_price(models.Model):
    class Available_currencys(models.TextChoices):
        USD = 'USD','US Dollar'
        EUR = 'EURO','Euro'
        JPY = 'YEN','Yen'
        GBP = 'GBP','Pound'
        AUD = 'AUD','Australian Dollar'
        CAD = 'CAD','Canadian Dollar'
    article_id = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='delivery_price')
    value = models.DecimalField(max_digits=10, decimal_places=2,blank=True,null=True)
    currency = models.CharField(
        max_length=5, 
        choices=Available_currencys.choices,
        default=Available_currencys.USD,
        null=True
    )

class Author(models.Model):
    article_id = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='authors') 
    value = models.CharField(max_length=100,blank=True) 

class Artist(models.Model):
    article_id = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='artists') 
    value = models.CharField(max_length=100,blank=True) 

class Saga(models.Model):
    article_id = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='sagas') 
    value = models.CharField(max_length=100,blank=True) 

class Language(models.Model):
    article_id = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='languages') 
    value = models.CharField(max_length=100,blank=True) 



#============CUSTOM====================
# Custom fields are stored in json
class Custom(models.Model):
    article_id = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='customs') 
    value = models.JSONField(default=dict, blank=True) 





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