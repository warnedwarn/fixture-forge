# Steward remediation matrix

| Requested correction | Implementation | Verification |
| --- | --- | --- |
| Hash-pin the specification at creation | `specify` fetches the complete bounded specification and stores `spec_digest`; `record_run` refetches it and rejects any digest change. | Live record `REMEDIATION-1790254214` stores the digest shown in `network-run.json`. |
| Complete a clean lifecycle | The live record moved through `specify`, `record_run`, and permissionless `finalize` to `VERIFIED`. | All three finalized transaction hashes and the final state are recorded in `network-run.json`. |
| Show the runner or challenger role filled independently of the author | `specify` rejects the author address in either review role and rejects a shared runner/challenger address. `record_run` then accepts only the nominated runner's signature. | StudioNet shows `specify` signed by `0x013A…C88A` and `record_run` signed by the different nominated runner `0xAD04…1FD4`; both are `FINALIZED`. A fresh negative transaction from the author attempting to nominate itself as runner finalized with validator consensus on `ERROR` and `[EXPECTED] complete independent fixture required`. Exact hashes and senders are in `network-run.json`. |
| Keep consensus deterministic | The validator decision now returns a closed verdict plus a deterministic variance code rather than free-form prose. | The corrected deployed source is byte-for-byte identical to `contracts/contract.py`; SHA-256 is in `deployment.json`. |

The public bench exposes the same corrected contract address and immutable evidence URLs. A focused surface test verifies that wiring. The signer separation above is an on-chain authorization guarantee; it does not assert any off-chain organizational affiliation. The current local direct-test runner cannot load this contract's legacy StudioNet SDK header, so the included direct tests are not represented as executed evidence.
