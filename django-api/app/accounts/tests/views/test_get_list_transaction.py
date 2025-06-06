import json
from ..base import BaseTestCase


class GetListTransactionTests(BaseTestCase):
	def test_get_list_transaction_success(self):
		"""
		正常系
		"""

		response = self.client.get("/api/transactions/")
		self.assertEqual(response.status_code, 200)