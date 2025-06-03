from django.db import models

class Category(models.Model):
	id = models.IntegerField("ID", primary_key=True)
	name = models.CharField("名前", max_length=20)
	notes = models.CharField("備考", max_length=100, null=True, blank=True)

	class Meta:
		db_table = '費目'
		verbose_name = '費目'
		verbose_name_plural = '費目'

	def __str__(self):
		return self.name

class Transaction(models.Model):
	date = models.DateField("日付")
	category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name="費目")
	memo = models.CharField("メモ", max_length=100, null=True, blank=True)
	income = models.IntegerField("入金額", default=0)
	expenditure = models.IntegerField("出金額", default=0)
	
	class Meta:
		db_table = '家計簿'
		verbose_name = '家計簿'
		verbose_name_plural = '家計簿'

	def __str__(self):
		return f"{self.date} - {self.memo}"