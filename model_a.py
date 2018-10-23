from wtforms import Form, FloatField, validators

class InputForm_a(Form):
    A = FloatField(
        label='A', default=10.0,
        validators=[validators.InputRequired()])
    B = FloatField(
        label='B', default=0.0,
        validators=[validators.InputRequired()])
    C = FloatField(
        label='C', default=5.0,
        validators=[validators.InputRequired()])
    D = FloatField(
        label='D', default=2.0,
        validators=[validators.InputRequired()])
    E = FloatField(
        label='E', default=18.0,
        validators=[validators.InputRequired()])
