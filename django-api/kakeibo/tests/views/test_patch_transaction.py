import json
from ..base import BaseTestCase


class PatchTransactionTests(BaseTestCase):
	def _patch_and_assert_status(self, txn_id, payload, expected_status):
		response = self.client.patch(
			f"/api/transactions/{txn_id}/",
			data=json.dumps(payload),
			content_type="application/json"
		)
		self.assertEqual(response.status_code, expected_status)
		return response

	def test_patch_transaction_success(self):
		"""
		正常系
		"""

		txn_id = 1
		payload = {
			"memo": "PATCH - 映画鑑賞",
		}
		response = self._patch_and_assert_status(txn_id, payload, 200)

		data = response.json()
		self.assertEqual(data["id"], txn_id)
		self.assertEqual(data["memo"], "PATCH - 映画鑑賞")
	
	def test_patch_transaction_invalid_field(self):
		"""
		異常系: 無効なフィールド値を指定
		- incomeフィールドは0以上のみ有効
		"""

		txn_id = 1
		payload = {
			"income": -100
		}
		self._patch_and_assert_status(txn_id, payload, 400)
	
	def test_patch_transaction_not_found(self):
		"""
		異常系: transactionの存在しないidを指定
		"""

		non_existent_id = 8888
		payload = {
			"memo": "存在しないID"
		}
		self._patch_and_assert_status(non_existent_id, payload, 404)