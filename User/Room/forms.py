from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['start_date', 'end_date', 'inquiry']
        widgets = {
            'start_date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control',
                'placeholder': 'Select start date',
            }),
            'end_date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control',
                'placeholder': 'Select end date',
            }),
            'inquiry': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your inquiry here',
                'rows': 4,
            }),
        }
        labels = {
            'start_date': 'Start Date',
            'end_date': 'End Date',
            'inquiry': 'Inquiry Details',
        }
