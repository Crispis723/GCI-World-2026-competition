# Resumen y organización del cuaderno `baseline.ipynb`

Este archivo resume y organiza el contenido del cuaderno de línea base para la competición.

## Propósito
- Construir una línea base para predecir si un jugador será seleccionado en el Draft de la NFL usando pruebas físicas y atributos del jugador.

## Estructura recomendada del cuaderno
1. Configuración: importaciones y definición de rutas.
2. Carga de datos: leer `train.csv`, `test.csv` y `sample_submission.csv`.
3. EDA: resumen de datos, valores faltantes, visualizaciones y análisis por escuela/conferencia.
4. Preprocesamiento: imputación, codificación, eliminación de columnas irrelevantes.
5. Ingeniería de características: crear `BMI`, `Sprint_Score`, interacciones y agregados por `Position`.
6. Modelado: baseline con RandomForest, validación cruzada y comparación con otros modelos.
7. Predicción y guardado del archivo de envío `submission.csv`.
8. Próximos pasos y notas de mejora.

## Cambios sugeridos realizados
- Se movió el cuaderno a `notebooks/baseline.ipynb` para mantener la raíz más limpia.
- Se añadió este resumen en `docs/` para facilitar la lectura y navegación del flujo de trabajo.
- Se creó una prueba simple en `tests/` que verifica que el notebook esté presente en `notebooks/`.

## Notas para ejecución
- Asegúrate de que la carpeta `input/` contenga `train.csv`, `test.csv` y `sample_submission.csv` cuando ejecutes el cuaderno.
- Ejecuta las celdas en orden de arriba a abajo para mantener el estado del DataFrame coherente.
- Si trabajas en Colab, ajusta las rutas de `drive.mount()` y `%cd` según corresponda.

## Buenas prácticas
- Usa un entorno virtual y `requirements.txt`.
- Versiona cambios en Git con mensajes claros.
- Añade pruebas unitarias adicionales para funciones reutilizables (preprocesamiento, ingeniería de características, métricas).
