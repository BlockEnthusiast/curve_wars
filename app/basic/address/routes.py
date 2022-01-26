from flask import current_app as app
from flask import Blueprint, render_template, redirect, url_for

from flask import Response
from flask import request

# from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
# from matplotlib.figure import Figure
# import io


# from .forms import AMMForm
from .models import  db, Address
from ...utility.w3 import W3

# Blueprint Configuration
address_bp = Blueprint(
    'address_bp', __name__,
    url_prefix='/address',
    template_folder='templates',
    static_folder='static'
)

# """Logged-in page routes."""
@address_bp.route('/', methods=['GET'])
def index():
    addresses = Address.query.all()
    return render_template(
        'index-address.jinja2',
        title='Address Index.',
        template='index-address',
        body="",
        addresses = addresses
    )

#
def get_address(_address, _name=None, _symbol=None):
    _address = W3.checksum_address(_address)
    found_address = Address.query.filter_by(address=_address).first()
    if found_address:
        return found_address
    else:
        new_address = Address(
                    address = _address,
                    name    = _name,
                    symbol  = _symbol,
        )
        db.session.add(new_address)
        db.session.commit()
        return new_address

#
# def new_address_list(_addresses):
#     out_list = []
#     for addr in _addresses:
#         new_addy = get_address(addr)
#         out_list.append(new_addy)
#     return out_list
#
#
# def get_address(address):
#     return Address.query.filter(Address.address == address).first()
#
#
# def get_address_id(address):
#     addr = get_address(address)
#     return addr.id
