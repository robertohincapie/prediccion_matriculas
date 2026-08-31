# Predicción de matrículas — Laboratorio MLOps

Versión inicial del repositorio para el laboratorio de despliegue y ciclo de vida de modelos.

## Punto de partida

Se asume que el estudiante ya conoce:

- Git
- Python
- UV
- ambientes virtuales (`.venv`)

La primera responsabilidad nueva del proyecto es la **ingesta reproducible de datos**.

La fuente inicial es:

`https://robertohincapie.com/data/matriculas/reporte1_31_08_26.xlsx`

El archivo descargado se considera **raw**: no se edita ni se transforma manualmente.

## Estructura

    prediccion-matriculas/
    ├── src/
    │   └── matriculas/
    │       ├── __init__.py
    │       ├── config.py
    │       └── ingest.py
    ├── data/
    │   └── raw/
    │       └── .gitkeep
    ├── pyproject.toml
    ├── uv.lock              # se generará con uv sync
    ├── .python-version
    ├── .gitignore
    └── README.md

Los archivos descargados dentro de `data/raw/` no se versionan con Git.

## Preparación

Desde la raíz del repositorio:

    uv sync

## Ejecutar la ingesta

    uv run python -m matriculas.ingest

También puede indicarse explícitamente otra URL:

    uv run python -m matriculas.ingest --url https://servidor/archivo.xlsx

o un directorio raw diferente:

    uv run python -m matriculas.ingest --raw-dir data/raw

## Resultado

La primera ejecución crea una carpeta semejante a:

    data/raw/reporte1_31_08_26/
    ├── reporte1_31_08_26.xlsx
    └── manifest.json

`manifest.json` registra, entre otros:

- URL de origen;
- nombre del archivo;
- instante de ingesta en UTC;
- tamaño en bytes;
- SHA-256;
- tipo MIME informado por el servidor;
- hojas encontradas en el libro Excel.

## Principios de esta versión

### 1. Código y datos tienen ciclos de vida distintos

Git versiona el código del proyecto.

La llegada de un nuevo archivo de matrículas es un **evento de datos**, no un cambio de código.

### 2. Raw es inmutable

Un archivo descargado no debe corregirse manualmente. Cualquier limpieza futura debe quedar expresada en código.

### 3. La ingesta es idempotente

Si el mismo archivo ya existe y su SHA-256 coincide, una nueva ejecución no lo sobrescribe.

Si existe un archivo con el mismo nombre pero contenido diferente, el proceso se detiene para evitar perder trazabilidad.

### 4. Cada dataset debe poder identificarse

El SHA-256 permite reconocer exactamente qué bytes fueron ingeridos.

## Próxima iteración

La siguiente etapa del laboratorio será la **validación de datos**:

    fuente
       ↓
    ingesta
       ↓
      raw
       ↓
    validación
       ↓
    processed

En esa etapa revisaremos la estructura real del Excel, las columnas, los períodos académicos, los códigos de curso, duplicados, valores faltantes y reglas de negocio.
