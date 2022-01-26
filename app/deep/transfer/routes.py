from flask import current_app as app
from flask import Blueprint, redirect, render_template, flash, request, session, url_for
import datetime

from .models import db, Transfer
from ...basic.token.models import Token
from ... utility.api import get_transfers_from, get_transfers_to

# Blueprint Configuration
transfer_bp = Blueprint(
    'transfer_bp', __name__,
    url_prefix='/transfer',
    template_folder='templates',
    static_folder='static'
)
#
@transfer_bp.route('/load', methods=['GET'])
def load():
    api = API()
    """Logged-in Load transactions"""
    tokens = Token.query.all()
    for token in tokens:
        address = token.contract.address
        ## Query transaction history from etherscan
        data = api.get_transfers_to(address.address)
        data2 = api.get_transfers_from(address.address)
        if data:
            for raw in data:
                existing_transfer = Transfer.query.filter_by(hash=raw['hash'], address_id=address.id).all()
                if existing_transfer == []:
                    transfer = Transfer(
                            blockNumber        = raw_entry(raw, 'blockNumber'),
                            timeStamp          = datetime.datetime.fromtimestamp(int(raw_entry(raw, 'timeStamp'))),
                            hash               = raw_entry(raw, 'hash'),
                            nonce              = raw_entry(raw, 'nonce'),
                            blockHash          = raw_entry(raw, 'blockHash'),
                            sender             = raw_entry(raw, 'from'),
                            to                 = raw_entry(raw, 'to'),
                            contractAddress    = raw_entry(raw, 'contractAddress'),
                            value              = raw_entry(raw, 'value'),
                            tokenName          = raw_entry(raw, 'tokenName'),
                            tokenSymbol        = raw_entry(raw, 'tokenSymbol'),
                            tokenDecimal       = raw_entry(raw, 'tokenDecimal'),
                            transactionIndex   = raw_entry(raw, 'transactionIndex'),
                            gas                = raw_entry(raw, 'gas'),
                            gasPrice           = raw_entry(raw, 'gasPrice'),
                            cumulativeGasUsed  = raw_entry(raw, 'cumulativeGasUsed'),
                            gasUsed            = raw_entry(raw, 'gasUsed'),
                            confirmations      = raw_entry(raw, 'confirmations'),
                            input              = raw_entry(raw, 'input'),
                            address_id         = address.id
                        )
                    db.session.add(transfer)
        if data2:
            for raw in data2:
                existing_transfer = Transfer.query.filter_by(hash=raw['hash'], address_id=address.id).all()
                if existing_transfer == []:
                    transfer = Transfer(
                            blockNumber        = raw_entry(raw, 'blockNumber'),
                            timeStamp          = datetime.datetime.fromtimestamp(int(raw_entry(raw, 'timeStamp'))),
                            hash               = raw_entry(raw, 'hash'),
                            nonce              = raw_entry(raw, 'nonce'),
                            blockHash          = raw_entry(raw, 'blockHash'),
                            sender             = raw_entry(raw, 'from'),
                            to                 = raw_entry(raw, 'to'),
                            contractAddress    = raw_entry(raw, 'contractAddress'),
                            value              = raw_entry(raw, 'value'),
                            tokenName          = raw_entry(raw, 'tokenName'),
                            tokenSymbol        = raw_entry(raw, 'tokenSymbol'),
                            tokenDecimal       = raw_entry(raw, 'tokenDecimal'),
                            transactionIndex   = raw_entry(raw, 'transactionIndex'),
                            gas                = raw_entry(raw, 'gas'),
                            gasPrice           = raw_entry(raw, 'gasPrice'),
                            cumulativeGasUsed  = raw_entry(raw, 'cumulativeGasUsed'),
                            gasUsed            = raw_entry(raw, 'gasUsed'),
                            confirmations      = raw_entry(raw, 'confirmations'),
                            input              = raw_entry(raw, 'input'),
                            address_id         = address.id
                        )
                    db.session.add(transfer)
            db.session.commit()
    return redirect(url_for('transfer_bp.index'))

@transfer_bp.route('/', methods=['GET'])
def index():
    """Logged-in View transfers"""
    transfers = Transfer.query.all()
    return render_template(
        'index-transfers.jinja2',
        title='Flask-Login Tutorial.',
        template='transfers-template',
        body="You are now logged in!"
        )

# @transfer_bp.route('/', methods=['GET'])
# def index():
#     """Logged-in View transfers"""
#     transfers = []
#     for address in current_user.addresses:
#         ## Query transaction history from etherscan
#         txns_by_address = Transfer.query.filter_by(address_id=address.id).all()
#         transfers += txns_by_address
#     return render_template(
#         'indextransfers.jinja2',
#         title='Flask-Login Tutorial.',
#         template='transfers-template',
#         current_user=current_user,
#         body="You are now logged in!"
#         )

def raw_entry(data, target):
    return data[target] if target in data else None
