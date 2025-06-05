import json
from ..base import BaseTestCase


class PutTransactionTests(BaseTestCase):
	def _put_and_assert_status(self, txn_id, payload, expected_status):
		response = self.client.put(
			f"/api/transactions/{txn_id}/",
			data=json.dumps(payload),
			content_type="application/json"
		)
		self.assertEqual(response.status_code, expected_status)
		return response

	def test_put_transaction_success(self):
		"""
		正常系
		"""

		txn_id = 1
		payload = {
			"date": "2025-06-05",
			"category_id": 18,
			"memo": "PUT - 給料2",
			"income": 1000000,
			"expenditure": 0
		}
		response = self._put_and_assert_status(txn_id, payload, 200)

		data = response.json()
		self.assertEqual(data["id"], txn_id)
		self.assertEqual(data["date"], "2025-06-05")
		self.assertEqual(data["category_id"], 18)
		self.assertEqual(data["memo"], "PUT - 給料2")
		self.assertEqual(data["income"], 1000000)
		self.assertEqual(data["expenditure"], 0)
	
	def test_put_transaction_invalid_field(self):
		"""
		異常系: dateフィールドがISO形式でない
		"""

		txn_id = 1
		payload = {
			"date": "2025/06/05",
			"category_id": 18,
			"memo": "日付形式エラー",
			"income": 1000000,
			"expenditure": 0
		}
		self._put_and_assert_status(txn_id, payload, 400)
	
	def test_put_transaction_missing_field(self):
		"""
		異常系: dateフィールド欠落
		"""

		txn_id = 1
		payload = {
			"category_id": 18,
			"memo": "日付なし",
			"income": 1000000,
			"expenditure": 0
		}
		self._put_and_assert_status(txn_id, payload, 400)

	def test_put_transaction_nonexistent_category(self):
		"""
		異常系: category_idで存在しないidを指定
		"""
		
		txn_id = 1
		payload = {
			"date": "2025-06-05",
			"category_id": 9999,
			"memo": "カテゴリなしエラー",
			"income": 1000000,
			"expenditure": 0
		}
		self._put_and_assert_status(txn_id, payload, 400)

	def test_put_transaction_not_found(self):
		"""
		異常系: transactionの存在しないidを指定
		"""

		non_existent_id = 9999
		payload = {
			"date": "2025-06-05",
			"category_id": 1,
			"memo": "存在しないID",
			"income": 1000000,
			"expenditure": 0
		}
		self._put_and_assert_status(non_existent_id, payload, 404)