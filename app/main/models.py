from sqlalchemy import Column, Boolean, Integer, String, DateTime
from sqlalchemy_utils import PasswordType, EmailType, PhoneNumberType as PhoneType

from app import db, lm


class Base(db.Model):
    __abstract__ = True
    created_on = Column(DateTime, default=db.func.now())
    updated_on = Column(DateTime, default=db.func.now(), onupdate=db.func.now())

    def create(self):
        db.session.add(self)
        db.session.commit()

    def update(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key) and key.lower() != 'id':
                setattr(self, key, value)
        db.session.commit()


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    password = Column(PasswordType(schemes=['pbkdf2_sha512']))
    firstname = Column(String, nullable=False)
    lastname = Column(String, nullable=False)
    email = Column(EmailType(), nullable=False)
    phone = Column(PhoneType(), nullable=False)

    type = Column(String, nullable=False)
    role = Column(String, nullable=False)
    status = Column(String, nullable=False)

    authenticate = Column(Boolean, default=False)

    def get_id(self):
        return self.id

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    @property
    def is_authenticated(self):
        return self.authenticate


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
