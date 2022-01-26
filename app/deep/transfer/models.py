from ... import db
from datetime import datetime
import markdown



sent_tokens = db.Table('sent_tokens',
    db.Column('address_id', db.String, db.ForeignKey('address.address'), primary_key=True),
    db.Column('transfer_id', db.Integer, db.ForeignKey('transfer.id'), primary_key=True)
)
received_tokens = db.Table('received_tokens',
    db.Column('address_id', db.String, db.ForeignKey('address.address'), primary_key=True),
    db.Column('transfer_id', db.Integer, db.ForeignKey('transfer.id'), primary_key=True)
)
# token_transfers = db.Table('token_transfers',
#     db.Column('token', db.Integer, db.ForeignKey('token.id'), primary_key=True),
#     db.Column('transfer', db.Integer, db.ForeignKey('transfer.id'), primary_key=True)
# )


class Transfer(db.Model):
    id = db.Column(
        db.Integer,
        primary_key=True
    )
    blockNumber = db.Column(
        db.String,
        nullable=True
    )
    timeStamp = db.Column(
        db.DateTime,
        nullable=True
    )
    hash = db.Column(
        db.String,
        nullable=True
    )
    nonce = db.Column(
        db.String,
        nullable=True
    )
    blockHash = db.Column(
        db.String,
        nullable=True
    )
    value = db.Column(
        db.String,
        nullable=True
    )
    tokenName = db.Column(
        db.String,
        nullable=True
    )
    tokenSymbol = db.Column(
        db.String,
        nullable=True
    )
    tokenDecimal = db.Column(
        db.String,
        nullable=True
    )
    transactionIndex = db.Column(
        db.String,
        nullable=True
    )
    gas = db.Column(
        db.String,
        nullable=True
    )
    gasPrice = db.Column(
        db.String,
        nullable=True
    )
    cumulativeGasUsed = db.Column(
        db.String,
        nullable=True
    )
    gasUsed = db.Column(
        db.String,
        nullable=True
    )
    confirmations = db.Column(
        db.String,
        nullable=True
    )
    input = db.Column(
        db.String,
        nullable=True
    )
    decoded_input = db.Column(
        db.String,
        nullable=True
    )
    token = db.Column(
        db.Integer,
        db.ForeignKey('token.id'),
        nullable=False
        )
    sender = db.relationship('Address',
                        secondary=sent_tokens,
                        lazy='subquery',
                        backref=db.backref('sent_tokens', lazy=True)
    )
    to = db.relationship('Address',
                        secondary=received_tokens,
                        lazy='subquery',
                        backref=db.backref('received_tokens', lazy=True)
    )
    # tokens_out = db.Column(
    #     db.Integer,
    #     nullable=True
    # )
    # tokens_in = db.Column(
    #     db.Integer,
    #     nullable=True
    # )

    @property
    def serialize(self):
        return {
            'blockNumber' : self.blockNumber,
            'timeStamp' : self.timeStamp,
            'hash' : self.hash,
            'nonce' : self.nonce,
            'blockHash' : self.blockHash,
            'from' : self.sender,
            'to' : self.to,
            'token_id' : self.token_id,
            'value' : self.value,
            'tokenName' : self.tokenName,
            'tokenSymbol' : self.tokenSymbol,
            'tokenDecimal' : self.tokenDecimal,
            'transactionIndex' : self.transactionIndex,
            'gas' : self.gas,
            'gasPrice' : self.gasPrice,
            'cumulativeGasUsed' : self.cumulativeGasUsed,
            'gasUsed' : self.gasUsed,
            'confirmations' : self.confirmations,
            'input' : self.input,
            }

    def set_decoded_input(self, _decoded_input):
        self.decoded_input = _decoded_input if _decoded_input else None
