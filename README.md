# Python-PostgreSQL

## 環境構築方法
Python 3.12を使用
```
python -m venv venv
.¥venv¥Scripts¥activate
pip install --upgrade pip
pip install -r requirements.txt
```

### 主なライブラリ
- pandas：表データ処理
- openpyxl：エクセルに格納されたデータをデータベースに登録する時に利用
- seaborn：データベースから取り出したデータの可視化
- statsmodels：データベースから取り出したデータの統計解析に
- scikit-learn：データベースから取り出したデータの機械学習に
- rdkit：化学構造を取り扱う際に
- psycopg：postgreSQL用ドライバ
- sqlalchemy：データベース操作
- dotenv：データベースの認証情報を記載した.envファイルの読み込み
- streamlit：簡易的なウェブアプリを作りたい場合に
- pygwalker：tableau風のBIダッシュボードを作成したい場合に
