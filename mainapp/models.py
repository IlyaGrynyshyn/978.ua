import random
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, AbstractUser
from django.utils.translation import gettext_lazy as _

User = get_user_model()


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    # return 'products/{0}/{1}/{2}'.format(instance.category.name, instance.title, filename)
    return 'products/{0}'.format( filename)


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name="Ім'я категорії")
    slug = models.SlugField(unique=True, db_index=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("category_detail", kwargs={'category_slug': self.slug})

    # Для відображення в адмінці назви

    class Meta:
        verbose_name = 'Категорії'
        verbose_name_plural = 'Категорії'

def get_product_code():
        code = random.randint(100000, 999999)
        return code

class Product(models.Model):
    category = models.ForeignKey(Category, verbose_name='Категорія', on_delete=models.CASCADE)
    title = models.CharField(max_length=150, verbose_name='Назва')
    slug = models.SlugField(unique=True, db_index=True)
    product_code = models.IntegerField(default=get_product_code(), verbose_name='Код продукту', blank=True, null=False)
    img = models.ImageField(verbose_name='Фотокартка', upload_to=user_directory_path)
    qty_product = models.IntegerField(default=1, verbose_name='Кількість товару')
    price = models.IntegerField(verbose_name='Ціна')
    new_price = models.IntegerField(null=True, blank=True, verbose_name='Нова ціна')
    description = models.TextField(verbose_name='Опис')
    features = models.ManyToManyField("specs.ProductFeatures", blank=True, related_name='features_for_product')
    ordered = models.IntegerField(default=0,verbose_name='Замовлено разів')


    # time_create = models.DateTimeField(auto_created=True,verbose_name='Час створення')

    def __str__(self):
        return self.title


    def get_features(self):
        return {f.feature.feature_name: ' '.join([f.value, f.feature.unit or ""]) for f in self.features.all()}

    def get_absolute_url(self):
        return reverse('product_detail', kwargs={'product_slug': self.slug})

    class Meta:
        verbose_name = 'Продукція'
        verbose_name_plural = 'Продукція'


class ProductImage(models.Model):
    product = models.ForeignKey(Product, default=None, on_delete=models.CASCADE)
    img = models.ImageField(upload_to=user_directory_path)

    def __str__(self):
        return self.product.title
