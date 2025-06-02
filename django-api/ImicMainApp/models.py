from django.db import models

class Drug(models.Model):
	case_id = models.CharField("識別番号", max_length=11)
	report_count = models.SmallIntegerField("報告回数", null=True, blank=True)
	drug_seq = models.SmallIntegerField("医薬品連番")
	role = models.CharField("医薬品の関与", max_length=4, null=True, blank=True)
	drug_name = models.CharField("医薬品(一般名)", max_length=128, null=True, blank=True)
	product_name = models.CharField("医薬品(販売名)", max_length=128, null=True, blank=True)
	administration_route = models.CharField("投与経路", max_length=1024, null=True, blank=True)
	start_date = models.CharField("投与開始日", max_length=1024, null=True, blank=True)
	end_date = models.CharField("投与終了日", max_length=1024, null=True, blank=True)
	dose = models.CharField("投与量", max_length=1024, null=True, blank=True)
	dose_unit = models.CharField("投与単位", max_length=512, null=True, blank=True)
	frequency = models.CharField("分割投与回数", max_length=512, null=True, blank=True)
	indication = models.CharField("使用理由", max_length=768, null=True, blank=True)
	action_taken = models.CharField("医薬品の処置", max_length=256, null=True, blank=True)
	rechallenge = models.CharField("再投与による再発の有無", max_length=1024, null=True, blank=True)
	risk_category = models.CharField("リスク区分等(R3のみ)", max_length=256, null=True, blank=True)
	created_at = models.DateTimeField("作成日時", auto_now_add=True)
	updated_at = models.DateTimeField("更新日時", auto_now=True)

class Meta:
	db_table = 'drug'
	verbose_name = '医薬品情報'
	verbose_name_plural = '医薬品情報'
	unique_together = [['case_id', 'drug_seq']]

def __str__(self):
	return f"{self.case_id}_{self.drug_seq}: {self.product_name or self.drug_name}"