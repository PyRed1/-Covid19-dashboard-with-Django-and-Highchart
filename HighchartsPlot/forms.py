from django import forms

class CountriesForm(forms.Form):
    countries=forms.CharField(max_length=100)



class myForm(forms.Form):
    OPTIONS = (
        ("AUT", "Austria"),
        ("DEU", "Germany"),
        ("NLD", "Neitherlands"),
        ('MA','Morocco'),
        ('TU','Tunisia'),
        ('US','united States'),
        ('Uk','United Kingdom')
    )
    choicesList = forms.MultipleChoiceField(choices=OPTIONS)