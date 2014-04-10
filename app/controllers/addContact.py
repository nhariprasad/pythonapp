import jinja2
import logging
import os
import webapp2
from app.models.Contact import Contact
from app.middleware.gaesessions import get_current_session

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader('app/templates'),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class AddContactPage(webapp2.RequestHandler):
	def get(self):
		template_values = get_current_session().data
		template = JINJA_ENVIRONMENT.get_template('addContact.html')
		self.response.write(template.render(template_values))

	def post(self):
		addline1 = self.request.get('addline1')
		addline2 = self.request.get('addline2')
		city = self.request.get('city')
		zip = self.request.get('zip')
		mobilePhone = self.request.get('mobilePhone')

		contact = Contact(addline1 = addline1, addline2 = addline2, city = city, zip = zip, mobilePhone = mobilePhone)
		contact_key = contact.put()

		session = get_current_session()
		session['contact_key'] = contact_key
		
		session['addline1'] = addline1
		session['addline2'] = addline2
		session['city'] = city
		session['zip'] = zip
		session['mobilePhone'] = mobilePhone
