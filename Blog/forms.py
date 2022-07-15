from django import forms
from Blog.models import Blog

class BlogForm(forms.ModelForm):
    title = forms.CharField(label='Topic',
                            widget = forms.TextInput(attrs=
                                {
                                "placeholder" : "Enter a Topic here"
                                }))
    description = forms.CharField( widget=forms.Textarea(attrs=
                                 {
                                    "placeholder": "Enter a Topic here",
                                     "rows" : 20,
                                     "cols" : 50
                                 }))
    class Meta:
        model = Blog
        fields = "__all__"

