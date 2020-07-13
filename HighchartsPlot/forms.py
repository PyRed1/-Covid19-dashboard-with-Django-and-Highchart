from django import forms

class CountriesForm(forms.Form):
    countries=forms.CharField(max_length=100)


from .views import recovered
choicesList=recovered.columns

options=tuple(zip(choicesList,choicesList))
# this is a a tuple of tuples of index and countrie peers
# like this :
# (('Afghanistan', 'Afghanistan'),('Albania', 'Albania'),('Algeria', 'Algeria'),('Andorra', 'Andorra'),.....)
class myForm(forms.Form):
    
    choicesList = forms.MultipleChoiceField(choices=options)