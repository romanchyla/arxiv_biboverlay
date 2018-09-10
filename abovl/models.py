"""
Database models
"""

import sqlalchemy as sa
from adsmutils import get_date, UTCDateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()



class OAuthClient(Base):
    __tablename__ = 'oauth_client'
    id = sa.Column(sa.Integer, primary_key=True)
    token = sa.Column(sa.String(40))
    client_id = sa.Column(sa.String(40))
    created = sa.Column(UTCDateTime, default=get_date)
    
    def toJSON(self):
        """Returns value formatted as python dict. Oftentimes
        very useful for simple operations"""
        
        return {
            'id': self.id,
            'token': self.token,
            'client_id': self.client_id,
            'created': self.created and self.created.isoformat() or None
        }