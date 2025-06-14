# Weather Forecast Retrieval Script

This Python script retrieves weather forecasts using JSON data provided by the Japan Meteorological Agency. It displays information such as weather conditions, temperature, and wind speed for a specified region.

## Features

* Retrieves weather forecasts by specifying a region code (e.g., 130000 for Tokyo)
* Displays weather conditions, wind direction, wind speed, and temperature
* Handles HTTP errors and data parsing errors gracefully

## Environment

* Python 3.x
* Required library: `requests`

```bash
pip install requests
```

## Usage

```bash
python scripts/get_weather_forecast.py --input "130000"  # Tokyo
```

## Sample Output

```
Issuing Agency: Tokyo District Meteorological Observatory
Report Date and Time: 2024-05-22T05:00:00+09:00

Region: Tokyo
Date and Time: 2024-05-22T06:00:00+09:00
  Weather: Sunny
  Wind: North wind
...
```

## Region Code List

Japan Meteorological Agency API:
[https://www.jma.go.jp/bosai/common/const/area.json](https://www.jma.go.jp/bosai/common/const/area.json)

Examples:

* 130000: Tokyo
* 270000: Osaka
* 010000: Hokkaido

## Notes

* The Japan Meteorological Agency API may be unofficial
* Temperature values may vary by day
* Humidity is not included in the API data and therefore not displayed by this script

## License

[MIT License](./LICENSE)
