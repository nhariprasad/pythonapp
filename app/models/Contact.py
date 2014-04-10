from google.appengine.ext import ndb

class Contact(ndb.Model):
	addline1 = ndb.StringProperty()
	addline2 = ndb.StringProperty()
	city = ndb.StringProperty()
	zip = ndb.StringProperty()
	mobilePhone = ndb.StringProperty()
