from ... import db
from datetime import datetime
import markdown

class Address(db.Model):
    address = db.Column(
        db.String(42),
        primary_key=True
    )
    name = db.Column(
        db.String(100),
        nullable=False,
    )
    symbol = db.Column(
        db.String(20),
        nullable=True,
    )
    contract = db.relationship(
                            "Contract",
                            backref="address",
                            lazy="select",
                            uselist=False
    )
    transactions = db.relationship(
                            "Transaction",
                            backref="address",
                            lazy="select",
    )
    @property
    def serialize(self):
        return {
            'address': self.address,
            'name': self.name,
            'symbol': self.symbol,
            'contract': self.contract,
            }

    # def start_date(self):
    #     return datetime.utcfromtimestamp(self.start).strftime('%Y-%m-%d %H:%M')
    #
    # def end_date(self):
    #     return datetime.utcfromtimestamp(self.end).strftime('%Y-%m-%d %H:%M')
    #
    # def body_markdown(self):
    #     return markdown.markdown(self.body)
