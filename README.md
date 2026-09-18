# Fixture Forge — a bench record

> A reproducibility claim is not a green badge. It is a frozen specimen, a declared environment, an observed output, and time for someone else to break the result.

## Drawer A: what gets frozen

The author nominates a runner and a separate challenger, then seals a public specification, the exact expected output, the execution environment, and a bounded challenge window. The nominated runner cannot substitute a private log: the observed output and run artifact must come from two additional HTTPS origins.

## Drawer B: what the quorum examines

Validators independently fetch the specification, output, and artifact. They agree on a closed `REPRODUCED` or `DIVERGED` verdict, a bounded variance note, and the digest of every fetched byte sequence. A leader cannot relabel the result or detach it from its sources without failing validator comparison.

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

Deployment coordinates and finalized lifecycle transactions are recorded in `deployment.json` after the exact reviewed source is published.
