from sqlalchemy import *
from db.databasse import Base
from datetime import datetime, timezone

class user_details(Base):
    __tablename__ = "user_details1"
    id=  Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(30))
    mail = Column(String(30))
    age= Column(Integer)
    create_by= Column(String(30))
    create_date= create_date = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))


