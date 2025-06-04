from pydantic import BaseModel, Field
from datetime import date

class TransactionCreateSchema(BaseModel):
	date: date
	category_id: int = Field(gt=0)
	memo: str | None = None
	income: int = Field(default=0, ge=0)
	expenditure: int = Field(default=0, ge=0)
