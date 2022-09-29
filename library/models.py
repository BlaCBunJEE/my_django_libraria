from django.db import models


# Create your models here.
class LibraryUser(models.Model):
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    Email = models.EmailField(max_length=120)
    password = models.CharField(max_length=120)
    library_code = models.UUIDField(max_length=120)

    def __str__(self):
        return self.library_code


class Author(models.Model):
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    DOB = models.CharField(max_length=120)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class BooksMedia(models.Model):
    name = models.CharField(max_length=200)
    ISBN = models.CharField(max_length=120)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    Publisher = models.CharField(max_length=200)
    pub_date = models.CharField(max_length=200)
    price = models.IntegerField()
    units = models.IntegerField(default=2)

    def __str__(self):
        return self.name


class Cart(models.Model):
    user = models.ForeignKey(LibraryUser, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated', '-created']


class CartItem(models.Model):
    book = models.ForeignKey(BooksMedia, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    book_price = models.IntegerField(blank=True)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)

