from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'location', 'travel_date', 'story', 'photo']  # photo included
        labels = {
            'title': '標題',
            'location': '地點',
            'travel_date': '旅行日期',
            'story': '旅行故事',
            'photo':'照片',
        }
        widgets = {
            'travel_date': forms.DateInput(attrs={'type': 'date'}),
        }
