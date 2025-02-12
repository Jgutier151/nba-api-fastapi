#!/usr/bin/env bash
# Install Rust (for maturin-based dependencies)
curl https://sh.rustup.rs -sSf | sh -s -- -y
source $HOME/.cargo/env
pip install --no-cache-dir -r requirements.txt
