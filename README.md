# nedry-lockout

Jurassic Park–style terminal lockout animation.

A faithful recreation of the iconic  
"YOU DIDN'T SAY THE MAGIC WORD!" sequence.

---

## Quick Start

Pick your platform and run the command.

---

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

## Windows (PowerShell)

### First time (install Python)

```powershell
winget install --id Python.Python.3.12 --exact --source winget
```

Close PowerShell and open a new window.

### Run

```powershell
py -m venv clean_test; .\clean_test\Scripts\Activate.ps1; py -m pip install --no-cache-dir --force-reinstall nedry-lockout; nedry
```

### If activation is blocked

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

### If `nedry` is not recognized

```powershell
py -m nedry.main
```

---

## Notes

- Requires Python 3.8+
- Uses an isolated virtual environment (safe for all systems)
- Works on macOS, Linux, Windows

---

## Troubleshooting

### Old version still runs

```bash
python3 -m pip install --no-cache-dir --force-reinstall nedry-lockout
```

### Windows: `py` not found

Restart PowerShell after installing Python.

---

## License

MIT
