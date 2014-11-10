from django.forms import ModelForm
from myfeeder.models import FeedSource


class FeedSourceForm(ModelForm):
	#link = forms.CharField()
	class Meta:
		model = FeedSource
		fields = ['link','category']
