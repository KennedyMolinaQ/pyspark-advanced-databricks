# pyspark-advanced-databricks
En este repositorio se tratara de abarcar la configuración del entorno y conceptos desde basicos a avanzados


------------------------------------------------

NOTA IMPORTANTE

Este entorno permite practicar ingeniería de datos real con control total del motor Spark.
A diferencia de entornos serverless gratuitos, aquí sí se puede:
- tunear joins
- controlar broadcast
- gestionar memoria
- analizar planes físicos
- simular producción
- optimizar pipelines

------------------------------------------------

OBJETIVO DEL PROYECTO

Crear un laboratorio profesional para:
- formación en ingeniería de datos
- pruebas de arquitectura
- simulación de pipelines productivos
- aprendizaje de optimización Spark
- diseño de lakehouse local
- validación de patrones de datos
------------------------------------------------

CAPACIDADES DEL ENTORNO

- Spark SQL
- PySpark DataFrames
- Broadcast joins
- Shuffle joins
- AQE (Adaptive Query Execution)
- Repartition / Coalesce
- Skew handling
- Execution plans
- Delta Lake
- Arquitectura bronze / silver / gold
- Pipelines locales
- Tuning real de performance
- DAGs reales
- Jobs reales
- Stages reales


# Spark Advanced Labs Structure

```text
/labs
│
├── 01_data_modeling
│   └─ cómo se representan los datos en Spark
│
├── 02_partitioning_basics
│   └─ particiones físicas y lógicas
│
├── 03_parallelism
│   └─ tasks, cores, ejecutores, concurrencia real
│
├── 04_shuffle_mechanics
│   └─ movimiento de datos entre nodos
│
├── 05_joins
│   └─ estrategias de join y planes físicos
│
├── 06_broadcast
│   └─ joins optimizados por distribución
│
├── 07_skew_handling
│   └─ hot keys, data skew, balanceo
│
├── 08_aqe (Adaptive Query Execution)
│   └─ optimización dinámica del plan
│
├── 09_caching_persistence
│   └─ memoria, reutilización, materialización
│
├── 10_cluster_simulation
│   └─ simulación de cluster real
│
└── 11_benchmarking
    └─ métricas, tiempos, comparación de estrategias
