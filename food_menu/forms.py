from django import forms
from .models import Item


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item  # Use Item as model for this form
        fields = ['item_name', 'item_desc', 'item_price', 'item_image']  # Data fields for form
