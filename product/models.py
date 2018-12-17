from django.db import models as db
from django.contrib.auth.models import User

# Create your models here.
class Product(db.Model):
    title = db.CharField(max_length = 100)
    url = db.URLField()
    pub_date = db.DateTimeField(auto_now_add = True)
    votes_total = db.IntegerField(default = 0)
    image = db.ImageField(upload_to = 'images/')
    icon = db.ImageField(upload_to = 'images/')
    body = db.TextField()
    hunter = db.ForeignKey(User, on_delete = db.SET_NULL, null = True)

    def __str__(self):
        return self.title

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')

    @staticmethod
    def latest_products():
        return Product.objects.order_by('-pub_date')
