# nedry-lockout

Jurassic Park–style terminal lockout animation.

A faithful recreation of the iconic  
"YOU DIDN'T SAY THE MAGIC WORD!" sequence.

---

## Installation & Usage

## macOS

### Run

```bash
rm -rf clean_test && \
python3 -m venv clean_test && \
source clean_test/bin/activate && \
python3 -m pip install --no-cache-dir --force-reinstall nedry-lockout && \
nedry
```

### If Python is missing

```bash
brew install python
```

---

## Linux (Ubuntu / Debian)

### Run

```bash
rm -rf clean_test && \
python3 -m venv clean_test && \
source clean_test/bin/activate && \
python3 -m pip install --no-cache-dir --force-reinstall nedry-lockout && \
nedry
```

### If Python / venv is missing

```bash
sudo apt update && sudo apt install -y python3 python3-venv
```

---

## Linux (Arch / Steam Deck)

### Run

```bash
rm -rf clean_test && \
python3 -m venv clean_test && \
source clean_test/bin/activate && \
python3 -m pip install --no-cache-dir --force-reinstall nedry-lockout && \
nedry
```

### If Python is missing

```bash
sudo pacman -Syu python
```

---

## Notes

- Requires Python 3.8+
- Uses isolated virtual environment
- Optimized for macOS and Linux terminals

---

## Troubleshooting

### Old version still runs

```bash
python3 -m pip install --no-cache-dir --force-reinstall nedry-lockout
```

### Steam Deck / Linux shell note

Commands must be separated by new lines or `&&`.  
Do not paste them as one plain space-separated line.

Correct example:

```bash
python3 -m venv clean_test && \
source clean_test/bin/activate && \
pip install nedry-lockout && \
nedry
```

---

## License

MIT
