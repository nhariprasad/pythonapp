import jinja2
import os
import webapp2

from app.controllers import *
from google.appengine.ext.webapp.util import run_wsgi_app

app = webapp2.WSGIApplication([
		('/', IndexPage),
		('/about', AboutPage),
		('/addPerson', AddPersonPage),
		('/addContact', AddContactPage),
	], debug = True)

def main():
	run_wsgi_app(app)

if __name__ == '__main__':
	main()