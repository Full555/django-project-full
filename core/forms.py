from django import forms
from .models import Booking, ServiceType, Master

class BookingForm(forms.ModelForm):
    service = forms.ModelChoiceField(
        queryset=ServiceType.objects.all(),
        empty_label="Выберите услугу",
        widget=forms.Select(attrs={'class': 'modal-input'})
    )
    master = forms.ModelChoiceField(
        queryset=Master.objects.all(),
        empty_label="Выберите мастера",
        widget=forms.Select(attrs={'class': 'modal-input'})
    )

    class Meta:
        model = Booking
        fields = [
            'name',
            'phone',
            'service',
            'master',
            'date',
            'time',
            'comment',
        ]
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Введите имя', 'class': 'modal-input'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Введите номер телефона', 'class': 'modal-input'}),
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'modal-input'}),
            'time': forms.TimeInput(attrs={'type': 'time', 'class': 'modal-input'}),
            'comment': forms.Textarea(attrs={'placeholder': 'Оставить комментарий', 'class': 'modal-textarea', 'rows': 3}),
        }
