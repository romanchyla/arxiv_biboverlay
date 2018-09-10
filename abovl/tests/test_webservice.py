from flask.ext.testing import TestCase
from flask import url_for, request
import unittest
from abovl.models import Base
from abovl import app
import json
import os
from mock import mock

class TestServices(TestCase):
    '''Tests that each route is an http response'''

    def create_app(self):
        '''Start the wsgi application'''
        a = app.create_app(**{
               'SQLALCHEMY_DATABASE_URI': 'sqlite://',
               'SQLALCHEMY_ECHO': False,
               'TESTING': True,
               'PROPAGATE_EXCEPTIONS': True,
               'TRAP_BAD_REQUEST_ERRORS': True
            })
        Base.metadata.bind = a.db.session.get_bind()
        Base.metadata.create_all()
        return a


    def tearDown(self):
        unittest.TestCase.tearDown(self)
        Base.metadata.drop_all()
        self.app.db = None


    def test_date(self):
        # if you want to know the urls: print self.app.url_map
        
        r = self.client.get(url_for('abovl.token'))
        self.assertEqual(r.status_code,200)
        print r.json
        
    
        
        
if __name__ == '__main__':
  unittest.main()
