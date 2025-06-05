from __future__ import annotations
from pydantic import BaseModel, Field
from typing import Optional
from datetime import date


class TransactionCreateSchema(BaseModel):
	date: date
	category_id: int = Field(gt=0)
	memo: Optional[str] = None
	income: int = Field(default=0, ge=0)
	expenditure: int = Field(default=0, ge=0)


class TransactionUpdateSchema(BaseModel):
	date: Optional[date] = None
	category_id: Optional[int] = None
	memo: Optional[str] = None
	income: Optional[int] = Field(None, ge=0)
	expenditure: Optional[int] = Field(None, ge=0)