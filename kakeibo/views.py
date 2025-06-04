import json
from django.http import JsonResponse, Http404, HttpResponseBadRequest
from django.views import View
from pydantic import ValidationError
from .schemas import TransactionCreateSchema
from .sqlalchemy import get_session, TransactionSQL, CategorySQL


class TransactionListCreateView(View):
    """
    GET: 取引一覧を取得する
    POST: 新規取引を作成する
    """

    def get(self, request):
        session = get_session()
        try:
            transactions = (session.query(TransactionSQL).all())
            data = [txn.to_dict() for txn in transactions]
            return JsonResponse(data, safe=False)
        finally:
            session.close()

    def post(self, request):
        try:
            payload = json.loads(request.body)
        except json.JSONDecodeError:
            return HttpResponseBadRequest("JSONフォーマットが不正です")
        
        try:
            validated = TransactionCreateSchema.parse_obj(payload)
        except ValidationError as e:
            return HttpResponseBadRequest(e.json())

        session = get_session()

        try:
            if session.get(CategorySQL, validated.category_id) is None:
                return HttpResponseBadRequest("指定されたカテゴリが存在しません")
            
            new_txn = TransactionSQL(
                date = validated.date,
                category_id = validated.category_id,
                memo = validated.memo,
                income = validated.income,
                expenditure = validated.expenditure
            )
            session.add(new_txn)
            session.commit()
            session.refresh(new_txn)

            return JsonResponse(new_txn.to_dict(), status=201)
        finally:
            session.close()


class TransactionDetailView(View):
    """
    GET: 指定IDの取引を取得する
    PUT/PATCH: 指定IDの取引を更新する
    DELETE: 指定IDの取引を削除する
    """

    def get(self, request, transaction_id):
        session = get_session()
        try:
            transaction_record = session.get(TransactionSQL, transaction_id)
            if transaction_record is None:
                raise Http404("指定されたIDの家計簿レコードは見つかりません。")
            return JsonResponse(transaction_record.to_dict())
        finally:
            session.close()

    def put(self, request, transaction_id):
        session = get_session()
        try:
            return None
        finally:
            session.close()

    def patch(self, request, transaction_id):
        session = get_session()
        try:
            return None
        finally:
            session.close()

    def delete(self, request, transaction_id):
        session = get_session()
        try:
            return None
        finally:
            session.close()
