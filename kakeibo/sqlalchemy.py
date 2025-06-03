from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey, DateTime
from sqlalchemy.orm import sessionmaker, declarative_base
from django.conf import settings
from django.utils import timezone
from datetime import date


db_settings = settings.DATABASES['default']
DB_USER = db_settings['USER']
DB_PASSWORD = db_settings['PASSWORD']
DB_HOST = db_settings['HOST']
DB_PORT = db_settings['PORT']
DB_NAME = db_settings['NAME']

DATABASE_URL = f"mysql+mysqldb://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}?charset=utf8mb4"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class CategorySQL(Base):
	__tablename__ = "費目"

	id = Column(Integer, primary_key=True)
	name = Column(String(20))
	notes = Column(String(100), nullable=True)

	def to_dict(self):
		return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class TransactionSQL(Base):
	__tablename__ = "家計簿"

	id = Column(Integer, primary_key=True, index=True, autoincrement=True)
	date = Column(Date, nullable=False)
	category_id = Column(Integer, ForeignKey("費目.id"))
	memo = Column(String(100), nullable=True)
	income = Column(Integer, default=0)
	expenditure = Column(Integer, default=0)
	created_at = Column(DateTime, default=timezone.now)
	updated_at = Column(DateTime, default=timezone.now, onupdate=timezone.now)

	def to_dict(self):
		data = {}
		for c in self.__table__.columns:
			value = getattr(self, c.name)
			if isinstance(value, date):
				data[c.name] = value.isoformat()
			else:
				data[c.name] = value
		return data
