# Building or updating Binaryen.py

1. (Optional) Update `BINARYEN_VERSION` in `pyproject.toml` and `.github/workflows/build.yaml`
2. Run `bash scripts/build_libbinaryen.sh`
3. Run `cibuildwheel`, `python -m pip wheel .`, `python -m pip install -e .` or whichever supported build command you would prefer
