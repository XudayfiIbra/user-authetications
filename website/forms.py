from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class singUpForm(UserCreationForm):
    # Email field
    email = forms.EmailField(required=True, label="", widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Email address'
    }))
    # Frist name field
    first_name = forms.CharField(max_length=255, required=False, label="", widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Frist name'
    }))
    # Last name field
    last_name = forms.CharField(max_length=255, required=True, label="", widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Last name'
    }))

    class Meta:
        model = User
        fields = ('username', 'first_name',
                  'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(singUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].label = ''
        self.fields['username'].help_text = ''

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = ''

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = ''
        
        
# class addPost(forms.ModelForm):
#     post_title = forms.CharField(required=True, widget=forms.TextInput(
#     attrs={
#         "placeholder": "Exsample here",
#         "class": "form-control"
#     }),
#     label= 'Post title'
#     )
    
#     image = forms.CharField(required=True, widget=forms.TextInput(
#     attrs={
#         "placeholder": "Enter image url",
#         "class": "form-control"
#     }),
#     label= 'Cover image'
#     )
    
#     content = forms.CharField   (required=True, widget=forms.TextInput(
#     attrs={
#         "placeholder": "content of the Post",
#         "class": "form-control"
#     }),
#     label= 'Content'
#     )
    
#     post_published = forms.BooleanField(required=True, widget=forms.TextInput(
#     attrs={
#         "placeholder": "False is defualt",
#         "class": "form-control"
#     }),
#     label= 'Is it published'
#     )
    
#     creater = forms.CharField(required=True, widget=forms.TextInput(
#     attrs={
#         "placeholder": "who is the author",
#         "class": "form-control"
#     }),
#     label= 'Author'
#     )
    
#     class Meta:
#         model = Post
#         exclude = ('user',)
