import sys
from pathlib import Path

# Project root folder (layer-0-bedrock)
ROOT = Path(__file__).resolve().parents[1]

# Make ROOT importable so "import src..." works
sys.path.insert(0, str(ROOT))
