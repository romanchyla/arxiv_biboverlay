
import unittest
from abovl import app, models
import os, json
from mock import mock

class TestCase(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)
        self.app = app.AbovlADSFlask('test', local_config=\
            {
            'SQLALCHEMY_DATABASE_URI': 'sqlite:///',
            'SQLALCHEMY_ECHO': False
            })
        models.Base.metadata.bind = self.app.db.session.get_bind()
        models.Base.metadata.create_all()
    
    
    def tearDown(self):
        self.app.close_app()
        unittest.TestCase.tearDown(self)
        models.Base.metadata.drop_all()


    def test_load(self):
        app = self.app
        with app.session_scope() as session:
            session.add(models.OAuthClient(token='foo'))
            session.commit()
        
        t = app.load_client('foo')
        assert t['id'] == 1
        assert t['token'] == 'foo'
        


if __name__ == '__main__':
    unittest.main()