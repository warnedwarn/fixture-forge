# Steward remediation matrix

| Requested correction | Implementation | Verification |
| --- | --- | --- |
| Hash-pin the specification at creation | `specify` fetches the complete bounded specification and stores `spec_digest`; `record_run` refetches it and rejects any digest change. | Live record `REMEDIATION-1790254214` stores the digest shown in `network-run.json`. |
| Complete a clean lifecycle | The live record moved through `specify`, `record_run`, and permissionless `finalize` to `VERIFIED`. | All three finalized transaction hashes and the final state are recorded in `network-run.json`. |
| Separate the author from runner and challenger roles | The contract enforces distinct author, nominated runner, and designated challenger addresses. The network run used four separate addresses for author, runner, challenger, and finalizer. | Addresses are listed in `network-run.json`. They are user-controlled demo addresses; this proves address separation, not third-party authority. |
| Keep consensus deterministic | The validator decision now returns a closed verdict plus a deterministic variance code rather than free-form prose. | The corrected deployed source is byte-for-byte identical to `contracts/contract.py`; SHA-256 is in `deployment.json`. |

The public bench exposes the same corrected contract address and immutable evidence URLs. A focused surface test verifies that wiring. The current local direct-test runner cannot load this contract's legacy StudioNet SDK header, so the included direct tests are not represented as executed evidence.
