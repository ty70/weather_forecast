# 天気預報取得スクリプト

このプログラムは、気象局が提供するJSON形式のデータを利用して、指定した地域の「天候」「気温」「風速」などの予報を表示するPythonスクリプトです。

## 機能
- 地域コード(例: 130000 東京都)を指定して天候予報を取得
- 天候、風向、風速、気温を表示
- HTTPエラーやデータ解析エラーにも対応

## 実行環境
- Python 3.x
- ライブラリ: `requests`

```bash
pip install requests
```

## 使い方
```python
from weather_forecast import get_weather_forecast
get_weather_forecast("130000")  # 東京都
```

## サンプル出力
```
発表機関: 東京都地方気象台
報告日時: 2024-05-22T05:00:00+09:00

地域: 東京都
日時: 2024-05-22T06:00:00+09:00
  天気: 晴れ
  風: 北風
...
```

## 地域コードの一覧
気象局API:
[https://www.jma.go.jp/bosai/common/const/area.json](https://www.jma.go.jp/bosai/common/const/area.json)

例:
- 130000: 東京都
- 270000: 大阪府
- 010000: 北海道

## 注意
- 気象局のAPIは非公式の場合があります
- 温度は日によって有効値が変わることがあります
- 湿度は利用API内に含まれていないため、このスクリプトは表示に対応していません

## ライセンス
[MIT License](./LICENSE)

