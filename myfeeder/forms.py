from django.forms import ModelForm,TextInput
from myfeeder.models import FeedSource


class FeedSourceForm(ModelForm):
	#link = forms.CharField()
	class Meta:
		model = FeedSource
		fields = ['link','category']
		widgets = {'link':TextInput(attrs={'class':'form-control'})}
