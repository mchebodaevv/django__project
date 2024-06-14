from django.db import models


class ProductCategory(models.Model):
    category_name = models.CharField(max_length=100,unique=True, verbose_name='Категория', primary_key=True)
    def __str__(self):
        return self.category_name
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class Product(models.Model):
    name = models.CharField(max_length=100,verbose_name='Имя')
    description = models.TextField(verbose_name='Описание')
    quantity = models.IntegerField(verbose_name='Количество')
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE,verbose_name='Категория')

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

class Customer(models.Model):
    name = models.CharField(max_length=100,verbose_name='Имя')
    email = models.EmailField(verbose_name='Электронная почта')
    phone = models.CharField(max_length=15,verbose_name='Телефон')
    address = models.CharField(max_length=255,verbose_name='Адрес')

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class Order(models.Model):

    order_date = models.DateField(verbose_name='Дата заказа')
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE,verbose_name='ID клиента')
    def __str__(self):
        return f'Order {self.id}'
    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE,verbose_name='Номер заказа')
    product = models.ForeignKey(Product, on_delete=models.CASCADE,verbose_name='Номер товара')
    quantity = models.IntegerField(verbose_name='Количество')

    def __str__(self):
        return f'Detail {self.id} of Order {self.order.id}'
    class Meta:
        verbose_name = 'Детали заказа'
        verbose_name_plural = 'Детели заказа'

class Supplier(models.Model):
    name = models.CharField(max_length=100,verbose_name='Имя поставщика')
    contact_info = models.CharField(max_length=100,verbose_name='Контакты')
    address = models.CharField(max_length=255,verbose_name='Адрес')

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'

class Shipment(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE,verbose_name='Номер поставщика')
    product = models.ForeignKey(Product, on_delete=models.CASCADE,verbose_name='Номер товара')
    quantity = models.IntegerField(verbose_name='Количество')
    shipment_date = models.DateField(verbose_name='Дата поставки')

    def __str__(self):

        return f'Shipment {self.id}'
    class Meta:
        verbose_name = 'Поставка'
        verbose_name_plural = 'Поставки'

class Employee(models.Model):
    name = models.CharField(max_length=100,verbose_name='Имя сотрудника')
    email = models.EmailField(verbose_name='Электронная почта')
    phone = models.CharField(max_length=15,verbose_name='Номер телефона')
    position = models.CharField(max_length=100,verbose_name='Должность')

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'