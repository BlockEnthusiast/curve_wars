from flask import current_app as app
from flask import Blueprint, render_template, redirect, url_for
from flask_login import current_user, login_required

from flask import Response
from flask import request

# from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
# from matplotlib.figure import Figure
# import io


# from .forms import AMMForm
# from .models import  db, Proposal
# from ..utility.api import get_curve_contracts, get_curve_contract
# from ..address.routes import new_address
# from ..choice.routes import new_choice_list
from .models import db, CurveFinance

# Blueprint Configuration
curve_contracts_bp = Blueprint(
    'curve_contracts_bp', __name__,
    url_prefix='/curve_contract',
    template_folder='templates',
    static_folder='static'
)

"""Logged-in page routes."""
@curve_contracts_bp.route('/', methods=['GET'])
# @login_required
def index():
    curve_contracts = Proposal.query.order_by(Proposal.start).all()
    return render_template(
        'index_curve_contract.jinja2',
        title='Proposal Index',
        template='curve_contract-index',
        body="",
        curve_contracts = curve_contracts
    )
#
# # """Logged-in page routes."""
# @curve_contracts_bp.route('/show/<string:curve_contract_id>', methods=['GET'])
# # @login_required
# def show(curve_contract_id):
#     curve_contract = Proposal.query.filter(Proposal.id==curve_contract_id).first()
#     return render_template(
#         'show_curve_contract.jinja2',
#         title=curve_contract.title,
#         template='curve_contract-show',
#         body="",
#         curve_contract = curve_contract
#     )
#
# # """Logged-in page routes."""
# @curve_contracts_bp.route('/<string:space_id>', methods=['GET'])
# # @login_required
# def indexspace(space_id):
#     curve_contracts = Proposal.query.filter(Proposal.space_id==space_id).all()
#     return render_template(
#         'index_curve_contract.jinja2',
#         title=space_id,
#         template='curve_contract-show',
#         body="",
#         curve_contracts = curve_contracts,
#         space_id = space_id
#     )
#
# # """Logged-in page routes."""
# @curve_contracts_bp.route('/load/<int:first>/<string:space_id>', methods=['GET'])
# # @login_required
# def load(first, space_id):
#     existing_curve_contracts = Proposal.query.filter(Proposal.space_id == space_id).all()
#     if not existing_curve_contracts:
#         print("NONE FOUND!!!!")
#         existing_curve_contracts = []
#     else:
#         print(len(existing_curve_contracts))
#     # first = 100
#     # existing_curve_contracts = []
#     new_curve_contracts = get_curve_contracts(space_id, first, len(existing_curve_contracts))
#     if len(new_curve_contracts) > 0:
#         for p in new_curve_contracts:
#             previous_entry = Proposal.query.filter(Proposal.id == p['id']).first()
#             author = new_address(p['author'])
#             if not previous_entry:
#                 new_curve_contract = Proposal(
#                     id = p['id'],
#                     title = p['title'],
#                     body = p['body'],
#                     start = p['start'],
#                     end = p['end'],
#                     snapshot = p['snapshot'],
#                     state = p['state'],
#                     author_address = author.address,
#                     space_id = p['space']['id'],
#                 )
#                 db.session.add(new_curve_contract)
#                 new_curve_contract.choices = new_choice_list(p['choices'], new_curve_contract.id)
#             else:
#                 print(p['title'])
#                 previous_entry.id = p['id'],
#                 previous_entry.title = p['title'],
#                 previous_entry.body = p['body'],
#                 previous_entry.start = p['start'],
#                 previous_entry.end = p['end'],
#                 previous_entry.snapshot = p['snapshot'],
#                 previous_entry.state = p['state'],
#                 previous_entry.author_address = author.address,
#                 previous_entry.space_id = p['space']['id'],
#                 previous_entry.author = new_address(p['author'])
#                 previous_entry.choices = new_choice_list(p['choices'], previous_entry.id)
#         db.session.commit()
#     return redirect(url_for('curve_contracts_bp.indexspace', space_id=space_id))
#
# # """Logged-in page routes."""
# @curve_contracts_bp.route('/reload/<string:curve_contract_id>', methods=['GET'])
# # @login_required
# def reload(curve_contract_id):
#     existing_curve_contract = Proposal.query.filter(Proposal.id == curve_contract_id).first()
#     refreshed_curve_contract = get_curve_contract(curve_contract_id)
#     if existing_curve_contract:
#         print(existing_curve_contract.title)
#         author = new_address(refreshed_curve_contract['author'])
#         existing_curve_contract.title = refreshed_curve_contract['title'],
#         existing_curve_contract.body = refreshed_curve_contract['body'],
#         existing_curve_contract.start = refreshed_curve_contract['start'],
#         existing_curve_contract.end = refreshed_curve_contract['end'],
#         existing_curve_contract.snapshot = refreshed_curve_contract['snapshot'],
#         existing_curve_contract.state = refreshed_curve_contract['state'],
#         existing_curve_contract.author_address = author.address,
#         existing_curve_contract.space_id = refreshed_curve_contract['space']['id'],
#         db.session.add(existing_curve_contract)
#         existing_curve_contract.choices = new_choice_list(refreshed_curve_contract['choices'], existing_curve_contract.id)
#
#         db.session.add(existing_curve_contract)
#         db.session.commit()
#     return redirect(url_for('curve_contracts_bp.show', curve_contract_id=curve_contract_id))
#
#
# def retrieve_curve_contract(curve_contract_id):
#     return Proposal.query.filter(Proposal.id == curve_contract_id).first()
