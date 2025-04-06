from django.db import models
from django.contrib.auth.models import User


class Coleoncore(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='collections')
    title = models.CharField(max_length=50)  # Name of the collection
    description = models.TextField(blank=True) # Description, mostrly for when the collection is shared
    date = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True) # for putting on the top of the list the last modified collection

    def __str__(self):
        return self.title


class Article(models.Model):
    class ArticleState(models.TextChoices):
        MISSING = 'missing', 'Missing'
        ON_DELIVERY = 'on_delivery', 'On Delivery'
        OBTAINED = 'obtained', 'Obtained'

    name = models.CharField(max_length=100,null=True) # self explanatory
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

    coleoncore = models.ForeignKey(Coleoncore, on_delete=models.CASCADE, related_name='articles')

    def __str__(self):
        return self.name or "Unnamed article"
