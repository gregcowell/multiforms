from flask import render_template, Blueprint, redirect, url_for
from .models import Stock, db
from .forms import ModifyStockForm

web = Blueprint('web', __name__)


@web.route('/stocks', methods=['GET', 'POST'])
def stocks():
    """Return Stocks HTML page."""
    stocks = Stock.query.all()
    forms = []
    for stock in stocks:
        form = ModifyStockForm()
        form.stock_id.default = stock.stock_id
        form.stock_name.default = stock.stock_name
        forms.append(form)

    for form in forms:
        if form.validate_on_submit():
            if form.modify.data:
                stock = Stock.query.filter_by(stock_id=form.stock_id.data).one()
                stock.stock_name = form.stock_name.data
                db.session.add(stock)
                db.session.commit()
            elif form.delete.data:
                stock = Stock.query.filter_by(stock_id=form.stock_id.data).one()
                db.session.delete(stock)
                db.session.commit()
            return redirect(url_for('.stocks'))

        form.process()  # Do this after validate_on_submit or breaks CSRF token

    return render_template('stocks.html', forms=forms, stocks=stocks)
