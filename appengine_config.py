from app.middleware.gaesessions import SessionMiddleware

import os

COOKIE_KEY = 'adn9oy9o9kyynn9on9o98wa345654ey87y687esfy6s7d76fsd78f6sd78f'

def webapp_add_wsgi_middleware(app):
	app = SessionMiddleware(app, cookie_key=COOKIE_KEY)
	return app