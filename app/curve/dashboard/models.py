from ... import db
from datetime import datetime
import markdown

class CurveFinance(db.Model):
    id = db.Column(
        db.Integer,
        primary_key=True
    )
    type = db.Column(
        db.String(15),
        nullable=False,
    )
    identifier = db.Column(
        db.String(30),
        nullable=False,
    )
    contract_id = db.Column(db.Integer,
                        db.ForeignKey('contract.id'),
                        nullable=False
    )
    @property
    def serialize(self):
        return {
            'id': self.id,
            'address': self.address,
            'name': self.address.name,
            'symbol': self.address.symbol,
            'abi': self.abi,
            }

    # def start_date(self):
    #     return datetime.utcfromtimestamp(self.start).strftime('%Y-%m-%d %H:%M')
    #
    # def end_date(self):
    #     return datetime.utcfromtimestamp(self.end).strftime('%Y-%m-%d %H:%M')
    #
    # def body_markdown(self):
    #     return markdown.markdown(self.body)
