import json
from django.http import HttpResponseBadRequest, Http404
from pydantic import BaseModel, ValidationError


def parse_json(request):
	try:
		return json.loads(request.body), None
	except json.JSONDecodeError:
		return None, HttpResponseBadRequest("JSONフォーマットが不正です")

def validate_schema(payload: dict, schema: BaseModel):
	try:
		return schema.parse_obj(payload), None
	except ValidationError as e:
		return None, HttpResponseBadRequest(e.json())

def check_category_exists(session, category_id: int):
	from .sqlalchemy import CategorySQL
	if session.get(CategorySQL, category_id) is None:
		return HttpResponseBadRequest("指定されたカテゴリが存在しません")
	return None

def get_txn(session, model, pk):
	obj = session.get(model, pk)
	if obj is None:
		raise Http404(f"指定されたIDの{model.__tablename__}レコードは見つかりません。")
	return obj