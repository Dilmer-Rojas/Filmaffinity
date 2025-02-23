
---

## 📌 **Ejemplo de Estadísticas Básicas en SQL**  

Supongamos que tienes una tabla llamada `ventas` con la columna `precio`. Puedes obtener estadísticas básicas así:  

```sql
SELECT 
    COUNT(precio) AS total_registros,  -- Cantidad de valores no nulos
    MIN(precio) AS minimo,             -- Valor mínimo
    MAX(precio) AS maximo,             -- Valor máximo
    AVG(precio) AS promedio,           -- Promedio
    SUM(precio) AS suma_total,         -- Suma total
    STDDEV(precio) AS desviacion_std,  -- Desviación estándar
    VARIANCE(precio) AS varianza       -- Varianza
FROM ventas;
```

---

## 📌 **Explicación de cada función**  

| **Función**       | **Descripción** |
|-------------------|---------------|
| `COUNT(precio)`  | Cuenta cuántos valores NO son `NULL` en la columna `precio`. |
| `MIN(precio)`    | Encuentra el valor mínimo en la columna `precio`. |
| `MAX(precio)`    | Encuentra el valor máximo en la columna `precio`. |
| `AVG(precio)`    | Calcula el **promedio** de la columna `precio`. |
| `SUM(precio)`    | Suma todos los valores de `precio`. |
| `STDDEV(precio)` | Calcula la **desviación estándar**, que mide la dispersión de los datos. |
| `VARIANCE(precio)` | Calcula la **varianza**, que es el cuadrado de la desviación estándar. |

---

## 📌 **Ejemplo con Datos**
| ID | precio |
|----|--------|
| 1  | 100    |
| 2  | 150    |
| 3  | 200    |
| 4  | 250    |
| 5  | 300    |

🔹 **Resultados de la consulta:**  
- `total_registros` → 5  
- `minimo` → 100  
- `maximo` → 300  
- `promedio` → 200  
- `suma_total` → 1000  
- `desviacion_std` → 79.05  
- `varianza` → 6250  

---

### 📌 **Si quieres agrupar por categorías**  
Puedes agrupar estadísticas por otro campo, por ejemplo, por `categoria`:  

```sql
SELECT 
    categoria,
    COUNT(precio) AS total,
    AVG(precio) AS promedio,
    MIN(precio) AS minimo,
    MAX(precio) AS maximo
FROM ventas
GROUP BY categoria;
```

---

## 📌 **¿Qué más puedes hacer?**
- **Filtrar datos** (`WHERE precio > 100`)  
- **Redondear valores** (`ROUND(AVG(precio), 2)`)  
- **Obtener la mediana** (requiere una subconsulta)  

Si necesitas estadísticas más avanzadas o específicas, dime y te ayudo a construir la consulta adecuada 🚀