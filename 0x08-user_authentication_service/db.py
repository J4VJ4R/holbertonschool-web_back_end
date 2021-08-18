#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound

from typing import TypeVar, Any

from user import Base
from user import User


class DB:
    """A DB class
    """
    def __init__(self):
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self):
        """Sets and gets a session
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """Saves the user to the database
        """
        user = User(email=email, hashed_password=hashed_password)
        self._session.add(user)
        self._session.commit()
        return user

    def find_user_by(self, **filters: Any) -> User:
        """Returns the first row found in the users table that matches the
        input's keywords arguments
        """
        if not User.__dict__.get(*filters):
            raise InvalidRequestError
        query = self._session.query(User).filter_by(**filters)
        if not query.first():
            raise NoResultFound
        return query.first()

    def update_user(self, user_id: int, **kwargs: Any):
        """Uses find_user_by to locate the user and then updates it with the
        attributes passed as kwargs
        """
        try:
            user = self.find_user_by(id=user_id)
            for key, val in kwargs.items():
                setattr(user, key, val)
            self._session.commit()
            return None
        except Exception:
            raise ValueError
