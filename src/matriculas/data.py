"""Carga y normalización inicial de datos."""

from pathlib import Path

import pandas as pd

COLUMN_MAPPING = {
    "Período Académico": "period",
    "Materia-Curso": "course_code",
    "# Estudiantes": "enrollment",
}

REQUIRED_COLUMNS = set(COLUMN_MAPPING)


def load_raw_data(path: Path) -> pd.DataFrame:
    """Carga un reporte raw y normaliza su esquema básico."""

    df = pd.read_excel(path)

    missing = REQUIRED_COLUMNS - set(df.columns)

    if missing:
        raise ValueError(f"Faltan columnas requeridas: {sorted(missing)}")

    return df.rename(columns=COLUMN_MAPPING)
