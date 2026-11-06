from django import forms

from .models import Contest


class ContestForm(forms.ModelForm):
    class Meta:
        model = Contest
        fields = ('title', 'description', 'price', 'comment')
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'comment': forms.Textarea(attrs={'rows': 4}),
        }
        help_texts = {
            'price': 'Рекомендованная розничная цена',
        }
        labels = {
            'title': 'Название',
            'description': 'Описание',
            'price': 'Цена',
            'comment': 'Комментарий',
        }