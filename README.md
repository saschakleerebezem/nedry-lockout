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

MIT License

Copyright (c) 2026 Sascha Kleerebezem

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
