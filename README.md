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

The files under `evidence/` are technical fixtures. Independence in this protocol is enforced at the signer-role boundary: the author address cannot be nominated as runner or challenger, the two review roles cannot share an address, and only the nominated runner can record the run.

## Studio coordinates

StudioNet contract: [`0xeF62CeE31C70D22D8f199ed2aB7808e2bA2F5Af8`](https://explorer-studio.genlayer.com/address/0xeF62CeE31C70D22D8f199ed2aB7808e2bA2F5Af8). Live record `REMEDIATION-1790254214` was created by `0x013A…C88A`, recorded by the separately signed nominated runner `0xAD04…1FD4`, and permissionlessly finalized by `0x412d…2E87` after its challenge window as `VERIFIED`. StudioNet reports every transaction as `FINALIZED`; the repository records the complete hashes, role addresses, stored specification digest, and deployed-source digest in `deployment.json` and `evidence/network-run.json`. The public bench is published at [warnedwarn-fixture-forge.pages.dev](https://warnedwarn-fixture-forge.pages.dev/).
