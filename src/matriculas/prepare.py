"""Preparación de los datos de matrículas para modelado."""

import pandas as pd

from matriculas.config import BASE_YEAR, VALID_SEMESTER_CODES


def prepare_period(df: pd.DataFrame, column: str = "PERIODO") -> pd.DataFrame:
    """Prepara la información temporal del período académico.

    Conserva únicamente los períodos regulares 10 y 20 y crea:
    - year: año académico.
    - semester: semestre 1 o 2.
    - time_index: índice secuencial desde BASE_YEAR.
    """
    result = df.copy()

    # Garantizamos representación numérica
    result[column] = pd.to_numeric(result[column], errors="coerce")

    # Eliminamos registros sin período interpretable
    result = result.dropna(subset=[column])

    result[column] = result[column].astype(int)

    # Separar año y código del período
    result["year"] = result[column] // 100
    result["semester"] = result[column] % 100

    # Para este modelo solo interesan los semestres regulares
    result = result[result["semester"].isin(VALID_SEMESTER_CODES)].copy()

    # 10 -> semestre 1
    # 20 -> semestre 2
    result["semester"] = result["semester"].map(
        {
            10: 1,
            20: 2,
        }
    )

    # Índice temporal:
    # 201510 -> 0
    # 201520 -> 1
    # 201610 -> 2
    # ...
    result["time_index"] = 2 * (result["year"] - BASE_YEAR) + result["semester"] - 1

    return result
