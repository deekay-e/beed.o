#!/usr/bin/env python
''' BaseModel module '''
from datetime import datetime
from uuid import uuid4
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

from app.storage import storage_t

time = '%Y-%m-%dT%H:%M:%S.%f'

if storage_t == 'db':
    Base = declarative_base()
else:
    Base = object


class BaseModel:
    ''' The BaseModel class from which future classes will be derived '''
    if storage_t == 'db':
        id = Column(UUID(as_uuid=True), primary_key=True, index=True,
            default=uuid4)
        created_at = Column(DateTime, default=datetime.utcnow)
        updated_at = Column(DateTime, default=datetime.utcnow,
            onupdate=datetime.utcnow)

    def __init__():
        ''' Initialize the Base model '''
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)
            if kwargs.get('created_at', None) and type(self.created_at) is str:
                self.created_at = datetime.strptime(kwargs['created_at'], time)
            else:
                self.created_at = datetime.utcnow()
            if kwargs.get('updated_at', None) and type(self.updated_at) is str:
                self.updated_at = datetime.strptime(kwargs['updated_at'], time)
            else:
                self.updated_at = datetime.utcnow()
            if kwargs.get('id', None) is None:
                self.id = str(uuid4())
        else:
            self.id = str(uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = self.created_at


