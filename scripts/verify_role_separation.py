import json
import re
import time
from pathlib import Path

from genlayer_py import create_account, create_client
from genlayer_py.chains import studionet

ROOT = Path(__file__).parents[1]
ENV = (ROOT.parents[3] / "accounts.env").read_text(encoding="utf-8")
DEPLOYMENT = json.loads((ROOT / "deployment.json").read_text(encoding="utf-8"))


def account(slot: int):
    match = re.search(
        rf'^ACCOUNT_{slot}_GENLAYER_PRIVATE_KEY\s*=\s*"?([^"\r\n]+)', ENV, re.M
    )
    if not match:
        raise RuntimeError(f"Missing GenLayer key for account slot {slot}")
    return create_account(account_private_key=match.group(1).strip())


author = account(2)
challenger = account(4)
client = create_client(chain=studionet, account=author)
fixture_id = f"NEGATIVE-SELF-RUNNER-{int(time.time())}"
commit = DEPLOYMENT["sourceCommit"]
spec_url = (
    "https://raw.githubusercontent.com/warnedwarn/fixture-forge/"
    f"{commit}/evidence/frozen-spec.txt"
)

transaction = client.write_contract(
    address=DEPLOYMENT["contractAddress"],
    function_name="specify",
    args=[
        fixture_id,
        "Self runner rejection fixture",
        author.address,
        challenger.address,
        "Python 3.13 / UTF-8 / Linux",
        "sha256:8ed3f6ad685b959ead7022518e1af76cd816f8e8ec7ccdda1ed4018e8f2223f8",
        spec_url,
        300,
    ],
    value=0,
)
print(f"transaction={transaction}", flush=True)
receipt = client.wait_for_transaction_receipt(
    transaction_hash=transaction,
    status="FINALIZED",
    retries=180,
    interval=5000,
    full_transaction=True,
)
leader = (receipt.get("consensus_data", {}).get("leader_receipt") or [{}])[0]
result = {
    "fixtureId": fixture_id,
    "transaction": str(transaction),
    "status": receipt.get("status_name"),
    "result": receipt.get("result_name"),
    "leaderExecution": leader.get("execution_result"),
    "leaderError": leader.get("output")
    or leader.get("error")
    or leader.get("return_data"),
}
print(json.dumps(result, default=str), flush=True)

if receipt.get("status_name") != "FINALIZED":
    raise RuntimeError("Negative role-separation transaction did not finalize")
if str(leader.get("execution_result", "")).upper() == "SUCCESS":
    raise RuntimeError("Author was unexpectedly accepted as runner")
