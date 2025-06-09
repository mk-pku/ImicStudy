# Setup
## 環境変数の設定
下記はホストユーザの確認
```
id -u   # 現在のユーザー UID を表示
id -g   # 現在のユーザー GID を表示
```

# テスト
```
docker-compose exec app ./gradlew test --tests --info "com.example.api.controller.<クラス名>"
```