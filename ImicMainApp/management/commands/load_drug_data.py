import pandas as pd
from django.core.management.base import BaseCommand
from ImicMainApp.models import Drug
from django.db import transaction
from django.utils import timezone


class Command(BaseCommand):
    help = 'CSVファイルから医薬品情報を読み込み、データベースに保存します'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='医薬品情報が記載されたCSVファイルのパス')
    
    @transaction.atomic
    def handle(self, *args, **options):
        csv_file_path = options['csv_file']
        chunk_size = 10000
        total_rows_processed = 0

        self.stdout.write(self.style.NOTICE(f'[1/6] 医薬品情報の読み込みを開始します...'))

        try:
            Drug.objects.all().delete()
            self.stdout.write(self.style.WARNING(f'[3/6] 既存の医薬品データを全て削除しました。'))

            for chunk_df in pd.read_csv(csv_file_path, dtype=str, chunksize=chunk_size):
                drugs_to_create = []
                current_time = timezone.now()

                for row in chunk_df.itertuples(index=False):
                    drug_instance = Drug(
                        case_id=getattr(row, '識別番号', None),
                        report_count=int(getattr(row, '報告回数')) if getattr(row, '報告回数') else None,
                        drug_seq=int(getattr(row, '医薬品連番')) if getattr(row, '医薬品連番') else None,
                        role=getattr(row, '医薬品の関与', None),
                        drug_name=getattr(row, '医薬品（一般名）', None),
                        product_name=getattr(row, '医薬品（販売名）', None),
                        administration_route=getattr(row, '経路', None),
                        start_date=getattr(row, '投与開始日', None),
                        end_date=getattr(row, '投与終了日', None),
                        dose=getattr(row, '投与量', None),
                        dose_unit=getattr(row, '投与単位', None),
                        frequency=getattr(row, '分割投与回数', None),
                        indication=getattr(row, '使用理由', None),
                        action_taken=getattr(row, '医薬品の処置', None),
                        rechallenge=getattr(row, '再投与による再発の有無', None),
                        risk_category=getattr(row, 'リスク区分等', None),
                        created_at=current_time,
                        updated_at=current_time
                    )
                    drugs_to_create.append(drug_instance)
            
                Drug.objects.bulk_create(drugs_to_create)
                total_rows_processed += len(drugs_to_create)
                self.stdout.write(self.style.NOTICE(f'  ... {total_rows_processed} 件処理完了'))
            self.stdout.write(self.style.SUCCESS(f'完了: 合計 {total_rows_processed} 件の医薬品情報を正常に登録しました。'))
        except Exception as e:
            self.stderr.write(self.style.ERROR(f'エラーが発生しました: {e}'))