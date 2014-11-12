from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from myfeeder.forms import FeedSourceForm
from myfeeder.models import FeedSource
import feedparser
from time import mktime
from datetime import datetime

# Create your views here.

def addsource(request):
	if request.method == 'POST':
		addsourceForm = FeedSourceForm(request.POST)
		if addsourceForm.is_valid():
			cd = addsourceForm.cleaned_data
			print 'the feed link is: ' + cd['link']
			print 'the category is: ' + cd['category'].title
			fetchFeedAndStore(cd)
	else:
		addsourceForm = FeedSourceForm()
	return render(request,'myfeeder/add_source.html',{'form':addsourceForm})

def fetchFeedAndStore(formdata):
	myfeed = feedparser.parse(formdata['link'])
	feed_title = ''
	feed_link = ''
	feed_description = ''
	feed_category = None
	feed_updated = None
	if myfeed:
		if myfeed.feed.title:
			print 'Feed title: ' + myfeed.feed.title
			feed_title = myfeed.feed.title
		if myfeed.feed.link:	
			feed_link = myfeed.feed.link
		if myfeed.feed.description:
			feed_description = myfeed.feed.description
		if formdata['category']:
			feed_category = formdata['category']
		if myfeed.feed.updated_parsed:
			feed_updated = datetime.fromtimestamp(mktime(myfeed.feed.updated_parsed))

		oneFeed = FeedSource(title=feed_title,link=feed_link,description=feed_description,updated_on=feed_updated,category=feed_category)
		oneFeed.save()
		print 'FeedSource saved successfully'
		return HttpResponseRedirect('/myfeeder/home')
	
def feedhome(request):
	feeds = FeedSource.objects.all()
	firstFeedEntries = []
	if len(feeds)>0:
		firstFeed = feeds[0]
		firstFeedEntries = get_feed_entries(firstFeed.title)
		if len(firstFeedEntries) > 0:
			paginator = Paginator(firstFeedEntries,10)
			page = request.GET.get('page')
			print "page: " + str(page)
			feed_entries_page = []
			try:
				feed_entries_page = paginator.page(page)
			except PageNotAnInteger:
				print "in EmptyPage block"
				feed_entries_page = paginator.page(1)
			except EmptyPage:
				print "in EmptyPage block"
				feed_entries_page = paginator.page(paginator.num_pages)
	return render(request,'myfeeder/feeds_home.html',{'feeds':feeds,'firstFeedEntries':feed_entries_page})
	
def feed_entries(request,parameter):
	print 'Fetching entries for feed:' + parameter
	if parameter:
		feed_entries = get_feed_entries(parameter)
		if len(feed_entries) > 0:
			paginator = Paginator(feed_entries,10)
			page = request.GET.get('page')
			print "page: " + str(page)
			feed_entries_page = []
			try:
				feed_entries_page = paginator.page(page)
			except PageNotAnInteger:
				print "in EmptyPage block"
				feed_entries_page = paginator.page(1)
			except EmptyPage:
				print "in EmptyPage block"
				feed_entries_page = paginator.page(paginator.num_pages)
			return render(request,'myfeeder/feed_entries.html',{'feedtitle':parameter,'entries':feed_entries_page})
		else:
			return HttpResponse("No entries in the feed")

def get_feed_entries(feedName):
	feed_source_obj = FeedSource.objects.get(title=feedName)
	if feed_source_obj:
		d = feedparser.parse(feed_source_obj.link)
		if d.entries:
			return d.entries
		else:
			return []
