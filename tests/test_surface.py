from pathlib import Path
TEXT=Path('contracts/contract.py').read_text(encoding='utf-8');PAGE=Path('docs/index.html').read_text(encoding='utf-8')
def test_surface():
 for n in ('specify','record_run','challenge','finalize','get_fixture'):assert 'def '+n in TEXT and n in PAGE
 assert 'status: "FINALIZED"' in PAGE
 assert 'id="specimenTray"' in PAGE and 'id="microscope"' in PAGE and 'id="runTape"' in PAGE
 assert 'class="desk"' not in PAGE and 'Deployment pending' not in PAGE
 assert 'CONTRACT_ADDRESS' not in PAGE and 'DEMO_SPEC_URL' not in PAGE
 assert '0xeF62CeE31C70D22D8f199ed2aB7808e2bA2F5Af8' in PAGE
 assert '5c531bc4c3a299923819c173900fc9e9e1fb2c5a' in PAGE
