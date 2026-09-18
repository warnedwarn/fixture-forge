from pathlib import Path
TEXT=Path('contracts/contract.py').read_text(encoding='utf-8');PAGE=Path('docs/index.html').read_text(encoding='utf-8')
def test_surface():
 for n in ('specify','record_run','challenge','finalize','get_fixture'):assert 'def '+n in TEXT and n in PAGE
 assert "status:'FINALIZED'" in PAGE
 assert 'id="specimenTray"' in PAGE and 'id="microscope"' in PAGE and 'id="runTape"' in PAGE
 assert 'class="desk"' not in PAGE and 'Deployment pending' not in PAGE
