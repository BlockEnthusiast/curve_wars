from flask import current_app as app
from flask import Blueprint, render_template, redirect, url_for

from flask import Response
from flask import request

# from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
# from matplotlib.figure import Figure
# import io


# from .forms import AMMForm
from .models import  db, Contract

# Blueprint Configuration
contract_bp = Blueprint(
    'contract_bp', __name__,
    url_prefix='/contract',
    template_folder='templates',
    static_folder='static'
)

# """Logged-in page routes."""
@contract_bp.route('/', methods=['GET'])
def index():
    contracts = Contract.query.all()
    return render_template(
        'generalform.jinja2',
        title='Contract Index.',
        template='contract-index',
        body="",
        contracts = contracts
    )

#
# def new_contract(_contract):
#     found_contract = Contract.query.filter_by(contract=_contract).first()
#     if found_contract:
#         return found_contract
#     else:
#         new_contract = Contract(
#                     contract = _contract
#         )
#         db.session.add(new_contract)
#         db.session.commit()
#         return new_contract
#
#
# def new_contract_list(_contracts):
#     out_list = []
#     for addr in _contracts:
#         new_addy = new_contract(addr)
#         out_list.append(new_addy)
#     return out_list
#
#
# def get_contract(contract):
#     return Contract.query.filter(Contract.contract == contract).first()
#
#
# def get_contract_id(contract):
#     addr = get_contract(contract)
#     return addr.id
