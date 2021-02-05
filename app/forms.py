from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
import re
class SignUpForm(UserCreationForm):
    
    fno=forms.CharField(widget = forms.HiddenInput())
  
    sno=forms.CharField(widget = forms.HiddenInput())
    captcha_value=forms.IntegerField()

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2','fno', 'sno',
'captcha_value', )

    def clean(self):
        super(SignUpForm, self).clean()

        fno = self.cleaned_data.get('fno')
        sno = self.cleaned_data.get('sno')
        captcha_value = self.cleaned_data.get('captcha_value')
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        

        if fno and sno and captcha_value:
            if int(fno)+int(sno)==captcha_value:
                print(fno,sno,captcha_value,'arith')
            else:
                self._errors['captcha_value'] = self.error_class([
				'wrong captcha'])

        if password1:
            # if len(password1)<8:
            #     self._errors['password1'] = self.error_class([
			# 	'password must have 8 greater then character'])
            if re.search(r"[\w]+[0-9]+[\W]",password1):
                self._errors['password1'] = self.error_class([
				'password must contain at least 1 alphabate, number and special character'])
            
        return self.cleaned_data


class loginform(forms.Form):
    username=forms.CharField(max_length=30)
    password=forms.CharField(widget=forms.PasswordInput())

    def clean(self):
        super(loginform, self).clean()

        username=self.cleaned_data.get('username')

        password=self.cleaned_data.get('password')
        print(username,password)
        try:
            User.objects.get(username=username)
        except:
            # if not user:
                self._errors['username'] = self.error_class(["username doesn't exist"])
        
        return self.cleaned_data
        