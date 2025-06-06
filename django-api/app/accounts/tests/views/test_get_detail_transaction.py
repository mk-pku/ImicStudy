import json
from ..base import BaseTestCase


class GetDetailTransactionTests(BaseTestCase):
	def test_get_detail_transaction_success(self):
		"""
		正常系
		"""

		txn_id = 1
		response = self.client.get(f"/api/transactions/{txn_id}/")
		self.assertEqual(response.status_code, 200)

		data = json.loads(response.content)

		self.assertEqual(data["id"], txn_id)
		self.assertEqual(data["date"], "2025-06-01")
		self.assertEqual(data["category_id"], 1)
		self.assertEqual(data["memo"], "Base - 趣味・娯楽1")
		self.assertEqual(data["income"], 0)
		self.assertEqual(data["expenditure"], 5000)
	
	def test_get_detail_transaction_not_found(self):
		"""
		異常系: transactionの存在しないidを指定
		"""

		non_existent_id = 9999
		response = self.client.get(f"/api/transactions/{non_existent_id}/")
		self.assertEqual(response.status_code, 404)