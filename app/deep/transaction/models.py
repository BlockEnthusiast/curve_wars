from datetime import datetime

"""Database models."""
from ... import db


eth_sent_transactions = db.Table('eth_sent_transactions',
    db.Column('address_id', db.String, db.ForeignKey('address.address'), primary_key=True),
    db.Column('transaction_id', db.Integer, db.ForeignKey('transaction.id'), primary_key=True)
)
eth_received_transactions = db.Table('eth_received_transactions',
    db.Column('address_id', db.String, db.ForeignKey('address.address'), primary_key=True),
    db.Column('transaction_id', db.Integer, db.ForeignKey('transaction.id'), primary_key=True)
)

class Transaction(db.Model):
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
    transactionIndex = db.Column(
        db.String,
        nullable=True
    )
    value = db.Column(
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
    isError = db.Column(
        db.String,
        nullable=True
    )
    txreceipt_status = db.Column(
        db.String,
        nullable=True
    )
    input = db.Column(
        db.String,
        nullable=True
    )
    contractAddress = db.Column(
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
    decoded_input = db.Column(
        db.String,
        nullable=True
    )
    address_id = db.Column(
        db.String,
        db.ForeignKey('address.address'),
        nullable=False
    )

    sender = db.relationship('Address',
                        secondary=eth_sent_transactions,
                        lazy='subquery',
                        backref=db.backref('eth_sent_transactions', lazy=True)
    )
    to = db.relationship('Address',
                        secondary=eth_received_transactions,
                        lazy='subquery',
                        backref=db.backref('eth_received_transactions', lazy=True)
    )

    @property
    def serialize(self):
        return {
                'blockNumber' : self.blockNumber,
                'timeStamp' : self.timeStamp,
                'hash' : self.hash,
                'nonce' : self.nonce,
                'blockHash' : self.blockHash,
                'transactionIndex' : self.transactionIndex,
                'sender' : self.sender,
                'to' : self.to,
                'value' : self.value,
                'gas' : self.gas,
                'gasPrice' : self.gasPrice,
                'isError' : self.isError,
                'txreceipt_status' : self.txreceipt_status,
                'input' : self.input,
                'contractAddress' : self.contractAddress,
                'cumulativeGasUsed' : self.cumulativeGasUsed,
                'gasUsed' : self.gasUsed,
                'confirmations' : self.confirmations,
                'etherscan' : "https://etherscan.io/tx/"+str(self.hash)
            }

    def set_decoded_input(self, _decoded_input):
        self.decoded_input = _decoded_input if _decoded_input else None

    def ts(self):
        return datetime.utcfromtimestamp(self.start).strftime('%Y-%m-%d %H:%M')
