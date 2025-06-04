from django.test import TransactionTestCase, Client
from ..sqlalchemy import get_engine, get_session, Base, CategorySQL, TransactionSQL


class BaseTestCase(TransactionTestCase):
	@classmethod
	def setUpClass(cls):
		super().setUpClass()
		engine = get_engine()
		Base.metadata.create_all(bind=engine)

		session = get_session()
		try:
			categories = [
				CategorySQL(id=1, name="給料", notes="給与等の定期収入"),
				CategorySQL(id=18, name="趣味・娯楽", notes="映画やゲーム等"),
			]
			session.add_all(categories)
			session.commit()
		finally:
			session.close()

	def setUp(self):
		self.client = Client()
	
	def tearDown(self):
		session = get_session()
		try:
			session.query(TransactionSQL).delete()
			session.commit()
		finally:
			session.close()