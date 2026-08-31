import pandas as pd
import pytest

from matriculas.validate import (
    DataValidationError,
    validate_dataset,
)


def valid_dataset():
    return pd.DataFrame({
        "period": [202510, 202520, 202610],
        "course_code": ["COD1", "COD1", "COD1"],
        "enrollment": [40, 45, 48],
        "year": [2025, 2025, 2026],
        "semester": [1, 2, 1],
        "time_index": [20, 21, 22],
    })


def test_valid_dataset_passes():
    df = valid_dataset()

    validate_dataset(df)


def test_negative_enrollment_fails():
    df = valid_dataset()

    df.loc[1, "enrollment"] = -5

    with pytest.raises(DataValidationError):
        validate_dataset(df)


def test_missing_course_code_fails():
    df = valid_dataset()

    df.loc[1, "course_code"] = None

    with pytest.raises(DataValidationError):
        validate_dataset(df)


def test_invalid_semester_fails():
    df = valid_dataset()

    df.loc[1, "semester"] = 3

    with pytest.raises(DataValidationError):
        validate_dataset(df)


def test_inconsistent_time_index_fails():
    df = valid_dataset()

    df.loc[1, "time_index"] = 999

    with pytest.raises(DataValidationError):
        validate_dataset(df)