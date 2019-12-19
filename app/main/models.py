import uuid

from flask_sqlalchemy import BaseQuery
from sqlalchemy import Column, Boolean, Integer, String, DateTime, and_
from sqlalchemy_utils import UUIDType, PasswordType, EmailType, PhoneNumberType as PhoneType, force_auto_coercion

from app import db, lm

force_auto_coercion()


class Query(BaseQuery):

    def find_one(self, identity, include_removed=False):
        query = self.get(identity)
        if isinstance(query, Base):
            if not include_removed and query.removed_on is not None:
                query = None
        return query

    def find_all(self, include_removed=False, *criterion):
        if not include_removed:
            return self.filter(and_(Base.removed_on.isnot(None), *criterion))
        else:
            return self.filter(*criterion)

    def find_all_by(self, include_removed=False, **kwargs):
        if not include_removed:
            return self.filter(and_(Base.removed_on.isnot(None), **kwargs))
        else:
            return self.filter(and_(**kwargs))


class Base(db.Model):
    __abstract__ = True
    created_on = Column(DateTime, default=db.func.now())
    updated_on = Column(DateTime, default=db.func.now(), onupdate=db.func.now())
    removed_on = Column(DateTime)

    query_class = Query

    def create(self):
        db.session.add(self)
        db.session.commit()

    def update(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key) and key.lower() != 'uuid':
                setattr(self, key, value)
        db.session.commit()

    def delete(self):
        self.removed_on = db.func.now()
        db.session.commit()


class User(Base):
    __tablename__ = 'user'
    uuid = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
    username = Column(String(32), unique=True, nullable=False)
    password = Column(PasswordType(schemes=['pbkdf2_sha512']))
    firstname = Column(String(32), nullable=False)
    lastname = Column(String(32), nullable=False)
    email = Column(EmailType(128), nullable=False)
    phone = Column(PhoneType(), nullable=False)

    type = Column(String(32), default='')
    role = Column(String(32), default='user')
    status = Column(String(32), default='active')

    session_login = Column(Boolean, default=False)
    session_count = Column(Integer, default=0)

    def get_id(self):
        return self.uuid

    @property
    def is_active(self):
        return self.status == 'active'

    @property
    def is_anonymous(self):
        return False

    @property
    def is_authenticated(self):
        return self.session_login


@lm.user_loader
def user_loader(user_id):
    if isinstance(user_id, int):
        pass
    elif isinstance(user_id, str):
        if user_id.strip().isdigit():
            user_id = int(user_id)
        else:
            return
    else:
        return

    return User.query.get(user_id)
