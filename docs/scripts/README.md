# Patch 0004 - Repo Structure Management Tools

This patch introduces utility scripts to manage local patch archives and apply them in sequence.
Includes:

- `scripts/patch_applier.py`: A Python 3 cross-platform tool that applies patches from the `patches/` folder.
- Patch order handling, unzip, copy, overwrite logic.
- Cleans up temporary extract folder after use.
- Output logs for each patch applied.

## Usage

```bash
python3 scripts/patch_applier.py
```

Ensure your `patches/` folder is in the root of your local repo.

