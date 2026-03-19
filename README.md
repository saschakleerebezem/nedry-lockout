# nedry-lockout

Jurassic Park–style terminal lockout animation.

A faithful recreation of the iconic "YOU DIDN'T SAY THE MAGIC WORD!" sequence, including:
- interactive command input
- authentic timing and pacing
- continuous lockout scroll
- terminal title override
- cross-platform support (macOS, Linux, Windows)

---

## Installation & Usage

### Universal (clean environment, recommended)

Works on macOS and Linux, and any system with Python 3:

rm -rf clean_test && \
python3 -m venv clean_test && \
source clean_test/bin/activate && \
python3 -m pip install --no-cache-dir --force-reinstall nedry-lockout && \
nedry

---

## macOS

### Option 1 — Quick run (no global install)

python3 -m venv clean_test
source clean_test/bin/activate
pip install nedry-lockout
nedry

### Option 2 — Install once (if your Python allows it)

python3 -m pip install --user nedry-lockout
nedry

Note: Some macOS setups (Homebrew Python) block global installs.
Use the virtual environment method if you see an "externally managed environment" error.

---

## Linux

### Quick run

python3 -m venv clean_test
source clean_test/bin/activate
pip install nedry-lockout
nedry

### Alternative (if allowed)

python3 -m pip install --user nedry-lockout
nedry

---

## Windows (PowerShell)

### Quick run (recommended)

python -m venv clean_test
clean_test\Scripts\activate
pip install nedry-lockout
nedry

### If `nedry` is not recognized

python -m nedry.main

---

## Notes

- Requires Python 3.8+
- No external dependencies
- Works in most modern terminals:
  - macOS Terminal / iTerm2
  - Linux terminals
  - Windows Terminal / PowerShell

### Sound behavior

- Windows: native beep via winsound
- macOS: system sounds via afplay
- Linux: terminal bell fallback (may depend on terminal settings)

---

## Troubleshooting

### Old version still runs

Force reinstall:

python3 -m pip install --no-cache-dir --force-reinstall nedry-lockout

Or use a clean environment:

rm -rf clean_test
python3 -m venv clean_test
source clean_test/bin/activate
pip install nedry-lockout
nedry

---

## License

MIT
