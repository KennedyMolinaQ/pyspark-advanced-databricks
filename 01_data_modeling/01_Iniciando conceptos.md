## 1.1 ¿Qué es un DataFrame en Spark?

Un DataFrame es:

> Una colección distribuida de filas (rows) organizadas en particiones

No es una tabla:

- No es un array  
- No es una lista  
- No es una base de datos  
- Es un **RDD optimizado + esquema**

### Modelo real

```text
DataFrame
 ├── Partition 1 → rows
 ├── Partition 2 → rows
 ├── Partition 3 → rows
 └── Partition N → rows
```
## 🔹 1.2 Componentes reales

a) Schema (estructura lógica)

El schema define cómo Spark interpreta los datos:
- nombres de columnas  
- tipos de datos  
- nullabilidad  
- estructura (simple o compleja)
```text
Ejemplo:

df.printSchema()

Salida típica:
root
 |-- user_id: long (nullable = false)
 |-- country: integer (nullable = true)
 |-- event_type: integer (nullable = true)
 |-- value: double (nullable = true)
```
Esto representa la estructura lógica del DataFrame.

---

b) Particiones (distribución física)

Las particiones definen cómo los datos se distribuyen físicamente en el cluster.  
Cada partición = 1 unidad de ejecución (task).
```text
Ejemplo:

print("Número de particiones:", df.rdd.getNumPartitions())

Ver tamaño por partición:

df.rdd.glom().map(len).collect()

Salida ejemplo:
[50000, 50000, 50000, 50000, ...]
```
Esto muestra la distribución física real de los datos.

---

c) Linaje (DAG)

El linaje es el grafo de transformaciones que Spark construye internamente para ejecutar el job.  
No ejecuta nada hasta que hay una acción (count(), show(), write(), etc).

Ejemplo:

df2 = df.filter("value > 0.5").select("user_id", "country")

Ver linaje lógico/físico:

df2.explain(mode="formatted")

Esto muestra:
- Plan lógico
- Plan optimizado
- Plan físico
- DAG de ejecución real

---

Modelo mental correcto:

Schema = cómo se ve el dato  
Particiones = dónde vive el dato  
DAG = cómo se procesa el dato
