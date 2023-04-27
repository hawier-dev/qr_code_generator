from django import forms


class MainForm(forms.Form):
    text = forms.CharField(
        label="Text to convert",
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "placeholder": "Enter text to convert",
                "rows": 5,
            }
        ),
    )
    