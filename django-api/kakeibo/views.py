from django.http import JsonResponse, Http404
from .sqlalchemy import SessionLocal
from .sqlalchemy import TransactionSQL


def get_transaction_by_id_sqlalchemy(request, transaction_id):
    db_session = SessionLocal()
    try:
        transaction_record = db_session.query(TransactionSQL).filter(TransactionSQL.id == transaction_id).first()

        if transaction_record is None:
            raise Http404("指定されたIDの家計簿レコードは見つかりません。")
        
        return JsonResponse(transaction_record.to_dict())
    
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
    finally:
        db_session.close()