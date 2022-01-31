from django import forms

class PostsForm(forms.Form):
    caption = forms.CharField(max_length=1000)
    comment = forms.CharField(max_length=1000)
    image = forms.ImageField()
    ts_schedule = forms.DateTimeField(label="Schedule Date (DD/MM/YYY HH:MM)")
    fields = ["caption", "comment", "image", "ts_schedule"]
