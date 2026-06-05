# YouTube Music Desktop for Linux

Simple desktop application for YouTube Music built with PyQt6.

## Features

* Persistent login
* Saved cookies and session
* Standalone desktop window
* Cross-user compatible storage path
* Custom application icon

## Requirements

* Python 3
* PyQt6
* PyQt6 WebEngine

## Installation

```bash
sudo apt update
sudo apt install python3-pyqt6 python3-pyqt6.qtwebengine
```

## Run

```bash
python3 ytmusic.py
```

## Project Structure

```text
.
├── ytmusic.py
├── icon.png
└── README.md
```

## Notes

The application stores cookies and session data locally, allowing users to stay logged in between launches.

Built for Linux using PyQt6 and Qt WebEngine.
