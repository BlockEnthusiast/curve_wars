from flask import current_app as app
from flask import Blueprint, render_template, redirect, url_for

from flask import Response
from flask import request

# from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
# from matplotlib.figure import Figure
# import io


# from .forms import AMMForm
from .models import  db, Token
from ..contract.models import Contract

# Blueprint Configuration
token_bp = Blueprint(
    'token_bp', __name__,
    url_prefix='/token',
    template_folder='templates',
    static_folder='static'
)

# """Logged-in page routes."""
@token_bp.route('/', methods=['GET'])
def index():
    tokens = Token.query.all()
    return render_template(
        'index-token.jinja2',
        title='Token Index.',
        template='index-token',
        body="",
        tokens = tokens
    )


def new_token(_contract):
    found_token = Token.query.filter_by(contract_id =_contract.id).first()
    if found_token:
        return found_token
    else:
        new_token = Token(
                    contract_id = _contract.id
        )
        db.session.add(new_token)
        db.session.commit()
        return new_token
#
#
# def new_token_list(_tokens):
#     out_list = []
#     for addr in _tokens:
#         new_addy = new_token(addr)
#         out_list.append(new_addy)
#     return out_list
#
#
# def get_token(token):
#     return Token.query.filter(Token.token == token).first()
#
#
# def get_token_id(token):
#     addr = get_token(token)
#     return addr.id
