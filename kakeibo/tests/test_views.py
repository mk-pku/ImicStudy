import json
from django.test import TestCase, Client
from ..sqlalchemy import Base, get_session, get_engine, CategorySQL, TransactionSQL


class TransactionAPITests(TestCase):
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
	
	def test_create_transaction_success(self):
		payload = {
			"date": "2025-06-01",
			"category_id": 18,
			"memo": "［テスト投稿］映画鑑賞",
			"income": 0,
			"expenditure": 2000
		}
		response = self.client.post(
			"/api/transactions/",
			data = json.dumps(payload),
			content_type = "application/json"
		)
		self.assertEqual(response.status_code, 201)
	
	def test_create_transaction_missing_field(self):
		payload = {
			"category_id": 1,
			"memo": "日付なしエラー",
			"income": 200000,
			"expenditure": 0
		}
		response = self.client.post(
			"/api/transactions/",
			data=json.dumps(payload),
			content_type="application/json"
		)
		self.assertEqual(response.status_code, 400)
	
	def test_create_transaction_invalid_date_format(self):
		payload = {
			"date": "2025/06/30",
			"category_id": 1,
			"memo": "日付形式エラー",
			"income": 200000,
			"expenditure": 0
		}
		response = self.client.post(
			"/api/transactions/",
			data=json.dumps(payload),
			content_type="application/json"
		)
		self.assertEqual(response.status_code, 400)
	
	def test_create_transaction_nonexistent_category(self):
		payload = {
			"date": "2025/06/30",
			"category_id": 9999,
			"memo": "カテゴリなしエラー",
			"income": 200000,
			"expenditure": 0
		}
		response = self.client.post(
			"/api/transactions/",
			data=json.dumps(payload),
			content_type="application/json"
		)
		self.assertEqual(response.status_code, 400)