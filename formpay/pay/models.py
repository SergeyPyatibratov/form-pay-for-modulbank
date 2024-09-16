from django.db import models


class Pay(models.Model):
    amount = models.DecimalField(
        verbose_name='Сумма платежа, руб',
        max_digits=5,
        decimal_places=2,

    )
    payment_purpose = models.CharField(
        verbose_name='Назначение платежа',
        max_length=128,
    )
    client_phone = models.CharField(
        verbose_name='Номер телефона',
        max_length=15,
        blank=True,
    )
    client_email = models.EmailField(
        verbose_name='Email клиента',
        max_length=64,
    )
    created = models.DateTimeField(auto_now_add=True)
