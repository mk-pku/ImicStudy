from datetime import date
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

			transactions = [
				TransactionSQL(
					date=date(2025, 6, 1),
					category_id=1,
					memo="Base - 趣味・娯楽1",
					income=0,
					expenditure=5000
				),
				TransactionSQL(
					date=date(2025, 6, 2),
					category_id=18,
					memo="Base - 給料1",
					income=300000,
					expenditure=0
				),
			]
			session.add_all(transactions)
			session.commit()
		finally:
			session.close()
	
	@classmethod
	def tearDownClass(cls):
		engine = get_engine()
		Base.metadata.drop_all(bind=engine)
		super().tearDownClass()

	def setUp(self):
		self.client = Client()
