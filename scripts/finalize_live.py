import json,re
from pathlib import Path
from genlayer_py import create_client,create_account
from genlayer_py.chains import studionet
ROOT=Path(__file__).parents[1];ENV=(ROOT.parents[3]/'accounts.env').read_text(encoding='utf-8');DEP=json.loads((ROOT/'deployment.json').read_text())
key=re.search(r'^ACCOUNT_2_GENLAYER_PRIVATE_KEY="?([^"\r\n]+)',ENV,re.M).group(1).strip();client=create_client(chain=studionet,account=create_account(account_private_key=key));tx=client.write_contract(address=DEP['contractAddress'],function_name='finalize',args=[DEP['liveRecordId']]);receipt=client.wait_for_transaction_receipt(transaction_hash=tx,status='FINALIZED',retries=180,interval=5000);assert receipt.get('status_name')=='FINALIZED';print(json.dumps({'id':DEP['liveRecordId'],'state':'VERIFIED','finalize':tx}),flush=True)
