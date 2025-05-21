import requests
import argparse
import json

def get_weather_forecast(area_code):
    """
    指定したエリアコードの天気予報を取得し、天候、気温、風速、湿度を表示する。

    Parameters:
        area_code (str): 地域のエリアコード（例: '130000' は東京都）

    Returns:
        None

    Usage:
        python scripts/get_weather.py --input '130000'
    """
    # 気象庁の天気予報APIのURL
    url = f'https://www.jma.go.jp/bosai/forecast/data/forecast/{area_code}.json'

    try:
        # APIからデータを取得
        response = requests.get(url)
        response.raise_for_status()  # HTTPエラーが発生した場合、例外を発生させる
        data = response.json()

        # 天気予報の情報を抽出
        publishing_office = data[0]['publishingOffice']
        report_datetime = data[0]['reportDatetime']
        time_series = data[0]['timeSeries']

        print(f"発表機関: {publishing_office}")
        print(f"報告日時: {report_datetime}")
        print("")

        # 天気、風向、風速の情報
        weather_series = time_series[0]
        times = weather_series['timeDefines']
        areas = weather_series['areas']

        for area in areas:
            area_name = area['area']['name']
            weathers = area['weathers']
            winds = area['winds']
            print(f"地域: {area_name}")
            for i in range(len(times)):
                print(f"日時: {times[i]}")
                print(f"  天気: {weathers[i]}")
                print(f"  風: {winds[i]}")
            print("")

        # 気温の情報
        temperature_series = time_series[2]
        temp_times = temperature_series['timeDefines']
        temp_areas = temperature_series['areas']

        for area in temp_areas:
            area_name = area['area']['name']
            temps = area['temps']
            print(f"地域: {area_name}")
            for i in range(len(temp_times)):
                print(f"日時: {temp_times[i]}")
                print(f"  気温: {temps[i]}℃")
            print("")

    except requests.exceptions.RequestException as e:
        print(f"HTTPリクエストエラー: {e}")
    except KeyError as e:
        print(f"データの解析中にエラーが発生しました: {e}")
    except Exception as e:
        print(f"予期しないエラーが発生しました: {e}")

# 使用例
# 東京都のエリアコードは '130000'
# get_weather_forecast('130000')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="get weather forecast")
    parser.add_argument("--input", required=True, help="area code")
    args = parser.parse_args()

    get_weather_forecast(args.input)