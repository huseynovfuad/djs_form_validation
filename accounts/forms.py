from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User


class UserLoginForm(forms.Form):
    username = forms.CharField(max_length =120,widget = forms.TextInput(attrs={'placeholder':'Username','class':'form-control'}),label='')
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password','class':'form-control'}),label='')
    def clean(self,*args,**kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if username and password:
            user = authenticate(username = username,password=password)
            if not user:
                raise forms.ValidationError('Email or password is wrong')
            if not user.check_password(password):
                raise forms.ValidationError('Wrong password')
            if not user.is_active:
                raise forms.ValidationError("User is not active")
        return super(UserLoginForm,self).clean(*args,**kwargs)


class UserRegisterForm(forms.ModelForm):
    username = forms.CharField(max_length =120,widget = forms.TextInput)
    email = forms.EmailField(widget=forms.EmailInput)
    password1 = forms.CharField(min_length=8,max_length=30,widget = forms.PasswordInput)
    password2 = forms.CharField(widget = forms.PasswordInput)
    class Meta:
        model = User
        fields=[
            'username',
            'email',
            'password1',
            'password2'
        ]
    def clean(self,*args,**kwargs):
        email = self.cleaned_data.get('email')
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        email_qs = User.objects.filter(email = email)
        username = self.cleaned_data.get('username')
        username_qs = User.objects.filter(username=username)
        if not password1 == password2:
            raise forms.ValidationError("Passwords didn't match")
        if email_qs.exists():
            raise forms.ValidationError('This email already exists')
        if username_qs.exists():
            raise forms.ValidationError('This username already exists')
        return super(UserRegisterForm,self).clean(*args,**kwargs)

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm,self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].label = ''
        self.fields['username'].widget.attrs.update({'placeholder': 'Username','id':'username'})
        self.fields['email'].widget.attrs.update({'placeholder': 'Email','id':'email'})
        self.fields['password1'].widget.attrs.update({'placeholder': 'Password','id':'password'})
        self.fields['password2'].widget.attrs.update({'placeholder': 'Password Confirm','id':'password2'})