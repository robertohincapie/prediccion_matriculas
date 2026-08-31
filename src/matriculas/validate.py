"""Validación de los datos preparados para el modelo."""

from __future__ import annotations

import pandas as pd

from matriculas.config import BASE_YEAR


class DataValidationError(ValueError):
    """Indica que el dataset no cumple las reglas de calidad requeridas."""


REQUIRED_COLUMNS = {
    "period",
    "course_code",
    "enrollment",
    "year",
    "semester",
    "time_index",
}


def validate_required_columns(df: pd.DataFrame) -> None:
    """Verifica que existan todas las columnas requeridas."""

    missing = REQUIRED_COLUMNS - set(df.columns)

    if missing:
        raise DataValidationError(f"Faltan columnas requeridas: {sorted(missing)}")


def validate_course_codes(df: pd.DataFrame) -> None:
    """Verifica que los códigos de curso existan y no estén vacíos."""

    if df["course_code"].isna().any():
        raise DataValidationError("Existen registros sin código de curso.")

    empty = df["course_code"].astype(str).str.strip().eq("")

    if empty.any():
        raise DataValidationError("Existen códigos de curso vacíos.")


def validate_enrollment(df: pd.DataFrame) -> None:
    """Verifica que las matrículas sean numéricas y no negativas."""

    enrollment = pd.to_numeric(df["enrollment"], errors="coerce")

    if enrollment.isna().any():
        raise DataValidationError("Existen valores de matrícula no numéricos o nulos.")

    if (enrollment < 0).any():
        raise DataValidationError("Existen valores de matrícula negativos.")


def validate_semesters(df: pd.DataFrame) -> None:
    """Verifica que solamente existan semestres regulares."""

    invalid = ~df["semester"].isin([1, 2])

    if invalid.any():
        values = sorted(df.loc[invalid, "semester"].dropna().unique().tolist())

        raise DataValidationError(f"Existen semestres inválidos: {values}")


def validate_years(df: pd.DataFrame) -> None:
    """Verifica que los años sean compatibles con BASE_YEAR."""

    if df["year"].isna().any():
        raise DataValidationError("Existen registros sin año.")

    if (df["year"] < BASE_YEAR).any():
        raise DataValidationError(f"Existen años anteriores a BASE_YEAR={BASE_YEAR}.")


def validate_time_index(df: pd.DataFrame) -> None:
    """Verifica la consistencia del índice temporal."""

    expected = 2 * (df["year"] - BASE_YEAR) + df["semester"] - 1

    inconsistent = df["time_index"] != expected

    if inconsistent.any():
        raise DataValidationError("Existen índices temporales inconsistentes.")


def validate_dataset(df: pd.DataFrame) -> None:
    """Ejecuta todas las validaciones del dataset."""

    validate_required_columns(df)
    validate_course_codes(df)
    validate_enrollment(df)
    validate_semesters(df)
    validate_years(df)
    validate_time_index(df)
