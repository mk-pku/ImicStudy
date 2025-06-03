# Setup
## 環境変数の設定
下記はホストユーザの確認
```
id -u   # 現在のユーザー UID を表示
id -g   # 現在のユーザー GID を表示
```

## DBのマイグレーションと初期データ投入
```
docker-compose exec app alembic revision --autogenerate -m "initial table"  # マイグレーションファイルが存在しない場合
docker-compose exec app alembic upgrade head
docker-compose exec app python manage.py init_data
```


