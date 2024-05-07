"""
When you make updates to the models in this file, you need to bring the
database into synch with it

open a terminal with the correct environment activated
type: alembic revision --autogenerate -m "Initial migration"

Then check the sql update statements in the script that was generated.
NB This is an important check, not a cursory glance!
NB They might be wrong!

When you are confident they are correct,
type: alembic upgrade head

The database is now updated to reflect this model file
"""

from website import Base
from sqlalchemy import Column, Integer, String, ForeignKey, BOOLEAN, DateTime
from sqlalchemy.sql import func, expression


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    role_id = Column(
        Integer,
        ForeignKey("roles.id", name="fk_users_roles", ondelete="CASCADE"),
        nullable=False,
    )
    name = Column(String(200), unique=False, nullable=False)
    email = Column(String(200), unique=True, nullable=False)
    failed_login_streak = Column(Integer, server_default="0")
    hashed_password = Column(String(200), unique=False, nullable=False)
    mfa_secret = Column(String(100), unique=False, nullable=True)
    mfa_secret_confirmed = Column(
        BOOLEAN, nullable=False, server_default=expression.false()
    )
    is_deleted = Column(BOOLEAN, nullable=False, server_default=expression.false())
    created_timestamp = Column(DateTime(timezone=True), server_default=func.now())
    pii_key_id = Column(Integer, index=True, nullable=False, server_default="0")
