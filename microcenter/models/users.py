import uuid

from sqlalchemy import Column, Boolean, ForeignKey, Integer, String, DateTime, and_
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

    status = Column(String(32), default='active')

    session_login = Column(Boolean, default=False)
    session_count = Column(Integer, default=0)

    roles = db.relationship('UserRole', back_populates='user')

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

    def get_roles(self):
        user_roles = []
        for role in self.roles:
            user_roles.append(role.role_name)
        return user_roles

    def assign(self, roles):
        for role in roles:
            user_role = UserRole(user_uuid=self.uuid, role_name=role)
            db.session.add(user_role)
            db.session.commit()


class UserRole(db.Model):
    __tablename__ = 'user_role'
    user_uuid = db.Column(UUIDType(binary=False), ForeignKey('user.uuid'), primary_key=True)
    role_name = db.Column(String(32), ForeignKey('role.name'), primary_key=True)

    user = db.relationship('User', back_populates='roles')
    role = db.relationship('Role', back_populates='users')


class Role(db.Model):
    __tablename__ = 'role'
    name = Column(String(32), primary_key=True)
    rank = Column(Integer, nullable=False)

    users = db.relationship('UserRole', back_populates='role')
