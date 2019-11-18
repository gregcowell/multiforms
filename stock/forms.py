from flask_wtf import FlaskForm
from wtforms import SubmitField, TextField, IntegerField
from wtforms.validators import DataRequired


class ModifyStockForm(FlaskForm):
    """Modify stock form."""

    stock_id = IntegerField('ID:', validators=[DataRequired()])
    stock_name = TextField('Name:', validators=[DataRequired()])
    modify = SubmitField('Modify')
    delete = SubmitField('Delete')
