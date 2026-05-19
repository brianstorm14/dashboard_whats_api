<a name="readme-top"></a>

<br />
<div align="center">

<h3 align="center">Dashboard de Mensajes por WhatsApp API</h3>
  <p align="center">
    Dashboard desarrollado en Streamlit para visualizar métricas de mensajes enviados mediante WhatsApp API, integrando información del panel de Meta y registros operativos de listas de distribución.
    <br />
    <a href="#uso"><strong>Ver cómo usar »</strong></a>
    <br />
    <br />
  </p>
</div>

<details>
  <summary>Tabla de contenidos</summary>
  <ol>
    <li>
      <a href="#acerca-del-proyecto">Acerca del proyecto</a>
      <ul>
        <li><a href="#fuentes-de-información">Fuentes de información</a></li>
        <li><a href="#módulos-principales">Módulos principales</a></li>
        <li><a href="#arquitectura">Arquitectura</a></li>
      </ul>
    </li>
    <li>
      <a href="#iniciando">Iniciando</a>
      <ul>
        <li><a href="#prerequisitos">Prerequisitos</a></li>
        <li><a href="#instalación">Instalación</a></li>
      </ul>
    </li>
    <li><a href="#uso">Uso</a></li>
    <li><a href="#estructura-del-repositorio">Estructura del repositorio</a></li>
    <li><a href="#contacto">Contacto</a></li>
  </ol>
</details>

## Acerca del proyecto

Este repositorio contiene una aplicación web desarrollada en **Streamlit** para analizar el comportamiento de envíos realizados a través de **WhatsApp API**.

El dashboard permite consultar información desde dos perspectivas:

- **Meta Dashboard**: métricas consolidadas a partir de un archivo exportado con información de conversaciones, plantillas, fechas y costos.
- **Listas de distribución**: análisis de archivos operativos utilizados para campañas y envíos masivos, incluyendo validación de números telefónicos, programas, fechas y plantillas.

<p align="right">(<a href="#readme-top">regresar arriba</a>)</p>

---

### Fuentes de información

#### Meta Dashboard

La información proviene de la base de datos en MongoDB y se procesa para cargarse en:

- `DataClean.csv`

A partir de este archivo se procesan campos como:

- Fecha de envío
- Número de conversaciones
- Costo
- Categoría o plantilla

#### Listas de distribución

La información se consolida desde múltiples archivos CSV que fueron enviados por la SII para los envíos, y son depositados como archivos csv dentro de:

- `lists/`

Estos archivos se unifican para generar métricas de operación relacionadas con:

- Total de registros
- Números válidos e inválidos
- Programas atendidos
- Plantillas utilizadas
- Actividad por fecha
- Contactos únicos por programa

<p align="right">(<a href="#readme-top">regresar arriba</a>)</p>

---

### Módulos principales

#### Selector de fuente de datos

La aplicación permite alternar entre dos vistas principales:

- `Meta Dashboard`
- `Listas de distribución`

---

#### Meta Dashboard 📊

Muestra indicadores generales sobre mensajes y costos:

- Total de mensajes
- Plantillas distintas
- Días de envío
- Costo acumulado
- Promedio de mensajes por día
- Costo promedio por mensaje
- Día con mayor volumen de mensajes

Además, integra las siguientes visualizaciones:

- Mensajes por plantilla
- Mensajes por día
- Costo acumulado
- Costo diario

---

#### Listas de distribución 📋

Consolida y analiza los archivos operativos de campañas de mensajería.

Incluye métricas como:

- Total de registros
- Números válidos
- Errores por teléfonos inválidos
- Programas distintos
- Promedio por día
- Programa con más envíos
- Día más activo
- Plantilla más usada

También presenta visualizaciones de:

- Mensajes por programa
- Mensajes por día
- Plantillas más usadas
- Mensajes por programa y fecha
- Contactos únicos por programa

---

### Procesamiento de datos

#### Limpieza de información de Meta

El archivo `DataClean.csv` es procesado para:

- Convertir fechas a formato datetime
- Convertir conversaciones a valores numéricos
- Limpiar y convertir costos a formato flotante

#### Limpieza de listas de distribución

Los archivos de `lists/` son integrados y procesados para:

- Conservar las primeras cinco columnas esperadas
- Eliminar filas completamente vacías
- Convertir fechas al formato correcto
- Limpiar números telefónicos
- Validar teléfonos con longitud de 10 dígitos

<p align="right">(<a href="#readme-top">regresar arriba</a>)</p>

---

### Arquitectura

- **Streamlit** para la interfaz web
- **Pandas** para carga, transformación y análisis de datos
- **Plotly Express** para visualizaciones interactivas
- Archivos CSV como fuente de información

<p align="right">(<a href="#readme-top">regresar arriba</a>)</p>

## Iniciando

Para ejecutar el proyecto en local, sigue estos pasos:

### Prerequisitos

- Python instalado
- Dependencias incluidas en `requirements.txt`

### Instalación

1. Clonar repositorio:
```bash
git clone https://github.com/brianstorm14/dashboard_whats_api.git
cd dashboard_whats_api
```

2. Crear entorno virtual:
```bash
python -m venv venv
```

3. Activar entorno virtual:
Para Windows:
```bash
source venv/Scripts/activate
```

Para Mac/Linux:
```bash
source venv/bin/activate
```

4. Instalar dependencias:
```bash
pip install -r requirements.txt
```

<p align="right">(<a href="#readme-top">regresar arriba</a>)</p>

## Uso
Para levantar la aplicación de Streamlit, ejecuta:
```bash
streamlit run app.py
```

Una vez iniciada, la aplicación mostrará un selector para elegir entre:
Meta Dashboard
Listas de distribución
Cada vista despliega sus métricas y gráficas correspondientes.

<p align="right">(<a href="#readme-top">regresar arriba</a>)</p>

## Estructura del repositorio
```text
.
├─ app.py
├─ DataClean.csv
├─ requirements.txt
├─ lists/
│  ├─ beneficiarios_tarjetas 12 mar.csv
│  ├─ recoger_tarjeta 5 may.csv
│  ├─ dia_madres_2025 9 may.csv
│  ├─ dia_madres_2025_2 10 may.csv
│  ├─ renovacion_tarjeta_3 19 a 25 may.csv
│  ├─ Retarjeteo 3 jun.csv
│  ├─ Retarjeteo 4 jun.csv
│  ├─ Retarjeteo 5 jun.csv
│  ├─ Retarjeteo 39 jun.csv
│  ├─ Retarjeteo 9 jun.csv
│  ├─ Retarjeteo 10 jun.csv
│  ├─ Retarjeteo 11 jun.csv
│  └─ Retarjeteo 12 jun.csv
└─ utils/
   ├─ load_data.py
   ├─ metrics.py
   ├─ lists.py
   └─ lists_metrics.py
```

<p align="right">(<a href="#readme-top">regresar arriba</a>)</p>

## Contacto
Brian De Anda - jafeth1114@gmail.com

Project Link: [(https://github.com/brianstorm14/dashboard_whats_api.git)]
<p align="right">(<a href="#readme-top">regresar arriba</a>)</p> ```
