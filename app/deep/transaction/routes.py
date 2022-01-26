from flask import current_app as app
from flask import Blueprint, redirect, render_template, flash, request, session, url_for
import datetime
from .models import db, Transaction
from ...utility.api import API

# Blueprint Configuration
transaction_bp = Blueprint(
    'transaction_bp', __name__,
    url_prefix='/transaction',
    template_folder='templates',
    static_folder='static'
)
#
# # """Logged-in page routes."""
# @transaction_bp.route('/load', methods=['GET'])
# def load():
#     api = API()
#     """Logged-in Load transactions"""
#     for address in current_user.addresses:
#         ## Query transaction history from etherscan
#         data = api.get_txn_history(address.address)
#         if data:
#             for raw in data:
#                 existing_transaction = Transaction.query.filter_by(hash=raw['hash'], address_id=address.id).all()
#                 if existing_transaction == []:
#                     transaction = Transaction(
#                         blockNumber        = raw_entry(raw, 'blockNumber'),
#                         timeStamp          = datetime.datetime.fromtimestamp(int(raw_entry(raw, 'timeStamp'))),
#                         hash               = raw_entry(raw, 'hash'),
#                         nonce              = raw_entry(raw, 'nonce'),
#                         blockHash          = raw_entry(raw, 'blockHash'),
#                         transactionIndex   = raw_entry(raw, 'transactionIndex'),
#                         sender             = raw_entry(raw, 'from'),
#                         to                 = raw_entry(raw, 'to'),
#                         value              = raw_entry(raw, 'value'),
#                         gas                = raw_entry(raw, 'gas'),
#                         gasPrice           = raw_entry(raw, 'gasPrice'),
#                         isError            = raw_entry(raw, 'isError'),
#                         txreceipt_status   = raw_entry(raw, 'txreceipt_status'),
#                         input              = raw_entry(raw, 'input'),
#                         contractAddress    = raw_entry(raw, 'contractAddress'),
#                         cumulativeGasUsed  = raw_entry(raw, 'cumulativeGasUsed'),
#                         gasUsed            = raw_entry(raw, 'gasUsed'),
#                         confirmations      = raw_entry(raw, 'confirmations'),
#                         address_id         = address.id
#                         )
#                     db.session.add(transaction)
#             db.session.commit()
#     return redirect(url_for('user_bp.dashboard'))

@transaction_bp.route('/', methods=['GET'])
def index():
    """Logged-in View transactions"""
        ## Query transaction history from etherscan
    transactions = Transaction.query.all()
    return render_template(
        'index-transaction.jinja2',
        title='Flask-Login Tutorial.',
        template='transactions-template',
        body="You are now logged in!"
        )


def raw_entry(data, target):
    return data[target] if target in data else None
