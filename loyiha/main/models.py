from django.db import models


class Home(models.Model):
    bg_img = models.ImageField()
    logo = models.ImageField()
    title = models.CharField(max_length=225)
    photo = models.ImageField(upload_to="Home/")

    def __str__(self):
        return self.logo


class Order(models.Model):
    title = models.TextField()
    text = models.TextField()
    name = models.CharField(max_length=200)
    phone = models.IntegerField()
    photo = models.ImageField()

    def __str__(self):
        return self.name


class Ads(models.Model):
    bg_img = models.ImageField()
    image = models.ImageField()
    photo = models.ImageField()
    name = models.CharField(max_length=200)
    price = models.IntegerField()

    def __str__(self):
        return self.photo


class Product(models.Model):
    text = models.TextField()
    photo = models.ImageField(upload_to="")

    def __str__(self):
        return self.text


class Prod(models.Model):
    image = models.ImageField(upload_to='Product/')
    text = models.TextField()
    photo = models.ImageField(upload_to='Product/')

    def __str__(self):
        return self.image


class Company(models.Model):
    gb_rasm = models.ImageField(upload_to='Company/')
    name = models.CharField(max_length=200)
    text = models.TextField()
    photo = models.ImageField(upload_to='Company/')

    def __str__(self):
        return self.gb_rasm


class Question(models.Model):
    title = models.TextField()
    bg_img = models.ImageField(upload_to='Question/')
    photo = models.ImageField(upload_to='Question/')

    def __str__(self):
        return self.title


class Method(models.Model):
    bg_img = models.ImageField(upload_to='Method/')
    name = models.CharField(max_length=200)
    text = models.TextField()

    def __str__(self):
        return self.text


class Fact(models.Model):
    bg_img = models.ImageField(upload_to='Fact/')

    def __str__(self):
        return self.bg_img
