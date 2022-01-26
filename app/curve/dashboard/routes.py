from flask import current_app as appC
from flask import Blueprint, render_template, redirect, url_for

from flask import Response
from flask import request


# from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
# from matplotlib.figure import Figure
# import io

from .models import db, CurveFinance
# from .forms import AMMForm
from ...basic.address.models import Address
from ...basic.contract.models import Contract
from ...basic.token.models import Token

from ...basic.address.routes import get_address
from ...basic.contract.routes import new_contract
from ...basic.token.routes import new_token

from ..deposit.interface import CurveDepositInterface

from ...data.curve.curve_address_harvest_2022_01_22 import DATA

# Blueprint Configuration
curve_dashboard_bp = Blueprint(
    'curve_dashboard_bp', __name__,
    url_prefix='/contract',
    template_folder='templates',
    static_folder='static'
)

# """Logged-in page routes."""
@curve_dashboard_bp.route('/', methods=['GET'])
def index():
    address = Address.query.all()
    contracts = Contract.query.all()
    tokens = Token.query.all()
    curve_counts = {}
    for k in ['swap', 'token', 'deposit', 'gauge', 'adapter', 'staking']:
        curve_counts[k] = CurveFinance.query.filter_by(type = k).count()
    return render_template(
        'dash-curve.jinja2',
        title='Curve Dashboard',
        template='contract-index',
        body="",
        contracts = contracts,
        curve_counts = curve_counts,
    )

# """Logged-in page routes."""
@curve_dashboard_bp.route('/load/', methods=['GET'])
def load():
    contracts = {}
    for k in DATA.keys():
        this = DATA[k]
        keys = ['swap', 'token', 'deposit', 'gauge', 'adapter', 'staking']
        name = this['name']
        symbol = this['symbol']
        for subkey in keys:
            if subkey in this.keys():
                start = len("https://etherscan.io/address/")
                address = get_address(this[subkey][start:], name, symbol)
                contract = new_contract(address)
                if subkey == 'token':
                    token = new_token(contract)
            curve = new_curve_contract(contract, subkey, k )

    return redirect(url_for('curve_dashboard_bp.index'))

# """Logged-in page routes."""
@curve_dashboard_bp.route('/load_underlying/', methods=['GET'])
def load_underlying():
    deposit_contracts = Contracts.query.filter_by(type='deposit').all()
    for contract in deposit_contracts:
        cdi = CurveDepositInterface(contract.address.address,
                                contract.address.name,
                                contract.address.symbol
        )
        underlying = []
        i = 0
        while i > 0:
            try:
                val = cdi.underlying_coins(i)
                if val:
                    new_token(new_contract(get_address(val, None, None)))
                    i += 1
                else:
                    i = -1
            except:
                i = -1
    return redirect(url_for('curve_dashboard_bp.index'))


def new_curve_contract(_contract, _type, _identifier):
    found_contract = CurveFinance.query.filter_by(contract_id =_contract.id).first()
    if found_contract:
        return found_contract
    else:

        new_curve_finance = CurveFinance(
            type = _type,
            identifier = _identifier,
            contract_id = _contract.id,
        )
        db.session.add(new_curve_finance)
        db.session.commit()
        return new_curve_finance
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
