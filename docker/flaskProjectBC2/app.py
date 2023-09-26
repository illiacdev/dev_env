#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask, jsonify, request
import json
from textwrap import dedent
from uuid import uuid4

from blockchain import Blockchain

app = Flask(__name__)

node_identifier = str(uuid4()).replace('-', '')

blockchain = Blockchain()


@app.route('/mine', methods=['GET'])
def mine():
    last_block = blockchain.last_block
    last_proof = last_block['proof']

    proof = blockchain.proof_of_work(last_proof)

    # blockchain.new_transaction(
    #     name='0',
    #     phone='00',
    #     type1='000',
    #     type2='0000',
    #     time='0123456789' #태깅시간.
    # )

    previous_hash = blockchain.hash(last_block)
    block = blockchain.new_block(proof, previous_hash)

    response = {
        'message': 'new block forged',
        'index': block['index'],
        'transactions': block['transactions'],
        'proof': block['proof'],
        'previous_hash': block['previous_hash']
    }
    return jsonify(response), 200



@app.route('/transactions/new', methods=['POST'])
def new_transaction():
    values = request.get_json()

#     required = ['name','phone','type1','type2','time']
    required = ['type1','type2','event_time']
    # required = ['name','phone','type1','time']
    if not all(k in values for k in required):
        return 'missing values', 400

    index = blockchain.new_transaction(values['type1'], values['type2'],values['event_time'])
    # index = blockchain.new_transaction(values['name'],values['phone'], values['type1'],  values['time'])

    response = {'message': 'Transaction will be added to Block {0}'.format(index)}

    return jsonify(response), 201



@app.route('/chain', methods=['GET'])
def full_chain():
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain),
    }

    return jsonify(response), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


# In[ ]:





# In[ ]:





# In[ ]:




