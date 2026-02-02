from django.db import models


class ServiceType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}- {self.pk}'

    class Meta:
        verbose_name = 'тип-услуг'
        verbose_name_plural = 'типы-услуги'


class Master(models.Model):
    image = models.ImageField(verbose_name='Image')
    name = models.CharField(max_length=100)
    typename = models.ForeignKey(ServiceType, on_delete=models.CASCADE)

    experience = models.CharField(max_length=100)
    information = models.CharField(max_length=100)

    class Meta:
       verbose_name = 'Мастер'
       verbose_name_plural = 'Мастеры'


    def __str__(self):
      return f"{self.name} {self.typename}"


class Photo(models.Model):
    master = models.ForeignKey(Master, on_delete=models.CASCADE, related_name='photos')
    typename = models.ForeignKey(ServiceType, on_delete=models.CASCADE)
    image = models.ImageField(verbose_name='Image')
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Фотогалерея работ'
        verbose_name_plural = 'Фотогалерея работы'

    def __str__(self):
        return self.name


class Feedback(models.Model):
    master = models.ForeignKey(Master, on_delete=models.CASCADE)
    typename = models.ForeignKey(ServiceType, on_delete=models.CASCADE)
    text = models.TextField(verbose_name='Текст отзыва')
    rating = models.PositiveSmallIntegerField(verbose_name='Звёзды')
    name = models.CharField(max_length=100, verbose_name='Имя')
    role = models.CharField(max_length=100, verbose_name='Профессия')
    avatar = models.ImageField(verbose_name='Фото')

    class Meta:
        verbose_name = 'Отзывы клиента'
        verbose_name_plural = 'Отзывы клиентов'


    def __str__(self):
        return f"{self.name}"





class Services(models.Model):
    typename = models.ForeignKey(ServiceType, on_delete=models.CASCADE, related_name='services',)
    photo = models.ImageField(verbose_name='Фото')
    name = models.CharField(max_length=100)
    money = models.PositiveIntegerField(verbose_name="Цена")

    class Meta:
        verbose_name = 'Услуги'
        verbose_name_plural = 'Услугие'

    def __str__(self):
        return f"{self.name}"



class Booking(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)

    service = models.ForeignKey(ServiceType, on_delete=models.CASCADE, related_name='bookings')

    master = models.ForeignKey(Master, on_delete=models.CASCADE, related_name='bookings')

    date = models.DateField()
    time = models.TimeField()
    comment = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} — {self.date} {self.time}"