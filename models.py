from sqlalchemy import Column, Integer, String, Text,DateTime
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class Invest_profile_tgbot(Base):
    __tablename__ = 'invest_profile_tgbot'

    user_id = Column(Integer, primary_key=True)
    last_modified = Column(DateTime)
    user_nickname = Column(String)
    otvet_1 = Column(String(3))
    otvet_2 = Column(String(3))
    otvet_3 = Column(String(3))
    otvet_4 = Column(String(3))
    otvet_5 = Column(String(3))
    otvet_6 = Column(String(3))
    otvet_7 = Column(String(3))
    otvet_8 = Column(String(3))
    otvet_9 = Column(String(3))
    invest_profile = Column(Text)