from ... import db
from datetime import datetime
import markdown

class Token(db.Model):
    id = db.Column(
        db.Integer,
        primary_key=True
    )
    contract_id = db.Column(db.Integer,
                        db.ForeignKey('contract.id'),
                        nullable=False
    )
    transfers = db.relationship('Transfer',
                                backref='token_transferred',
                                lazy=True
    )
    @property
    def serialize(self):
        return {
            'id': self.id,
            'address': self.contract.address,
            'name': self.contract.address.name,
            'symbol': self.contract.address.symbol,
            'transfers': len(self.contract.transfers),
            }

    # def start_date(self):
    #     return datetime.utcfromtimestamp(self.start).strftime('%Y-%m-%d %H:%M')
    #
    # def end_date(self):
    #     return datetime.utcfromtimestamp(self.end).strftime('%Y-%m-%d %H:%M')
    #
    # def body_markdown(self):
    #     return markdown.markdown(self.body)
