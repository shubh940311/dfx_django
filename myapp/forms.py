
# forms.py
from django import forms
from .model import image


class HotelForm(forms.ModelForm):

    class Meta:
        model = image.Hotel
        fields = ['name', 'hotel_Main_Img']
