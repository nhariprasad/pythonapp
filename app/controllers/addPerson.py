import jinja2
import logging
import os
import webapp2
from app.models.Person import Person
from app.middleware.gaesessions import get_current_session
from datetime import datetime

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader('app/templates'),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class AddPersonPage(webapp2.RequestHandler):
	def get(self):
		template_values = {}
		template = JINJA_ENVIRONMENT.get_template('addPerson.html')
		self.response.write(template.render(template_values))

	def post(self):
		firstName = self.request.get('firstName')
		middleName = self.request.get('middleName')
		lastName = self.request.get('lastName')
		dateOfBirth = str(self.request.get('dateOfBirth'))

		if(dateOfBirth):
			dob = datetime.strptime(dateOfBirth, '%Y-%m-%d').date() #Dates are of type: 2014-03-22
		else:
			dob = None

		person = Person(firstName = firstName, middleName = middleName, lastName = lastName, dateOfBirth = dob)
		person_key = person.put()

		session = get_current_session()
		session['person_key'] = person_key

		session['firstName'] = firstName
		session['middleName'] = middleName
		session['lastName'] = lastName
		session['dateOfBirth'] = dateOfBirth

		self.redirect('/addContact')