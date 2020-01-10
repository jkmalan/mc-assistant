import uuid

from sqlalchemy import Column, Boolean, Integer, String, DateTime, and_
from sqlalchemy_utils import UUIDType, PasswordType, EmailType, force_auto_coercion

from microcenter import db, lm

force_auto_coercion()


class Base(db.Model):
    __abstract__ = True
    created_on = Column(DateTime, default=db.func.now())
    updated_on = Column(DateTime, default=db.func.now(), onupdate=db.func.now())
    removed_on = Column(DateTime)

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
    email = Column(EmailType(128), unique=True, nullable=False)
    username = Column(String(32), unique=True, nullable=False)
    password = Column(PasswordType(schemes=['pbkdf2_sha512']))
    firstname = Column(String(32), nullable=False)
    lastname = Column(String(32), nullable=False)

    role = Column(String(32), default='associate')
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
    if isinstance(user_id, str):
        user_id = uuid.UUID(user_id)

    return User.query.get(user_id)
