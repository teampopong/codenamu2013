#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

import webapp2


class MainPage(webapp2.RequestHandler):

    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Hello, World!')


application = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
