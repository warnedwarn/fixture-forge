from conftest import CONTRACT

def setup(vm,deploy,alice,bob,charlie):
 vm.warp('2035-01-01T00:00:00+00:00');vm.sender=alice;c=deploy(CONTRACT);vm.mock_web(r'spec\.example',{'status':200,'body':'input=alpha; expected=sha256:7f-demo'});c.specify('fx-7','Canonical parser fixture','0x'+bob.hex(),'0x'+charlie.hex(),'Python 3.13 / UTF-8 / Linux','sha256:7f-demo','https://spec.example/fixture',600);return c
def mocks(vm,verdict='REPRODUCED'):
 vm.mock_web(r'spec\.example',{'status':200,'body':'input=alpha; expected=sha256:7f-demo'});vm.mock_web(r'output\.example',{'status':200,'body':'sha256:7f-demo'});vm.mock_web(r'artifact\.example',{'status':200,'body':'python 3.13 utf-8 linux'});vm.mock_llm(r'.*FixtureForge reproducibility inspection.*','{"verdict":"'+verdict+'"}')

def test_reproducible_run_and_permissionless_finalization(direct_vm,direct_deploy,direct_alice,direct_bob,direct_charlie):
 c=setup(direct_vm,direct_deploy,direct_alice,direct_bob,direct_charlie);direct_vm.sender=direct_bob;mocks(direct_vm);c.record_run('fx-7','https://output.example/value','https://artifact.example/log');assert c.get_fixture('fx-7')['state']=='RUN_RECORDED';direct_vm.warp('2035-01-01T00:11:00+00:00');direct_vm.sender=direct_alice;c.finalize('fx-7');assert c.get_fixture('fx-7')['state']=='VERIFIED'
def test_only_runner_can_record(direct_vm,direct_deploy,direct_alice,direct_bob,direct_charlie):
 c=setup(direct_vm,direct_deploy,direct_alice,direct_bob,direct_charlie);mocks(direct_vm)
 with direct_vm.expect_revert('nominated runner'):c.record_run('fx-7','https://output.example/value','https://artifact.example/log')
def test_author_cannot_fill_runner_or_challenger_role(direct_vm,direct_deploy,direct_alice,direct_bob,direct_charlie):
 direct_vm.warp('2035-01-01T00:00:00+00:00');direct_vm.sender=direct_alice;c=direct_deploy(CONTRACT);direct_vm.mock_web(r'spec\.example',{'status':200,'body':'input=alpha; expected=sha256:7f-demo'})
 with direct_vm.expect_revert('complete independent fixture'):c.specify('self-run','Canonical parser fixture','0x'+direct_alice.hex(),'0x'+direct_charlie.hex(),'Python 3.13 / UTF-8 / Linux','sha256:7f-demo','https://spec.example/fixture',600)
 with direct_vm.expect_revert('complete independent fixture'):c.specify('self-challenge','Canonical parser fixture','0x'+direct_bob.hex(),'0x'+direct_alice.hex(),'Python 3.13 / UTF-8 / Linux','sha256:7f-demo','https://spec.example/fixture',600)
 with direct_vm.expect_revert('complete independent fixture'):c.specify('same-role','Canonical parser fixture','0x'+direct_bob.hex(),'0x'+direct_bob.hex(),'Python 3.13 / UTF-8 / Linux','sha256:7f-demo','https://spec.example/fixture',600)
def test_validator_rejects_forged_verdict(direct_vm,direct_deploy,direct_alice,direct_bob,direct_charlie):
 c=setup(direct_vm,direct_deploy,direct_alice,direct_bob,direct_charlie);mocks(direct_vm);x=c.fixtures['FX-7'];result=c._judge_run(x,[x.spec_url,'https://output.example/value','https://artifact.example/log']);assert direct_vm.run_validator(leader_result=result) is True;forged=dict(result);forged['verdict']='DIVERGED';assert direct_vm.run_validator(leader_result=forged) is False
def test_material_challenge_preserves_source(direct_vm,direct_deploy,direct_alice,direct_bob,direct_charlie):
 c=setup(direct_vm,direct_deploy,direct_alice,direct_bob,direct_charlie);direct_vm.sender=direct_bob;mocks(direct_vm);c.record_run('fx-7','https://output.example/value','https://artifact.example/log');direct_vm.clear_mocks();direct_vm.sender=direct_charlie;direct_vm.mock_web(r'challenge\.example',{'status':200,'body':'Output changes under the frozen environment.'});direct_vm.mock_llm(r'.*FixtureForge challenge inspection.*','{"material":true}');c.challenge('fx-7','https://challenge.example/replay');assert c.get_fixture('fx-7')['state']=='CHALLENGED' and c.get_fixture('fx-7')['challenge_digest']
def test_specification_is_hash_pinned_at_creation(direct_vm,direct_deploy,direct_alice,direct_bob,direct_charlie):
 c=setup(direct_vm,direct_deploy,direct_alice,direct_bob,direct_charlie);record=c.get_fixture('fx-7');assert len(record['spec_digest'])==64;direct_vm.clear_mocks();direct_vm.sender=direct_bob;direct_vm.mock_web(r'spec\.example',{'status':200,'body':'CHANGED specification'});direct_vm.mock_web(r'output\.example',{'status':200,'body':'sha256:7f-demo'});direct_vm.mock_web(r'artifact\.example',{'status':200,'body':'python 3.13 utf-8 linux'})
 with direct_vm.expect_revert('frozen specification changed'):c.record_run('fx-7','https://output.example/value','https://artifact.example/log')
def test_oversized_specification_fails_closed(direct_vm,direct_deploy,direct_alice,direct_bob,direct_charlie):
 direct_vm.warp('2035-01-01T00:00:00+00:00');direct_vm.sender=direct_alice;c=direct_deploy(CONTRACT);direct_vm.mock_web(r'spec\.example',{'status':200,'body':'x'*12001})
 with direct_vm.expect_revert('12000-byte inspection limit'):c.specify('fx-big','Canonical parser fixture','0x'+direct_bob.hex(),'0x'+direct_charlie.hex(),'Python 3.13 / UTF-8 / Linux','sha256:7f-demo','https://spec.example/fixture',600)
