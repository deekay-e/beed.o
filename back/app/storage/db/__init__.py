#!/usr/bin/env python
''' Database storage module '''


class DBStorage:
    ''' Interact with the database '''
    __engine = None
    __session = None

    def __init__():
        ''' Initialize the Database storage '''
        self.__engine = create_engine(settings.SQLALCHEMY_DATABASE_URI,
            pool_pre_ping=True)

        if settings.BEEDO_ENV == 'test':
            Base.metadata.drop_all(self.__engine)
            self.__engine = create_engine(
                f'{settings.SQLALCHEMY_DATABASE_URI}_test', pool_pre_ping=True)


