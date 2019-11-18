from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Stock(db.Model):
    """Class that instantiates a stock table."""

    __tablename__ = 'stocks'
    stock_id = db.Column(db.Integer, primary_key=True)
    stock_name = db.Column(db.String(250), nullable=False)

    def __repr__(self):
        """Represent stock as stock id and name."""
        return f'<Stock:{self.stock_id},{self.stock_name}>'
