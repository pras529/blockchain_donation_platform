from flask import request, jsonify
from . import app, db
from .models import User, Donation, Project
from .blockchain import create_donation_transaction, get_transaction_receipt
from .smart_contracts import deploy_contract, release_funds


@app.route('/donate', methods=['POST'])
def donate():
    user_id = request.json['user_id']
    project_id = request.json['project_id']
    amount = request.json['amount']

    user = User.query.get(user_id)
    project = Project.query.get(project_id)

    tx_hash = create_donation_transaction(user, project, amount)

    new_donation = Donation(user_id=user_id, project_id=project_id, amount=amount, transaction_hash=tx_hash)
    db.session.add(new_donation)
    db.session.commit()

    return jsonify({"message": "Donation successful", "transaction_hash": tx_hash})


@app.route('/verify', methods=['POST'])
def verify_milestone():
    contract_address = request.json['contract_address']
    release_funds(contract_address)
    return jsonify({"message": "Funds released successfully"})
