import json
from ..base import BaseTestCase


class CreateTransactionTests(BaseTestCase):
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