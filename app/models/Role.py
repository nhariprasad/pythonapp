from google.appengine.ext import ndb

class Role(ndb.Model):
	roleName = ndb.StringProperty()
	status = ndb.StringProperty()