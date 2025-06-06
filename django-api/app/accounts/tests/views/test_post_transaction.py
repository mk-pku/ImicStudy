import json
from ..base import BaseTestCase


class PostTransactionTests(BaseTestCase):
	def _post_and_assert_status(self, payload, expected_status):
		response = self.client.post(
			"/api/transactions/",
			data = json.dumps(payload),
			content_type = "application/json"
		)
		self.assertEqual(response.status_code, expected_status)
		return response

	def test_post_transaction_success(self):
		payload = {
			"date": "2025-06-01",
			"category_id": 18,
			"memo": "［テスト投稿］映画鑑賞",
			"income": 0,
			"expenditure": 2000
		}
		self._post_and_assert_status(payload, 201)
	
	def test_post_transaction_missing_field(self):
		payload = {
			"category_id": 1,
			"memo": "日付なしエラー",
			"income": 200000,
			"expenditure": 0
		}
		self._post_and_assert_status(payload, 400)
	
	def test_post_transaction_invalid_date_format(self):
		payload = {
			"date": "2025/06/30",
			"category_id": 1,
			"memo": "日付形式エラー",
			"income": 200000,
			"expenditure": 0
		}
		self._post_and_assert_status(payload, 400)
	
	def test_post_transaction_nonexistent_category(self):
		payload = {
			"date": "2025/06/30",
			"category_id": 9999,
			"memo": "カテゴリなしエラー",
			"income": 200000,
			"expenditure": 0
		}
		self._post_and_assert_status(payload, 400)