import numpy as np
from plotly.offline import plot
import plotly.graph_objs as go

def compute_a(A, B, C, D, E):
    """Return filename of plot of the damped_vibration function."""
    data_a = [go.Scatterpolar(
            r = [A, B, C, D, E, A],
            theta = ['A','B','C', 'D', 'E', 'A'],
            fill = 'toself',
            fillcolor = '#BC8F8F',
            line =  dict(
            color = '#F4A460'
        )   
    )]

    layout = go.Layout(title='Ms(℃)=%9.1f' % (A),
            polar = dict(
                    radialaxis = dict(
                            visible = True,
                            range = [0, 50]
                        )
                    ),  
                    autosize=False,
                    width=500,
       			  height=500,
                    showlegend = False
            )
#    config={'showLink': False}
    fig = go.Figure(data=data_a ,layout=layout)
    my_plot_div = plot(fig, output_type='div', show_link=False,config=dict(displaylogo=False))    
    
    return my_plot_div