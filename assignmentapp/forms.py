from django import forms

class ContactForm(forms.Form):
    first_name = forms.CharField(label="First name",max_length=50)
    last_name = forms.CharField(label="Last name",max_length=50)
    email = forms.EmailField(label="Email")
    tel = forms.CharField(required=False)
    fax = forms.CharField(required=False)
    mob = forms.CharField(required=False)
    dob = forms.DateField(
        label="Date of Birth",
        widget=forms.DateInput(attrs={"type":"date"})

    )
    gender = forms.ChoiceField(
        choices=[("male","Male"), ("female","Female"), ("nb","Non-binary")],
        widget=forms.RadioSelect,
    )
    comment = forms.CharField(
        required=False, widget=forms.Textarea(attrs={"rows":4})
    )