from django.http import JsonResponse, HttpResponse
from django.views import View
from .utils import parse_json, validate_schema, check_category_exists, get_txn
from .schemas import TransactionCreateSchema
from .sqlalchemy import get_session, TransactionSQL, CategorySQL


class SessionMixin:
	def dispatch(self, request, *args, **kwargs):
		self.session = get_session()
		try:
			return super().dispatch(request, *args, **kwargs)
		finally:
			self.session.close()


class TransactionListCreateView(SessionMixin, View):
	"""
	GET: 取引一覧を取得する
	POST: 新規取引を作成する
	"""

	def get(self, request):
		transactions = (self.session.query(TransactionSQL).all())
		data = [txn.to_dict() for txn in transactions]
		return JsonResponse(data, safe=False)

	def post(self, request):
		payload, err = parse_json(request)
		if err: return err
		
		validated, err = validate_schema(payload, TransactionCreateSchema)
		if err: return err
		
		err = check_category_exists(self.session, validated.category_id)
		if err: return err
			
		new_txn = TransactionSQL(
			date = validated.date,
			category_id = validated.category_id,
			memo = validated.memo,
			income = validated.income,
			expenditure = validated.expenditure
		)

		self.session.add(new_txn)
		self.session.commit()
		self.session.refresh(new_txn)

		return JsonResponse(new_txn.to_dict(), status=201)


class TransactionDetailView(View):
	"""
	GET: 指定IDの取引を取得する
	PUT/PATCH: 指定IDの取引を更新する
	DELETE: 指定IDの取引を削除する
	"""

	def get(self, request, transaction_id):
		txn = get_txn(self.session, TransactionSQL, transaction_id)
		return JsonResponse(txn.to_dict())

	def put(self, request, transaction_id):
		payload, err = parse_json(request)
		if err: return err
		
		validated, err = validate_schema(payload, TransactionCreateSchema)
		if err: return err

		txn = get_txn(self.session, TransactionSQL, transaction_id)

		err = check_category_exists(self.session, validated.category_id)
		if err: return err
			
		txn.date = validated.date
		txn.category_id = validated.category_id
		txn.memo = validated.memo
		txn.income = validated.income
		txn.expenditure = validated.expenditure

		self.session.commit()
		self.session.refresh(txn)

		return JsonResponse(txn.to_dict(), status=200)

	def patch(self, request, transaction_id):
		payload, err = parse_json(request)
		if err: return err
		
		validated, err = validate_schema(payload, TransactionCreateSchema)
		if err: return err

		txn = get_txn(self.session, TransactionSQL, transaction_id)

		update_data = validated.dict(exclude_unset=True)

		if "category_id" in update_data:
			err = check_category_exists(self.session, update_data.category_id)
			if err: return err
		
		for field, value in update_data.items():
			setattr(txn, field, value)
			
		self.session.commit()
		self.session.refresh(txn)
		return JsonResponse(txn.to_dict(), status=200)

	def delete(self, request, transaction_id):
		txn = get_txn(self.session, TransactionSQL, transaction_id)
		self.session.delete(txn)
		self.session.commit()
		return HttpResponse(status=204)
