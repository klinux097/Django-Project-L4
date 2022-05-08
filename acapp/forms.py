from django import forms
class AcForm(forms.Form):
	num = forms.FloatField(label="Enter Number",widget=forms.NumberInput(attrs={"placeholder":"Enter the Number"}) , min_value=0.1)