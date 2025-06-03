from django.http import JsonResponse, Http404, HttpResponseBadRequest
from django.views.decorators.http import require_http_methods
from .sqlalchemy import get_session
from .sqlalchemy import TransactionSQL


@require_http_methods(["GET"])
def list_transactions(request):
    """
    TODO: 取引一覧を取得する処理
    """
    session = get_session()
    try:
        return None
    finally:
        session.close()

@require_http_methods(["GET"])
def retrieve_transactions(request, transaction_id):
    session = get_session()
    try:
        transaction_record = session.get(TransactionSQL, transaction_id)
        if transaction_record is None:
            raise Http404("指定されたIDの家計簿レコードは見つかりません。")
        return JsonResponse(transaction_record.to_dict())
    finally:
        session.close()

@require_http_methods(["POST"])
def create_transaction(request):
    """
    TODO: 新規取引を作成する処理
    """
    session = get_session()
    try:
        return None
    finally:
        session.close()

@require_http_methods(["PUT", "PATCH"])
def update_transaction(request, transaction_id):
    """
    TODO: 指定IDの取引を更新する処理
    """
    session = get_session()
    try:
        return None
    finally:
        session.close()

@require_http_methods(["DELETE"])
def delete_transaction(request, transaction_id):
    """
    TODO: 指定IDの取引を削除する処理を
    """
    session = get_session()
    try:
        return None
    finally:
        session.close()