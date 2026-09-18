import json,re,secrets,time
from pathlib import Path
from genlayer_py import create_client,create_account
from genlayer_py.chains import studionet
ROOT=Path(__file__).parents[1];ENV=(ROOT.parents[3]/'accounts.env').read_text(encoding='utf-8');DEP=json.loads((ROOT/'deployment.json').read_text())
def v(n):return re.search(rf'^{n}="?([^"\r\n]+)',ENV,re.M).group(1).strip()
def wait(c,h):
 r=c.wait_for_transaction_receipt(transaction_hash=h,status='FINALIZED',retries=180,interval=5000);assert r.get('status_name')=='FINALIZED';return r
owner=create_account(account_private_key=v('ACCOUNT_2_GENLAYER_PRIVATE_KEY'));runner=create_account(account_private_key='0x'+secrets.token_hex(32));challenger=create_account(account_private_key='0x'+secrets.token_hex(32));co=create_client(chain=studionet,account=owner);cr=create_client(chain=studionet,account=runner);address=DEP['contractAddress'];commit=DEP['sourceCommit'];item='LIVE-'+str(int(time.time()));spec=f'https://raw.githubusercontent.com/warnedwarn/fixture-forge/{commit}/evidence/frozen-spec.txt';output=f'https://cdn.jsdelivr.net/gh/warnedwarn/fixture-forge@{commit}/evidence/observed-output.txt';artifact=f'https://github.com/warnedwarn/fixture-forge/raw/{commit}/evidence/run-artifact.txt';a=co.write_contract(address=address,function_name='specify',args=[item,'Canonical UTF-8 parser fixture',runner.address,challenger.address,'Python 3.13 / UTF-8 / Linux','sha256:8ed3f6ad685b959ead7022518e1af76cd816f8e8ec7ccdda1ed4018e8f2223f8',spec,300]);wait(co,a);b=cr.write_contract(address=address,function_name='record_run',args=[item,output,artifact]);wait(cr,b);print(json.dumps({'id':item,'state':'RUN_RECORDED','specify':a,'record_run':b,'runner':runner.address,'challenger':challenger.address}),flush=True)
