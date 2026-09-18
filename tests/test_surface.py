from pathlib import Path
TEXT=Path('contracts/contract.py').read_text(encoding='utf-8');PAGE=Path('docs/index.html').read_text(encoding='utf-8')
def test_surface():
 for n in ('specify','record_run','challenge','finalize','get_fixture'):assert 'def '+n in TEXT and n in PAGE
 assert "status:'FINALIZED'" in PAGE
 assert 'id="specimenTray"' in PAGE and 'id="microscope"' in PAGE and 'id="runTape"' in PAGE
 assert 'class="desk"' not in PAGE and 'Deployment pending' not in PAGE
 assert 'CONTRACT_ADDRESS' not in PAGE and 'DEMO_SPEC_URL' not in PAGE
 assert '0xf05e56187452601F14ffec9ab2Beb66f9881e2D1' in PAGE
