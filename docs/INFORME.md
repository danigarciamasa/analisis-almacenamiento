# 📄 Informe Técnico y de Negocio: Análisis de Soluciones de Almacenamiento

### **Resumen Ejecutivo**

El presente informe analiza la infraestructura de almacenamiento de datos de la empresa, identificando la necesidad crítica de migrar de la tecnología de disco duro (HDD) a soluciones más modernas y eficientes. El crecimiento proyectado del 50% en los próximos dos años exige una estrategia de almacenamiento que garantice rendimiento, escalabilidad y un costo-beneficio favorable. Se evalúan tecnologías como HDD, SSD, Cinta y Almacenamiento en la Nube, concluyendo que una **estrategia híbrida** que combine **SSD en las instalaciones** para datos de acceso frecuente con **Almacenamiento en la Nube** para copias de seguridad y archivo de bajo costo es la solución óptima. Esta arquitectura balancea el alto rendimiento, la flexibilidad de la nube y la optimización de costes a largo plazo, mitigando los riesgos de ineficiencia y saturación.

---

### **1. Descripción del Escenario**

El cliente opera con cargas de trabajo intensivas en E/S (entrada/salida), incluyendo una base de datos de transacciones en línea (OLTP), análisis de datos y grandes repositorios de archivos. Las métricas actuales de rendimiento muestran una latencia creciente en operaciones críticas, lo que impacta directamente en la experiencia del usuario y en los Tiempos de Nivel de Servicio (SLA) para la generación de informes. El sistema actual, basado en HDD, tiene una capacidad de 10 TB, con un crecimiento esperado del 25% anual durante los próximos dos años, lo que se traduce en un **volumen total proyectado de 15.63 TB al final del período**. La principal restricción operativa es el rendimiento, mientras que las financieras apuntan a un balance entre el coste inicial (CAPEX) y los gastos operativos (OPEX).

* **Métricas de partida:**
    * Volumen de datos actual: 10 TB.
    * Volumen de datos de misión crítica: 20%.
    * Latencia promedio de E/S con HDD: 20 ms.
* **Supuestos no verificados:**
    * **\[Unverified]** El crecimiento de datos es constante y lineal.
    * **\[Unverified]** La carga de trabajo de E/S aumentará proporcionalmente al volumen de datos.

---

### **2. Criterios de Evaluación**

A continuación se definen los criterios clave para la evaluación de tecnologías, explicando su relevancia para el negocio.

* **Velocidad (Lectura/Escritura):** Se mide en megabytes por segundo (MB/s). Impacta directamente en el tiempo de respuesta de las aplicaciones, afectando la **experiencia de usuario** y el cumplimiento de **SLA**.
* **Capacidad (TB):** Cantidad total de datos que un sistema puede almacenar. Crucial para la planificación de la infraestructura y el **CAPEX**.
* **Costo por GB (USD):** El precio de la unidad de almacenamiento. Es una métrica fundamental para evaluar el **TCO (Costo Total de Propiedad)** y el impacto en el **OPEX**.
* **Fiabilidad (MTBF):** Tiempo Medio entre Fallos, medido en horas. Un MTBF alto reduce el riesgo de pérdida de datos y el **costo de la inactividad** no planificada.
* **Consumo (W):** El gasto energético del hardware. Influye en los **costos operativos** y la huella de carbono.
* **Seguridad:** Medidas de protección como el cifrado de datos y los controles de acceso. Es crucial para el **cumplimiento normativo** (ej. GDPR) y la protección de la información corporativa.
* **Escalabilidad:** Capacidad del sistema para crecer. La **escalabilidad horizontal** (añadir más nodos) o **vertical** (mejorar componentes) es clave para manejar el crecimiento de datos sin interrupciones. La **escalabilidad elástica** de la nube permite ajustar recursos según la demanda.

---

### **3. Comparación de Tecnologías**

La siguiente tabla compara las principales tecnologías de almacenamiento basándose en los criterios definidos.

| Tecnología | Velocidad Lectura (MB/s) | Velocidad Escritura (MB/s) | Capacidad (TB) | Costo por GB (USD) | Fiabilidad (MTBF horas) | Consumo (W) | Seguridad (1–5) | Escalabilidad (1–5) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **HDD** | **\[Unverified]** 150-200 | **\[Unverified]** 120-180 | **\[Unverified]** 1-20 | **\[Unverified]** 0.02 | **\[Unverified]** 1,500,000 | **\[Unverified]** 6-10 | 2 | 3 |
| **SSD** | **\[Unverified]** 500-7,000 | **\[Unverified]** 400-6,000 | **\[Unverified]** 0.5-30 | **\[Unverified]** 0.15 | **\[Unverified]** 2,000,000 | **\[Unverified]** 3-5 | 4 | 4 |
| **Cinta** | **\[Unverified]** 250-400 | **\[Unverified]** 200-350 | **\[Unverified]** 6-18 | **\[Unverified]** 0.01 | **\[Unverified]** >500,000,000 | **\[Unverified]** <1 | 5 | 2 |
| **Nube** | **\[Unverified]** Var. | **\[Unverified]** Var. | **\[Unverified]** Ilimitada | **\[Unverified]** 0.01-0.20 | **\[Unverified]** Muy alta | **\[Unverified]** Variable | 5 | 5 |

**Lectura ejecutiva:**
La tabla ilustra un claro **trade-off** entre coste y rendimiento. Mientras que los **HDD** ofrecen el menor costo por gigabyte, su rendimiento es el más bajo, lo que los hace inadecuados para cargas de trabajo críticas. Los **SSD** destacan en velocidad y fiabilidad, pero su costo inicial es considerablemente mayor. Las **Cintas** son la solución más económica para el archivo a largo plazo debido a su nulo consumo de energía cuando están inactivas, pero carecen de escalabilidad y accesibilidad. Finalmente, el **Almacenamiento en la Nube** ofrece la máxima flexibilidad, escalabilidad y seguridad, con un modelo de pago por uso que puede ser más costoso para datos de acceso muy frecuente.

---

### **4. Análisis Gráfico Comparativo**

Para la presentación visual del análisis, se recomienda la creación de tres gráficos utilizando `matplotlib` para la compatibilidad con el despliegue web sin dependencias complejas. Cada gráfico debe ser una figura independiente para optimizar la carga en Streamlit.

1.  **Gráfico de barras de velocidades:**
    * **Eje X:** Tecnologías (HDD, SSD, Cinta, Nube).
    * **Eje Y:** Velocidad (MB/s).
    * **Barras:** Dos barras por tecnología, representando la velocidad de lectura y escritura.
    * **Objetivo de negocio:** Demostrar visualmente la ventaja de rendimiento de los SSD sobre los HDD.
2.  **Gráfico de barras de costos:**
    * **Eje X:** Tecnologías.
    * **Eje Y:** Costo por GB (USD).
    * **Objetivo de negocio:** Resaltar la diferencia en el coste de unidad y justificar la inversión en SSD para datos críticos.
3.  **Gráfico de radar cualitativo:**
    * **Eje radial:** Puntuación normalizada de 1 a 5.
    * **Eje angular:** Criterios (Fiabilidad, Escalabilidad, Seguridad).
    * **Conversión:** Para la fiabilidad, la normalización se puede hacer mapeando el MTBF a una escala de 1 a 5, por ejemplo:
        * < 1.5 M horas = 1
        * 1.5 M - 2 M horas = 3
        * > 500 M horas = 5
    * **Objetivo de negocio:** Presentar una visión holística de las cualidades de cada tecnología más allá de las métricas puramente cuantitativas.

---

### **5. Simulación de Rendimiento**

**Escenario de simulación:**
* Volumen de datos inicial: 10 TB.
* Crecimiento anual: 25%.
* Horizonte: 2 años.

**Modelo de tiempo de respuesta (proxy de latencia de E/S):**
El tiempo de respuesta estimado es una función del volumen total de datos y la velocidad de lectura de la tecnología. **\[Speculation]** Se asume que el tiempo de respuesta total aumenta linealmente con el volumen de datos.

**Tabla de resultados:**

| Año | Volumen Estimado (TB) | Tiempo estimado HDD (ms) **\[Unverified]** | Tiempo estimado SSD (ms) **\[Unverified]** |
| :--- | :--- | :--- | :--- |
| 0 | 10.00 | 1000 | 100 |
| 1 | 12.50 | 1250 | 125 |
| 2 | 15.63 | 1563 | 156 |

**Interpretación ejecutiva:**
La simulación muestra que la latencia de un sistema basado en HDD aumentaría en más del 50% en tan solo dos años. Este aumento de 563 ms en el tiempo de respuesta podría traducirse en interrupciones en los servicios, incumplimiento de SLA y una frustración significativa para los usuarios. Por el contrario, un sistema basado en SSD mantendría un rendimiento consistente, con un aumento marginal del 56 ms en el tiempo de respuesta, asegurando la continuidad del negocio y la satisfacción del cliente.

**Limitaciones del modelo:** Este es un modelo simplificado que no considera la fragmentación de archivos, el rendimiento de la red o las optimizaciones de software.

---

### **6. Guía de Arquitectura Propuesta**

Se recomienda un **patrón de arquitectura híbrida** de almacenamiento por niveles, diseñado para optimizar tanto el rendimiento como el coste.

* **Nivel de datos calientes (Hot Tier):** Consiste en **SSD on-premise** para alojar datos de misión crítica que requieren baja latencia (bases de datos OLTP, cachés). Esto garantiza el máximo rendimiento para las operaciones más frecuentes.
* **Nivel de datos fríos (Cold Tier):** Se utilizará el **almacenamiento en la Nube** (por ejemplo, AWS S3 Glacier, Azure Archive Storage) para copias de seguridad a largo plazo, datos históricos y archivos que se consultan con poca frecuencia. Esto aprovecha el modelo de pago por uso para reducir drásticamente los costos operativos.
* **Flujo de datos:** Los datos se ingieren y procesan inicialmente en el nivel de SSD. Tras un período de tiempo definido por la política de retención, los datos más antiguos se mueven automáticamente al almacenamiento en la nube para archivo.
* **Seguridad y cumplimiento:** Se implementará **cifrado en reposo y en tránsito**. Los permisos de acceso se gestionarán bajo el principio de **mínimo privilegio (IAM)** y se aplicará la **autenticación multifactor (MFA)** para el acceso a la nube. La arquitectura cumple con los requisitos del **RGPD** al mantener los datos de misión crítica bajo el control directo de la empresa.
* **Recuperación ante desastres (DR):** La nube servirá como una ubicación de respaldo externo con objetivos de tiempo de recuperación (RTO) y de punto de recuperación (RPO) claramente definidos.

---

### **7. Riesgos, Mitigaciones y Oportunidades**

* **Riesgos:**
    * **Costo inicial:** El **CAPEX** de los SSD es alto.
    * **Durabilidad de las escrituras:** **\[Inference]** La vida útil de los SSD puede verse afectada por cargas de trabajo de escritura muy intensivas.
    * **Dependencia de la conectividad:** La latencia y la intermitencia en la red pueden afectar al acceso a los datos en la nube.
    * **Seguridad:** La migración a la nube introduce nuevos vectores de ataque si no se configura correctamente.
* **Mitigaciones:**
    * **Enfoque híbrido:** Se minimiza el costo inicial al no migrar todos los datos a SSD.
    * **Selección de SSD:** Se elige SSDs de grado empresarial diseñados para cargas de trabajo de escritura intensiva.
    * **Redundancia de red:** Se utiliza múltiples proveedores de servicios de Internet (ISP) para la conectividad a la nube.
    * **Seguridad proactiva:** Se implementan políticas de cifrado de extremo a extremo y una gestión estricta de las identidades y accesos.
* **Oportunidades:**
    * **Optimización del OPEX:** El modelo de pago por uso de la nube reduce los costos a largo plazo para el archivo.
    * **Mejora de SLA:** Los tiempos de respuesta se reducen drásticamente, lo que mejora la experiencia del usuario y permite nuevos casos de uso.
    * **Elasticidad:** La capacidad de escalar recursos de almacenamiento bajo demanda permite a la empresa adaptarse a picos de actividad sin sobreinversión.
    * **Continuidad del negocio:** La arquitectura de DR en la nube reduce significativamente los tiempos de inactividad en caso de desastre.

---

### **8. Conclusiones Técnicas y Recomendación**

Se recomienda la implementación de una **solución de almacenamiento híbrida (SSD + Nube)**. Esta arquitectura no solo abordará las limitaciones de rendimiento del sistema actual, sino que también proporcionará la flexibilidad y escalabilidad necesarias para el crecimiento futuro. La justificación técnica se basa en la capacidad del SSD para ofrecer una latencia mínima para datos críticos, mientras que la justificación de negocio se centra en la optimización de costes y la mejora de la continuidad del negocio que ofrece la nube.

**Próximos pasos:**
1.  **Validación de costes:** Realizar un análisis de costes detallado con proveedores de nube específicos (ej. AWS, Azure).
2.  **Prueba de Concepto (PoC):** Implementar un pequeño entorno de prueba para validar el rendimiento y la interoperabilidad de la solución híbrida.
3.  **Plan de migración:** Desarrollar un plan detallado de migración por fases para minimizar las interrupciones en el servicio.
4.  **Definición de métricas de éxito:** Establecer métricas de rendimiento (p. ej., reducción de latencia en un 80%) y financieras (p. ej., ahorro del TCO a 3 años) para medir el éxito del proyecto.

---

### **9. Apéndices**

#### **Glosario de Términos**
* **CAPEX:** Gasto de Capital (costo inicial de la infraestructura).
* **OPEX:** Gasto Operativo (costos continuos, ej. energía, licencias).
* **MTBF:** Mean Time Between Failures (Tiempo Medio Entre Fallos).
* **SLA:** Service Level Agreement (Acuerdo de Nivel de Servicio).
* **TCO:** Total Cost of Ownership (Costo Total de Propiedad).
* **RGPD:** Reglamento General de Protección de Datos.
* **RPO:** Recovery Point Objective (Objetivo de Punto de Recuperación).
* **RTO:** Recovery Time Objective (Objetivo de Tiempo de Recuperación).
