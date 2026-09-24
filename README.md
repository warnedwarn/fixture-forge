# Fixture Forge — a bench record

> A reproducibility claim is not a green badge. It is a frozen specimen, a declared environment, an observed output, and time for someone else to break the result.

## Drawer A: what gets frozen

The author nominates a runner and a separate challenger, then fetches and hash-pins a public specification at creation alongside the exact expected output, execution environment, and bounded challenge window. A later run refetches that specification and fails if its bytes no longer match the creation digest. The nominated runner cannot substitute a private log: the observed output and run artifact must come from two additional HTTPS origins.

## Drawer B: what the quorum examines

Validators independently fetch the specification, output, and artifact. Every source must be valid UTF-8 and no larger than 12,000 bytes. They agree on a closed `REPRODUCED` or `DIVERGED` verdict and the digest of every fetched byte sequence. The stored variance label is derived deterministically from that verdict, so harmless prose differences cannot break consensus. A leader cannot relabel the result, replace the frozen specification, or detach the verdict from its sources without failing validator comparison.

## Drawer C: how a record closes

`SPECIFIED → RUN_RECORDED → VERIFIED / FINAL_DIVERGED`

During the challenge window, only the designated challenger may attach evidence from a fourth origin. A material challenge moves the record to `CHALLENGED`; after the same deadline, anyone may close it as `FINAL_CHALLENGED`. Permissionless finalization prevents an absent author from trapping the record.

## Bench test

```bash
genvm-lint contracts/contract.py
python -m pytest -q
```

The files under `evidence/` are plainly labelled operator-created technical fixtures. They demonstrate the workflow; they are not independent real-world authorities.

## Studio coordinates

StudioNet contract: [`0xf05e56187452601F14ffec9ab2Beb66f9881e2D1`](https://explorer-studio.genlayer.com/address/0xf05e56187452601F14ffec9ab2Beb66f9881e2D1). Live record `LIVE-1789762047` was specified by the author, recorded by a separate runner, and permissionlessly finalized after its challenge window as `VERIFIED`. All three transactions finalized successfully. Exact hashes and the deployed-source digest live in `deployment.json`. The public bench is published at [warnedwarn-fixture-forge.pages.dev](https://warnedwarn-fixture-forge.pages.dev/).
