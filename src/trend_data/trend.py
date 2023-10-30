import plotly.express as px
import numpy as np

template_theme = "plotly_dark"

def format_data_for_plotly(data, date_key : str, kpi_list : list, dimension_list : list):
    # if dimension column, replace None with a string " " for plotly to interpret
    data[kpi_list] = data[kpi_list].replace(np.nan,0)
    # if dimension column, replace None with a string " " for plotly to interpret 
    data[dimension_list] = data[dimension_list].replace(np.nan," ")
    data = data.sort_values(by=date_key, ascending=False)
    return data

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