import django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

django.setup()

from store.models import Product, Category

# первый способ
category = Category.objects.get(name='Vegetables')
obj = Product(name='Carrots', description='Морковь', price=120,
             image='static/products/product-7.jpg',
             category=category)

obj.save()

# второй способ
obj = Product.objects.create(name='Fruit Juice',
                            description='Фруктовый сок',
                            price=120,
                            image='static/products/product-8.jpg',
                            category=Category.objects.get(name='Juice'))

