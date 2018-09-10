#!/usr/bin/python
# -*- coding: utf-8 -*-

from adsmutils import ADSFlask, get_date
from views import bp
from abovl.models import OAuthClient

def create_app(**config):
    """
    Create the application and return it to the user
    :return: flask.Flask application
    """

    app = AbovlADSFlask('arxiv_biboverlay', local_config=config)
    app.url_map.strict_slashes = False    
    app.register_blueprint(bp)
    return app


class AbovlADSFlask(ADSFlask):
    
    def __init__(self, *args, **kwargs):
        ADSFlask.__init__(self, *args, **kwargs)
        
        # HTTP client is provided by requests module; it handles connection pooling
        # here we just set some headers we always want to use while sending a request
        self.client.headers.update({'Authorization': 'Bearer {}'.format(self.config.get("API_TOKEN", ''))})
        
    
    def load_client(self, token):
        """Loads client entry from the database."""
        
        with self.session_scope() as session:
            t = session.query(OAuthClient).filter_by(token=token).first()
            if t:
                return t.toJSON()
            
    
    def create_client(self):
        """Calls ADS api and gets a new OAuth application
            registered."""
        
        url = '{}/v1/user/token'.format(self.config.get('API_URL'))
        self.client.get(url)