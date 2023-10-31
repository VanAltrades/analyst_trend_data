# analyst_trend_data

## Data in Motion: Time Series Visualizations using Python [The Programmatic Analyst's Handbook]

In previous repositories, I have explained how analysts can build foundational infrastructure for their operational needs.

[Setting up a Python Environment and Basic Version Control using Git](https://github.com/VanAltrades/analyst-python-environment)

[Building a Data Warehouse](https://github.com/VanAltrades/analyst-data-warehouse)

[Ingesting Data Sources with Python](https://github.com/VanAltrades/analyst_ingest_data)


Analysts are tasked with finding insight from data. You will be the domain expert for in your role, but a common first step in finding meaningful insight from your data sources is to visualize that data.

Python can help you quickly and efficiently visualize time-series and categorical data. This package builds on the repository structure from [analyst_ingest_data](https://github.com/VanAltrades/analyst_ingest_data) and includes routine functions that will help analysts visualize ingested data.

This repository favors Python's [Plotly](https://plotly.com/python/basic-charts/) package for simple visualizations that are easy to modify.

Analysts should leverage this package's functionality as a routine in their exploratory and permanent reporting to gain a 10,000 ft. view of their domain, and understand where to look deeper.

## Package Structure


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

Building upon [analyst_ingest_data](https://github.com/VanAltrades/analyst_ingest_data), this package introduces a new module called trend_data.

```
    ├───trend_data
    │       animate.py
    │       anomaly.py
    │       trend.py
    │       __init__.py
```

Whether you have time-series data from csvs or your cloud database, you can use `trend.py` functions to visualize your data over time.

`anomaly.py` allows analysts to find daily data that deviates from an expected standard deviation. This logic can be modified to meet your specific needs.

Finally, `animate.py` is an extension of `trend.py` and introduces visually interesting scatter and bar chart animations over time.

For examples of this package's functionality, refer to the `demo.ipynb` file in the repository's root folder.

## Trending Data over Time

To understand how a focus metric trends over time, analysts need to know 2 steps.

1. Import that data into Python (which has been covered)
2. Plot that data in a visualization of your choice

### Single Metric Trends over Time

> example data: U.S. Federal Reserve Monthly CPI

To import the data...

```
# demo.ipynb

from src.ingest_data.structured.files import get_csv_data
cpi = get_csv_data(".\src\data\CPIAUCSL.csv") # https://fred.stlouisfed.org/series/CPIAUCSL
cpi.tail(5)
```

To visualize the CPI over time, as a line chart, run the following function:

```
# demo.ipynb

from src.trend_data.trend import get_trend_line, get_trend_bar
get_trend_line(cpi, x_axis="DATE", y_axis="CPIAUCSL", title="U.S. Federal Reserve's Monthly Consumer Price Index - Line Chart")
```

The `trend.py` file acts as a wrapper to visualize line, bar, histograms, and scatter plots. 

The functions require arguments including the Pandas DataFrame with the data, what x and y axis columns should be used, and the ability to modify your own keyword arguments based on Plotly's documentation using `**kwargs` (keyword arguments).

```
# src.trend_data.trend

def get_trend_line(data, x_axis : str, y_axis : str, **kwargs):
    # https://plotly.com/python/line-charts/
    fig = px.line(data_frame=data, x=x_axis, y=y_axis, template=template_theme, **kwargs)
    return fig.show()

def get_trend_bar(data, x_axis : str, y_axis : str, **kwargs):
    # https://plotly.com/python/bar-charts/
    fig = px.bar(data_frame=data, x=x_axis, y=y_axis, template=template_theme, **kwargs)
    return fig.show()

def get_trend_distribution(data, x_axis : list,**kwargs):
    # https://plotly.com/python/histograms/
    fig = px.histogram(
        data_frame=data, 
        x=x_axis,
        template=template_theme,
        marginal="box", 
        barmode="overlay",
        **kwargs)
    fig.update_layout(title=f"Distribution of {x_axis_metrics.title()}")
    return fig.show()

def get_trend_scatter(data, x_axis : str, y_axis : str, **kwargs):
    # https://plotly.com/python/line-and-scatter/
    fig = px.scatter(
        data, 
        x=x_axis, 
        y=y_axis, 
        template=template_theme, 
        # color_discrete_sequence=['blue'], opacity=0.5, 
        **kwargs
        )
    return fig.show()
```

Perhaps you would prefer to see a bar chart? Simply use the `get_trend_bar()` function instead.

```
# demo.ipynb

get_trend_bar(cpi, x_axis="DATE", y_axis="CPIAUCSL", title="U.S. Federal Reserve's Monthly Consumer Price Index - Bar Chart")
```

### Single Metric Trends over Time by Dimension

> example data: Historic Events

To beter breakout your analysis, analysts will want to visualize metric trends by dimension breakouts.

```
# demo.ipynb

from src.ingest_data.structured.files import get_json_data
history = get_json_data(method="custom",path=".\src\data\en_historic_events.json", orient="index")
```

Dimensions must be properly grouped to avoid erronious visualizations and reporting. For the historical dataset, I quickly group the date dimension and the categorical dimension and count event occurances.

```
# demo.ipynb

history_grouped = history_w_year.groupby(by=["year","category2"]).agg({"description":"count"})    
history_grouped.reset_index(inplace=True)
history_grouped['event_count'] = history_grouped['description']
history_grouped
```

Now this data can be visualized by date and category using the `get_trend_bar()` function previously imported.

```
# demo.ipynb

get_trend_bar(history_grouped, x_axis="year", y_axis="event_count", color="category2", title="World History Events - Dimension Grouped Bar Chart")
```

And you can uncover the distribution of one dimension value that interests you.. in this case, Asian historical events over time within the data.

```
# demo.ipynb

from src.trend_data.trend import get_trend_distribution
asia = history_grouped.loc[history_grouped['category2']=="Asia"]
get_trend_distribution(asia, "year")
```

With this high-level overview, perhaps you are interested in a subset of the categories in the data. Perhaps you are interested in comparing the distributions of the top 4 most commonly occuring categories next to one another over time.

```
history_grouped['category2'].value_counts()
```

```
top = history_grouped.loc[history_grouped["category2"].isin(["Asia","Europe","Religion","Roman Empire"])]
get_trend_distribution(top, x_axis="year",color="category2")
```

With just a few lines of code, analysts can uncover interesting trends with ease.

## Identifying Anomalies in Daily Trend Data

> example data: E-Commerce Website Analytics data

Data trending overtime holds insight that analysts should understand. 

A common request is to identify anomalies in data. 

For time-series data, the ability to detect anomalies can be very useful in alerting an organization to a noteable change.

The `anomaly.py` file contains functions that detect daily anomalies outside an expected standard deviation. 

I encourage you to add more anomaly logic where needed.

Import the Google Analytics data from a cloud database:

```
# demo.ipynb

from src.utils.gcp_utils import client
from src.ingest_data.cloud.gcp import get_bigquery_data

clickstream = get_bigquery_data(
    """
    SELECT date, sum(revenue) revenue 
    FROM `e-commerce-demo-v.summary.s_ga_organic`
    WHERE pagetype="product_page"
    GROUP BY 1
    ORDER BY 1 DESC
    """, 
    client
    )
clickstream.head()
```

And run the anomaly detector to identify days with unexpected revenue totals:

```
# demo.ipynb

from src.trend_data.anomaly import get_anomalous_records_std, get_anomaly_trend
clickstream_anomalies = get_anomalous_records_std(data = clickstream, date_key = "date", metric = "revenue")
get_anomaly_trend(clickstream_anomalies, metric = "revenue")
```

With this high-level visualization, you may notice that a certain day has extraordinarily high revenue and investigate what page performed best.

This can be accomplised simply by re-using the cloud database ingestion function and using SQL clauses to specify what you want to see:

```
# demo.ipynb

clickstream_aug_anomaly = get_bigquery_data(
    """
    SELECT entry_page, product_type, category_type, sum(revenue) revenue 
    FROM `e-commerce-demo-v.summary.s_ga_organic`
    WHERE date = "2016-10-20" and pagetype = "product_page"
    GROUP BY 1,2,3
    ORDER BY 4 DESC
    """, 
    client
    )
clickstream_aug_anomaly.head()
```

## Animating Data Over Time to Impress

> example data: E-Commerce Website Analytics data

Animations are sometimes cringy when used to often in powerpoint, but they can also provide a certain "wow" factor when presenting data.

The `animate.py` file contains ready-made functions to animate scatter and bar charts.

They are simple modifications of the original function found in `trend.py`, but can help to tell a story when used properly.

In this example, I am interested in visualizing a scatter plot displaying pagetype visits and revenue over time.

```
# demo.ipynb

from src.utils.gcp_utils import client
from src.ingest_data.cloud.gcp import get_bigquery_data

clickstream_2016_pagetypes = get_bigquery_data(
    """
    SELECT date_month, pagetype, count(entry_page) as page_count, sum(pageviews) pageviews, sum(visits) visits, sum(revenue) revenue 
    FROM `e-commerce-demo-v.summary.s_ga_organic`
    WHERE date < "2017-12-31"
    GROUP BY 1,2
    ORDER BY 1 ASC
    """, 
    client
    )
clickstream_2016_pagetypes.head()
```

To avoid Plotly errors, I fill NA values using a format function.

```
# demo.ipynb

from src.trend_data.trend import format_data_for_plotly
clickstream_2016_pagetypes_formated = format_data_for_plotly(clickstream_2016_pagetypes, date_key="date_month", kpi_list=["page_count","pageviews","visits","revenue"], dimension_list=["pagetype"])
clickstream_2016_pagetypes_formated
```

And now I can create a scatter animation which displays category performance each month.

I just need to include what date column should act as the animation keyframe and which dimensino should be the animation group.

```
# demo.ipynb

from src.trend_data.animate import get_trend_scatter_animation
get_trend_scatter_animation(clickstream_2016_pagetypes, x_axis="visits", y_axis="revenue", date_to_animate="date_month", animation_group="pagetype", color="pagetype")
```

Finally, you can animate bar charts with a single metric using the get_trend_bar_animation() function which follows similiar requirements.

```
# demo.ipynb

from src.trend_data.animate import get_trend_bar_animation
get_trend_bar_animation(clickstream_2016_pagetypes, x_axis="pagetype", y_axis="revenue", date_to_animate="date_month", animation_group="pagetype", color="pagetype")
```