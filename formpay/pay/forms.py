from django import forms


class PayForm(forms.Form):
    merchant = forms.CharField(max_length=128)
    amount = forms.DecimalField(
        min_value=1.00,
        max_digits=5,
        decimal_places=2,
    )
    order_id = forms.CharField(max_length=50)
    description = forms.CharField(max_length=250)
    success_url = forms.CharField(
        max_length=128,
    )
    testing = forms.BooleanField()
    client_phone = forms.CharField(max_length=15)
    receipt_items = forms.JSONField()
    unix_timestamp = forms.DateTimeField()
