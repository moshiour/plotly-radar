#from plotly.offline import plot
#import plotly.graph_objs as go
from flask import Flask, render_template, request, Markup
#import plotly
from flask_bootstrap import Bootstrap

app = Flask(__name__)

Bootstrap(app)

#========for example=========
from compute_a import compute_a
from model_a import InputForm_a
#===============================

@app.route('/results/', methods=['GET', 'POST'])
def results():
    form = InputForm_a(request.form)
    if request.method == 'POST' and form.validate():
        my_plot_div = compute_a(form.A.data, form.B.data,form.C.data, 
                                form.D.data, form.E.data)
    else:
        my_plot_div = compute_a(15, 0.1, 10, 15, 20)
  
    return render_template('view_results.html',form=form, div_placeholder=Markup(my_plot_div))

if __name__ == '__main__':
	app.run(debug=True)


