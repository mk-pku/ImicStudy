from sqlalchemy import (
	Column,
	Integer,
	String,
	Date,
	ForeignKey,
	DateTime,
	create_engine,
	func,
)
from sqlalchemy.orm import sessionmaker, declarative_base, relationship, scoped_session
from sqlalchemy.pool import StaticPool
from django.conf import settings
from datetime import date


_engine = None
_SessionLocal = None

def get_engine():
	global _engine, _SessionLocal
	if _engine is None:
		db = settings.DATABASES["default"]
		engine_name = db.get("ENGINE", "")

		if "sqlite3" in engine_name:
			DATABASE_URL = "sqlite:///:memory:"
			_engine = create_engine(
				DATABASE_URL,
				connect_args={"check_same_thread": False},
				poolclass=StaticPool,
				echo=True,
			)
		else:
			DATABASE_URL = (
				f"mysql+mysqldb://{db['USER']}:{db['PASSWORD']}"
				f"@{db['HOST']}:{db['PORT']}/{db['NAME']}?charset=utf8mb4"
			)
			_engine = create_engine(
				DATABASE_URL,
				pool_recycle=3600,
				pool_pre_ping=True,
				echo=True,
			)
		_SessionLocal = scoped_session(
			sessionmaker(autocommit=False, autoflush=False, bind=_engine)
		)
	return _engine

def get_session():
	if _SessionLocal is None:
		get_engine()
	return _SessionLocal()


Base = declarative_base()

class TimestampMixin:
	created_at = Column(DateTime, nullable=False, server_default=func.now())
	updated_at = Column(DateTime, nullable=False, server_default=func.now(), onupdate=func.now())


class CategorySQL(TimestampMixin, Base):
	__tablename__ = "費目"

	id = Column(Integer, primary_key=True, autoincrement=True)
	name = Column(String(20))
	notes = Column(String(100), nullable=True)

	transactions = relationship("TransactionSQL", back_populates="category", lazy="selectin")

	def to_dict(self):
		return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class TransactionSQL(TimestampMixin, Base):
	__tablename__ = "家計簿"

	id = Column(Integer, primary_key=True, autoincrement=True, index=True)
	date = Column(Date, nullable=False)
	category_id = Column(Integer, ForeignKey("費目.id"), nullable=False)
	memo = Column(String(100), nullable=True)
	income = Column(Integer, default=0, nullable=False)
	expenditure = Column(Integer, default=0, nullable=False)

	category = relationship("CategorySQL", back_populates="transactions", lazy="joined")

	def to_dict(self):
		data = {}
		for c in self.__table__.columns:
			value = getattr(self, c.name)
			if isinstance(value, date):
				data[c.name] = value.isoformat()
			else:
				data[c.name] = value
		return data
