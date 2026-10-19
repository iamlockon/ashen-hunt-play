"""Validate the compiled payload before a manual Pages release."""
import hashlib
import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
site = root / 'site'
release = json.loads((root / 'release.json').read_text())
assert (site / 'index.html').is_file()
assert len(release['source_commit']) == 40
expected = set(release['sha256'])
actual = {str(p.relative_to(site)) for p in site.rglob('*') if p.is_file()}
assert expected == actual, 'Release inventory changed'
for name, digest in release['sha256'].items():
    p = site / name
    assert not p.is_symlink()
    assert p.stat().st_size < 100 * 1024 * 1024, f'File is too large: {name}'
    assert p.suffix not in {'.cs', '.glb', '.zip', '.log'}, f'Authoring file in player: {name}'
    assert hashlib.sha256(p.read_bytes()).hexdigest() == digest, f'Hash mismatch: {name}'
assert len(list((site / 'Build').glob('*.loader.js'))) == 1
assert len(list((site / 'Build').glob('*.data.unityweb'))) == 1
assert len(list((site / 'Build').glob('*.wasm.unityweb'))) == 1
print(f"Verified {len(expected)} files from game commit {release['source_commit']}")
