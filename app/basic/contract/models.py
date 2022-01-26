from ... import db
from datetime import datetime
import markdown

class Contract(db.Model):
    id = db.Column(
        db.Integer,
        primary_key=True
    )
    abi = db.Column(
        db.Boolean,
        nullable=True,
    )
    address_id = db.Column(db.String,
                        db.ForeignKey('address.address'),
                        nullable=False
    )
    token = db.relationship(
                            "Token",
                            backref="contract",
                            lazy="select",
                            uselist=False
    )
    curve = db.relationship(
                            "CurveFinance",
                            backref="contract",
                            lazy="select",
                            uselist=False
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
