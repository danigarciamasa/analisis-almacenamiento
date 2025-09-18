import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
from PIL import Image
import os

st.title("Análisis Técnico de Almacenamiento de Datos")
st.markdown("---")

## **Descripción del Escenario**
st.header("1. Descripción del Escenario")
st.markdown("""
Una empresa en crecimiento, que maneja grandes volúmenes de datos transaccionales, multimedia y de análisis, enfrenta desafíos en su infraestructura de almacenamiento. La solución actual, basada en discos duros tradicionales (HDD), ha comenzado a mostrar un **rendimiento deficiente**, especialmente en la velocidad de acceso a datos críticos para la operación diaria y la generación de reportes. La empresa necesita una solución escalable y rentable que no solo resuelva los problemas de rendimiento actuales, sino que también soporte un **crecimiento de datos proyectado del 50% en los próximos dos años**, sin incurrir en costos prohibitivos ni comprometer la fiabilidad.
""")
st.markdown("---")

## **Criterios de Evaluación**
st.header("2. Criterios de Evaluación")
st.markdown("""
Se han definido los siguientes criterios técnicos clave:
* **Velocidad de Lectura/Escritura:** Mide la rapidez con la que se pueden mover los datos.
* **Capacidad Total:** La cantidad de datos que el sistema puede almacenar.
* **Costo por GB:** El precio de la unidad de almacenamiento.
* **Fiabilidad (MTBF):** El "Tiempo Medio entre Fallos".
* **Consumo Energético:** El gasto de energía asociado a la operación del sistema.
* **Seguridad:** Las medidas de protección de los datos.
* **Escalabilidad:** La facilidad con la que el sistema de almacenamiento puede crecer.
""")
st.markdown("---")

## **Comparación de Tecnologías**
st.header("3. Comparación de Tecnologías")
st.markdown("""
| Característica | HDD (Disco Duro) | SSD (Disco de Estado Sólido) | Cintas (Tape) | Nube (Cloud Storage) |
|:---------------|:-----------------|:-----------------------------|:--------------|:---------------------|
| **Velocidad de Lectura** | ~150 MB/s | **~550 MB/s - 7 GB/s** | ~300 MB/s | Variable (múltiples GB/s) |
| **Velocidad de Escritura** | ~120 MB/s | **~500 MB/s - 7 GB/s** | ~250 MB/s | Variable (múltiples GB/s) |
| **Costo por GB** | **Bajo (~$0.02)** | Alto (~$0.15) | Muy bajo (~$0.01) | Variable (~$0.02 - $0.20) |
| **Fiabilidad** | Medio-bajo | **Alto** | Muy alto | Alto |
| **Consumo Energético** | Alto | **Bajo** | Muy bajo | Variable |
| **Seguridad** | Baja | Media | Alta | **Muy alta** |
| **Escalabilidad** | Baja | Media | Baja | **Muy alta** |
""")
st.markdown("---")

# Cargar los datos de ejemplo
try:
    df = pd.read_csv("data/sample_data.csv")
except FileNotFoundError:
    st.error("Archivo sample_data.csv no encontrado. Asegúrese de que está en la carpeta data.")
    df = pd.DataFrame({
        'Tecnologia': ['HDD', 'SSD', 'Cintas', 'Nube'],
        'Velocidad_Lectura_MBps': [150, 550, 300, 500],
        'Costo_GB_USD': [0.02, 0.15, 0.01, 0.05],
        'Fiabilidad_Score': [6, 9, 10, 9],
        'Escalabilidad_Score': [5, 7, 4, 10],
        'Seguridad_Score': [4, 8, 9, 10]
    })

## **Análisis Gráfico Comparativo**
st.header("4. Análisis Gráfico Comparativo")

st.subheader("Gráfico de Velocidad de Lectura")
fig_velocidad = px.bar(df, x='Tecnologia', y='Velocidad_Lectura_MBps',
                       title="Velocidad de Lectura (MB/s) por Tecnología",
                       labels={'Velocidad_Lectura_MBps': 'Velocidad (MB/s)', 'Tecnologia': 'Tecnología'},
                       color='Velocidad_Lectura_MBps')
st.plotly_chart(fig_velocidad)

st.subheader("Gráfico Radar de Criterios Cualitativos")
fig_radar = go.Figure()
for index, row in df.iterrows():
    fig_radar.add_trace(go.Scatterpolar(
        r=[row['Fiabilidad_Score'], row['Escalabilidad_Score'], row['Seguridad_Score']],
        theta=['Fiabilidad', 'Escalabilidad', 'Seguridad'],
        fill='toself',
        name=row['Tecnologia']
    ))
fig_radar.update_layout(
    polar=dict(radialaxis=dict(visible=True, range=[0, 10])),
    showlegend=True,
    title="Fiabilidad, Escalabilidad y Seguridad (1-10)"
)
st.plotly_chart(fig_radar)

st.subheader("Costo por GB")
fig_costo = px.bar(df, x='Tecnologia', y='Costo_GB_USD',
                   title="Costo por GB (USD) por Tecnología",
                   labels={'Costo_GB_USD': 'Costo por GB ($)', 'Tecnologia': 'Tecnología'},
                   color='Costo_GB_USD')
st.plotly_chart(fig_costo)
st.markdown("---")

## **Diagrama de la Infraestructura Propuesta**
st.header("5. Diagrama de la Infraestructura Propuesta")
st.markdown("Se propone una **arquitectura híbrida de almacenamiento** por niveles (Hot, Cold y Cloud), optimizando rendimiento y costos.")
try:
    image = Image.open('images/diagram.png')
    st.image(image, caption='Esquema Conceptual de la Infraestructura Híbrida', use_column_width=True)
except FileNotFoundError:
    st.info("El diagrama de infraestructura (diagram.png) no se encuentra en la carpeta /images.")
    st.markdown("Puedes crear el diagrama con una herramienta web (como draw.io) y subirlo a la carpeta `images/` de tu repositorio.")
st.markdown("---")

## **Análisis de Riesgos y Oportunidades**
st.header("6. Análisis de Riesgos y Oportunidades")
with st.expander("Haz clic para ver el análisis de riesgos y oportunidades"):
    st.markdown("""
### Riesgos Técnicos y Mitigaciones
* **Riesgo:** Complejidad y tiempo de la migración de datos. **Mitigación:** Plan de migración por fases.
* **Riesgo:** Alto costo inicial de los SSD. **Mitigación:** Justificar la inversión con un análisis detallado del TCO a largo plazo.
* **Riesgo:** Dependencia de un único proveedor de la nube. **Mitigación:** Diseñar una arquitectura multi-nube.
* **Riesgo:** Vulnerabilidad en la seguridad de los datos. **Mitigación:** Implementar encriptación y control de acceso.

### Oportunidades de Mejora
* **Mejora:** Optimización de costos a largo plazo con almacenamiento por niveles.
* **Mejora:** Mejora de la experiencia de usuario y la eficiencia operativa.
* **Mejora:** Habilitación de nuevas capacidades de negocio, como análisis de datos en tiempo real.
* **Mejora:** Aumento de la resiliencia del negocio y la recuperación ante desastres.
""")
st.markdown("---")

## **Conclusiones Técnicas**
st.header("7. Conclusiones Técnicas")
st.markdown("""
La arquitectura actual de HDD es insostenible para el crecimiento proyectado. La **solución recomendada es una infraestructura de almacenamiento híbrida (SSD + Nube)**, que combina el rendimiento del SSD para datos críticos con la escalabilidad y el costo-efectivo de la nube para archivo y backups.
""")

st.subheader("Simulación de Rendimiento con Crecimiento de Datos")
volumen_inicial_gb = 1000
crecimiento_anual_porc = 0.50
meses = np.arange(1, 25)
tasa_crecimiento_mensual = (1 + crecimiento_anual_porc)**(1/24) - 1
volumen_mensual = volumen_inicial_gb * (1 + tasa_crecimiento_mensual)**meses

latencia_base_hdd_ms = 50
latencia_base_ssd_ms = 5
degradacion_hdd_por_gb_ms = 0.005
degradacion_ssd_por_gb_ms = 0.0001

tiempo_respuesta_hdd = latencia_base_hdd_ms + (volumen_mensual * degradacion_hdd_por_gb_ms)
tiempo_respuesta_ssd = latencia_base_ssd_ms + (volumen_mensual * degradacion_ssd_por_gb_ms)

df_simulacion = pd.DataFrame({
    'Mes': meses,
    'HDD (ms)': tiempo_respuesta_hdd,
    'SSD (ms)': tiempo_respuesta_ssd
})

fig_simulacion = px.line(df_simulacion, x='Mes', y=['HDD (ms)', 'SSD (ms)'],
                        title='Tiempos de Respuesta con Crecimiento de Datos',
                        labels={'value': 'Tiempo de Respuesta (ms)', 'Mes': 'Meses', 'variable': 'Tecnología'},
                        markers=True)
st.plotly_chart(fig_simulacion)
