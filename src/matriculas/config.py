"""Configuración inicial del laboratorio."""

from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]

DEFAULT_SOURCE_URL = (
    "https://robertohincapie.com/data/matriculas/reporte1_31_08_26.xlsx"
)

DEFAULT_RAW_DIR = PROJECT_ROOT / "data" / "raw"

# Primer año utilizado como referencia para el índice temporal
BASE_YEAR = 2015

# Períodos académicos regulares que utilizaremos
VALID_SEMESTER_CODES = (10, 20)
