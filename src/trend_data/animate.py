import plotly.express as px

template_theme = "plotly_dark"

def get_trend_scatter_animation(data, x_axis : str, y_axis : str, date_to_animate : str, **kwargs):
    # https://plotly.com/python/line-and-scatter/
    fig = px.scatter(
        data, 
        x=x_axis, 
        y=y_axis, 
        animation_frame=date_to_animate,
        template=template_theme, 
        # color_discrete_sequence=['blue'], 
        # opacity=0.5, 
        **kwargs
        )
    return fig.show()

def get_trend_bar_animation(data, x_axis : str, y_axis : str, date_to_animate : str, **kwargs):
    # https://plotly.com/python/line-and-scatter/
    fig = px.bar(
        data, 
        x=x_axis, 
        y=y_axis, 
        animation_frame=date_to_animate,
        template=template_theme, 
        # color_discrete_sequence=['blue'], 
        # opacity=0.5, 
        **kwargs
        )
    return fig.show()