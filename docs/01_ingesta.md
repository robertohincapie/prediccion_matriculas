# Laboratorio 01 — Ingesta reproducible

## Objetivo

Separar explícitamente el ciclo de vida del **código** del ciclo de vida de los **datos**.

El repositorio se actualiza mediante Git. Los nuevos reportes de matrículas llegan desde una fuente externa.

## Flujo

    fuente externa
         ↓
      ingest.py
         ↓
      data/raw/
         ↓
     manifest.json

## Qué hace esta etapa

- descarga el `.xlsx`;
- no modifica sus datos;
- verifica que el archivo no esté vacío;
- verifica que pueda abrirse como Excel;
- calcula SHA-256;
- registra las hojas del libro;
- conserva metadata HTTP disponible;
- evita sobrescribir silenciosamente un raw existente.

## Qué NO hace todavía

- no interpreta columnas;
- no valida códigos de curso;
- no valida períodos académicos;
- no elimina duplicados;
- no trata nulos;
- no construye features;
- no entrena modelos.

Estas responsabilidades aparecerán en iteraciones posteriores.
