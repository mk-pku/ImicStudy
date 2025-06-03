# Setup
## パーミッション設定の為、ホストとコンテナのユーザを一致させる
```
echo "UID=$(id -u)" > .env
echo "GID=$(id -g)" >> .env
```

## DBのマイグレーションと初期データ投入
```
python manage.py migrate
python manage.py init_data
```


