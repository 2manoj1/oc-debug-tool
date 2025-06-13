# 🚀 OpenShift Debug CLI (`oc-debug`)

A lightweight Python CLI tool built using [Typer](https://typer.tiangolo.com/) and [Rich](https://rich.readthedocs.io/) to help DevOps and MLOps teams debug OpenShift resources interactively.

This tool prompts the user for details like resource type, name, namespace, and desired operation (`describe`, `logs`, etc.), and executes the corresponding `oc` commands with a clean output.

---

## 📦 Features

- ✅ Interactive prompts for pod/deployment/service debugging
- ✅ Support for `describe`, `logs`, `events`, and `exec`
- ✅ Colorful terminal UI with [Rich](https://rich.readthedocs.io/)
- ✅ Easy `oc login` integration via command or environment variables
- ✅ Single-command binary creation via PyInstaller

---

## ⚙️ Getting Started

### 🔧 Prerequisites
- Make sure `oc` CLI is installed on your system.
- Python 3.12+
- [uv](https://github.com/astral-sh/uv) (recommended) or `pip`

### 🔌 Installation (dev mode)

```bash
git clone this repo
cd oc-debug-tool

# Set up virtual environment
uv venv .

# Install dependencies
uv pip install -e .
or
uv sync
```

### ▶️ Usage
```bash
# Login first (optional if using env vars)
oc-debug login --token=sha256~xxx --server=https://api.example.com:6443

# Start debugging prompt
oc-debug
```

## 🌐 Environment Variable Support
Set your OpenShift credentials without passing them every time:
```bash
export OC_TOKEN="sha256~..."
export OC_SERVER="https://api.cluster.openshift.com:6443"
```
These are read automatically by the CLI.