from django.core.management.base import BaseCommand
from django.db import transaction
from kakeibo.models import Category, Transaction
from datetime import date


class Command(BaseCommand):
	help = '家計簿と費目の初期データを投入します'

	def handle(self, *args, **options):
		self.stdout.write('既存のデータを削除し、初期データの投入を開始します...')

		Transaction.objects.all().delete()
		Category.objects.all().delete()

		# --- 費目データの作成 ---
		self.stdout.write('費目データを作成中...')
		categories = [
			Category(id=1, name='給料', notes='給与や賞与などの定期収入'),
			Category(id=2, name='臨時収入', notes='副業や一時的な収入'),
			Category(id=11, name='食費', notes='スーパーでの買い物や昼食代'),
			Category(id=12, name='交通費', notes='電車代、バス代、タクシー代など'),
			Category(id=13, name='通信費', notes='スマホ代、インターネット料金など'),
			Category(id=14, name='水道光熱費', notes='水道・電気・ガス代'),
			Category(id=15, name='家賃', notes='毎月の家賃'),
			Category(id=16, name='日用品', notes='ティッシュ、洗剤などの消耗品'),
			Category(id=17, name='交際費', notes='友人との食事や飲み会'),
			Category(id=18, name='趣味・娯楽', notes='書籍、映画、ゲーム、スポーツなど'),
			Category(id=19, name='医療費', notes='病院、薬局での支払い'),
		]
		Category.objects.bulk_create(categories)

		cat_salary = Category.objects.get(id=1)
		cat_extra_income = Category.objects.get(id=2)
		cat_food = Category.objects.get(id=11)
		cat_transport = Category.objects.get(id=12)
		cat_communication = Category.objects.get(id=13)
		cat_utilities = Category.objects.get(id=14)
		cat_rent = Category.objects.get(id=15)
		cat_necessities = Category.objects.get(id=16)
		cat_social = Category.objects.get(id=17)
		cat_hobby = Category.objects.get(id=18)

		# --- 家計簿データの作成 ---
		self.stdout.write('家計簿データを作成中...')
		transactions = [
			# 2025年2月のデータ
			Transaction(date=date(2025, 2, 3), category=cat_food, memo='カフェラテを購入', expenditure=380),
			Transaction(date=date(2025, 2, 5), category=cat_food, memo='昼食（日の出食堂）', expenditure=750),
			Transaction(date=date(2025, 2, 7), category=cat_transport, memo='交通系ICカードにチャージ', expenditure=3000),
			Transaction(date=date(2025, 2, 9), category=cat_social, memo='同僚との飲み会', expenditure=4500),
			Transaction(date=date(2025, 2, 10), category=cat_salary, memo='1月の給料', income=280000),
			Transaction(date=date(2025, 2, 12), category=cat_hobby, memo='技術書を購入', expenditure=3200),
			Transaction(date=date(2025, 2, 15), category=cat_food, memo='スーパーで1週間分の食材購入', expenditure=5580),
			Transaction(date=date(2025, 2, 20), category=cat_extra_income, memo='クラウドソーシングの報酬', income=15000),
			Transaction(date=date(2025, 2, 25), category=cat_utilities, memo='2月分電気代', expenditure=4800),
			Transaction(date=date(2025, 2, 26), category=cat_communication, memo='スマホ代（2月分）', expenditure=3500),
			Transaction(date=date(2025, 2, 28), category=cat_rent, memo='3月分家賃', expenditure=85000),

			# 2025年3月のデータ
			Transaction(date=date(2025, 3, 2), category=cat_necessities, memo='ドラッグストアで日用品購入', expenditure=2800),
			Transaction(date=date(2025, 3, 4), category=cat_food, memo='コンビニで昼食', expenditure=650),
			Transaction(date=date(2025, 3, 5), category=cat_transport, memo='外出時の電車代', expenditure=880),
			Transaction(date=date(2025, 3, 8), category=cat_hobby, memo='映画鑑賞', expenditure=1900),
			Transaction(date=date(2025, 3, 10), category=cat_salary, memo='2月の給料', income=280000),
			Transaction(date=date(2025, 3, 11), category=cat_food, memo='スーパーで買い物', expenditure=4200),
			Transaction(date=date(2025, 3, 15), category=cat_social, memo='友人とのランチ', expenditure=2500),
			Transaction(date=date(2025, 3, 22), category=cat_transport, memo='交通系ICカードにチャージ', expenditure=3000),
			Transaction(date=date(2025, 3, 25), category=cat_utilities, memo='3月分ガス代', expenditure=3200),
			Transaction(date=date(2025, 3, 26), category=cat_communication, memo='インターネット料金（3月分）', expenditure=4500),
			Transaction(date=date(2025, 3, 28), category=cat_rent, memo='4月分家賃', expenditure=85000),
		]
		Transaction.objects.bulk_create(transactions)

		self.stdout.write(self.style.SUCCESS('初期データの投入が完了しました。'))