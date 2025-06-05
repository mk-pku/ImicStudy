import json
from ..base import BaseTestCase


class DeleteTransactionTests(BaseTestCase):
	def test_delete_transaction_success(self):
		"""
		正常系
		- 削除後、GETで404が返る事を確認
		"""

		txn_id = 1
		response = self.client.delete(f"/api/transactions/{txn_id}/")
		self.assertEqual(response.status_code, 204)

		response2 = self.client.get(f"/api/transactions/{txn_id}/")
		self.assertEqual(response2.status_code, 404)
	
	def test_delete_transaction_not_found(self):
		non_existent_id = 9999
		response = self.client.delete(f"/api/transactions/{non_existent_id}/")
		self.assertEqual(response.status_code, 404)