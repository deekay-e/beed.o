#!/usr/bin/env python
''' BaseModel module '''
import datetime
from uuid import uuid4


class BaseModel:
    ''' The BaseModel class from which future classes will be derived '''
    def __init__():
        ''' Initialize the Base model '''
        id = Column(
            UUID(as_uuid=True), primary_key=True, index=True, default=uuid4
        )
        created_at = Column(DateTime, default=datetime.datetime.utcnow)
        updated_at = Column(
            DateTime,
            default=datetime.datetime.utcnow,
            onupdate=datetime.datetime.utcnow,
        )
