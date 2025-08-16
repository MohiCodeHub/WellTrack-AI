from sqlalchemy import Column, Integer, Float, Date, ForeignKey, String
from sqlalchemy.orm import declarative_base, relationship

base = declarative_base()


class User(base):
    __tablename__ = "users"

    id = Column(Integer, primary_key= True, index = True)
    user_name = Column(String, unique = True, nullable = False)
    email = Column(String, unique = True, nullable = False)

    logs = relationship("DailyLog", back_populates = "user", cascade = "all, delete-orphan")


class DailyLog(base):
    __tablename__ = "DailyLog"

    id = Column(Integer, primary_key = True, index = True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable = False)

    sleep_hours = Column(Float)
    calories = Column(Float)
    workout_min = Column(Float)
    productivity_score = Column(Float)
    mood_score = Column(Float)

    date = Column(Date, nullable = False)
    
    user = relationship("User", back_populates = "logs")




