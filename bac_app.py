from plotly.offline import plot
import plotly.graph_objs as go
from flask import Flask, render_template, make_response, Markup

app = Flask(__name__)


@app.route('/results', methods=['GET', 'POST'])
def results():
    data = [go.Scatterpolar(
            r = [39, 28, 8, 7, 28, 39],
            theta = ['A','B','C', 'D', 'E', 'A'],
            fill = 'toself'
    )]

    layout = go.Layout(
            polar = dict(
                    radialaxis = dict(
                            visible = True,
                            range = [0, 50]
                        )
                    ),
                    showlegend = False
            )
    fig = go.Figure(data=data, layout=layout)
    my_plot_div = plot(fig, output_type='div')
    return render_template('results.html',div_placeholder=Markup(my_plot_div))

if __name__ == '__main__':
	app.run(debug=True)


