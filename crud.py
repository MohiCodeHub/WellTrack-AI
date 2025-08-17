from models import User, DailyLog
from sqlalchemy import create_engine, inspect as sa_inspect
from sqlalchemy.orm import sessionmaker
from datetime import date

DATABASE_URL = "sqlite:///./WellTracker.db"

engine = create_engine(
    DATABASE_URL,
    echo = True,
    connect_args={"check_same_thread": False}) 

SessionLocal = sessionmaker(bind = engine, autoflush = False, autocommit = False)


def delete_user(user_id : int) -> bool:
    with SessionLocal() as db:
        user = db.get(User, user_id)
        if not user:
            return False
        db.delete(user)
        db.commit()
        return True

def create_user(username : str, email : str) -> User:
    with SessionLocal() as db:
        user = User(username = username, email = email)
        db.add(user)
        db.commit()
        db.refresh(user)
        return user


def get_user(user_id : int):
    with SessionLocal() as db:
        return db.get(User,user_id)
    
def get_user_by_email(email : str):
    with SessionLocal() as db:
        user = db.query(User).filter(User.email == email)
        return user 
    
def update_username(user_id : int, username : str) -> User:
    with SessionLocal() as db:
        user = db.get(User,user_id)
        if not user:
            return None
        user.username = username
        db.commit()
        return user
    
def get_log(log_id  : int):
    with SessionLocal() as db:
        log = db.get(DailyLog, log_id)
        return log

def delete_log(log_id : int):
    with SessionLocal() as db:
        log = db.get(DailyLog, log_id)
        if not log:
            return False
        db.delete(log)
        db.commit()
        return True

#called on a daily basis to create a blank daily log
def create_log(user_id : int) -> DailyLog:
    with SessionLocal() as db:
        log = DailyLog()
        log.date = date.today()
        log.user_id = user_id
        db.add(log)
        db.commit()
        db.refresh(log)
        return log
    
def update_log(log_id : int, **kwargs) -> DailyLog:
    with SessionLocal() as db:
        log = db.get(DailyLog, log_id)
        if not log:
            return None
            
        # Build a safe whitelist of actual column names (no relationships/props)
        insp = sa_inspect(DailyLog)
        column_keys = {c.key for c in insp.mapper.column_attrs}
        # Exclude identity fields
        disallowed = {"id", "user_id"}
        allowed = column_keys - disallowed

        for key, val in kwargs.items():
            if key in allowed:
                setattr(log, key, val)
        db.commit()
        db.refresh(log)
        return log


       

        
        
        
