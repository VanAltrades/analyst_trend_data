```
analyst_trend_data
│   .gitattributes
│   .gitignore
│   demo.ipynb
│   LICENSE
│   README.md
│
├───config
│       gcp_service_account.json
│       news_api_key.json
│
└───src
    ├───data
    │       CPIAUCSL.csv
    │       CPIAUCSL.xls
    │       en_historic_events.json
    │       text_product_data.txt
    │
    ├───ingest_data
    │   │   __init__.py
    │   │
    │   ├───api
    │   │       request.py
    │   │       __init__.py
    │   │
    │   ├───cloud
    │   │       aws.py
    │   │       azure.py
    │   │       gcp.py
    │   │       google_sheet.py
    │   │       __init__.py
    │   │
    │   ├───scraped
    │   │       beautifulsoup.py
    │   │       scrapy.py
    │   │       __init__.py
    │   │
    │   ├───structured
    │   │       files.py
    │   │       __init__.py
    │   │
    │   └───unstructured
    │           text.py
    │           __init__.py
    │
    ├───trend_data
    │       animate.py
    │       anomaly.py
    │       trend.py
    │       __init__.py
    │
    └───utils
            api_utils.py
            df_format_utils.py
            gcp_utils.py
            __init__.py
```