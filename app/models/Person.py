from google.appengine.ext import ndb

class Person(ndb.Model):
	firstName = ndb.StringProperty()
	middleName = ndb.StringProperty()
	lastName = ndb.StringProperty()
	dateOfBirth = ndb.DateProperty()
	contact = ndb.KeyProperty(kind='Contact')