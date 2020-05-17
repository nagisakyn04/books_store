from django.db import models

class Category(models.Model):
    name = models.CharField("Категория ", max_length=150)
    description = models.TextField("Описание")
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Author(models.Model):
    name = models.CharField("Автор", max_length=150)
    age = models.PositiveSmallIntegerField("Возраст", default=0)
    description = models.TextField("Описание")
    image = models.ImageField("Изображение", upload_to="Authors/")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"

class Book(models.Model):
    title = models.CharField("Название", max_length=150)
    description = models.TextField("Описание")
    image = models.ImageField("Изображение", upload_to="Books/")
    year = models.PositiveSmallIntegerField("Год издания", default=0)
    category = models.ForeignKey(Category, verbose_name="Категория", on_delete=models.SET_NULL, null=True)
    author = models.ForeignKey(Author, verbose_name="Автор", on_delete=models.SET_NULL, null=True)
    cost = models.IntegerField("Цена", default=0)
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"

