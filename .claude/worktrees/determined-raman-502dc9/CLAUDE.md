# Instrucciones para Claude (CLAUDE.md)

Este archivo contiene reglas y contexto para el desarrollo del proyecto **"Enseñanza Curso Python"**.

---

## 1. Contexto del Proyecto

- **Tecnologías:** Python 3.12
- **Objetivo:** Ejecutar la enseñanza de un curso de Python con programa estructurado por bloques temáticos.
- **Estilo de asistencia:** Profesional, especialista en programación Python, análisis de datos con Python y manejo de bases de datos SQL (PostgreSQL, MySQL, SQLite).

---

## 2. Contexto del Desarrollador

- **Nombre:** Ronqui
- **Perfil:** Estudiante de derecho con especialización creciente en automatización de datos y procesos. Trabaja principalmente en la Universidad Libre (área de proyectos) y colabora con SoiTTech en proyectos específicos.
- **Stack principal:** Python 3.12 · PyQt5 · pandas · openpyxl · Rich · Streamlit · SQLite · MySQL · Power BI · Excel
- **Entorno de desarrollo:** iPad Air M4 con teclado mecánico · GitHub Codespaces como entorno principal
- **Dominio profesional:** Gestión de datos del sector público colombiano, concursos de méritos para la función pública.
- **Proyectos objetivo del curso:** Aplicación de gestión de talento · Sistema de repositorio de documentos · Herramienta de seguimiento de objetivos de equipo

---

## 3. Programa del Curso

- **Bloque 0 — Lógica de programación:** Algoritmos · Pseudocódigo · Árbol de descomposición · Lógica Booleana
- **Bloque 1 — Fundamentos absolutos:** Variables · Operadores · Strings · f-strings · Format Specifiers
- **Bloque 2 — Control de flujo:** Condicionales · Bucles · break/continue · Patrones 01–07 · Mapas de proceso
- **Bloque 3 — Estructuras de datos:** Listas · Diccionarios · Tuplas · Sets · Patrones 08–16
- **Bloque 4 — Funciones:** def · parámetros · scope · return · lambda · map() · filter()
- **Bloque 5 — Organización del código:** Módulos · venv/pip · Excepciones · Archivos de texto · datetime
- **Bloque 6 — OOP Básica:** Clases · Objetos · __init__ · Métodos · Herencia
- **Bloque 7 — Archivos, JSON y Bases de Datos:** open · read/write · json · csv · SQLite · sqlite3
- **Bloque 8 — Librerías y automatización:** Rich · Pandas · OpenPyXL · NumPy · Matplotlib · Seaborn · Plotly · Streamlit · SciPy · Polars · urwid · Dask
- **Ejercicios Integradores:** Ver instrucciones en Sección 4.

---

## 4. Estilo de Respuesta

- Responde siempre en **español**.
- Sé muy detallado en las explicaciones: comienza con definiciones y aplicabilidad del tema en la vida real.
- Cuando crees un componente nuevo, proporciona el **código completo** de una vez.
- Genera ejercicios basados en el contexto real de Ronqui: sector público colombiano, concursos de méritos, gestión documental, automatización de procesos. **Evita ejercicios genéricos** de frutas, estudiantes o listas de compras.
- Crea y documenta **patrones de código importantes** por cada bloque.
- Para los **Ejercicios Integradores** (al final del programa): genera ejercicios que combinen contenidos de múltiples bloques anteriores, con nivel de complejidad creciente y aplicación directa a los tres proyectos objetivo del curso.

---

## 5. Estructura del Repositorio

> ⚠️ **Completa esta sección** con la estructura real de carpetas de tu repositorio clonado.

```
Curso-de-Python/
├── 01. [RECURSOS]/
│   ├── [01. GUIAS]/
│   │   ├── Análisis de Datos con Python.html
│   │   ├── Guia Interactiva de Python.html
│   │   └── Roadmap python.html
│   ├── [02. CUADERNO Y NOTAS]/
│   │   ├── [01. NOTAS]/
│   │   ├── [02. Mi cartilla de Python]/
│   │   │   ├── [Recursos cartilla]/
│   │   │   ├── Cartilla_Python_Folleto_Oficio.pdf
│   │   │   ├── Mi Cartilla Python v2.docx
│   │   │   └── Logo de Python.webp
│   │   ├── [03. Memory Cards]/
│   │   │   ├── Observación para incluir en las memory card.txt
│   │   │   └── Python Memory Cards.pdf
│   │   └── cuaderno_python.html
│   ├── 03. [LIBROS]/
│   │   ├── algoritmos-programacion-Python.pdf
│   │   └── Python para todos.pdf
│   └── 04. [OTROS]/
│   │   ├── Ecosistema de analisis de datos con Python.docx
│   │   ├── Guia Completa Python.docx
│   │   ├── Patrones Python Completo.docx
│   │   └── Plan Estudio Python Completo.docx
├── 02. [ESTRUCTURA]/
│   ├── [00. Bloque 0 —  Logica de Programacion]/
│   ├── [01. Bloque 1 — Fundamentos absolutos]/
│   ├── [02. Bloque 2 — Control de flujo]/
│   ├── [03. Bloque 3 — Estructuras de datos]/
│   │   ├── [01. Listas]/
│   │   │   ├── Guía de listas en programación.png
│   │   │   └── Listas en Python.m4a
│   │   └── [02. Diccionarios]/
│   │   │   ├── Diccionarios.png
│   │   │   ├── Guía de diccionarios en programación.png
│   │   │   └── Diccionarios de Python y tablas hash.m4a
│   ├── [04. Bloque 4 — Funciones]/
│   ├── [05. Bloque 5 — Organización del código]/
│   ├── [06. Bloque 6 — OOP básica]/
│   ├── [07. Bloque 7 — Archivos, JSON y Bases de Datos]/
│   └── [08. Bloque 8 — Librerías y automatización]/
├── 03. [EJERCICIOS DE PRANCTICA]/
│   └── [01. LISTAS A FONDO]/
│   │   │   ├── [01. FACIL]/
│   │   │   ├── [02. MEDIO]/
│   │   │   ├── [03. DIFICIL]/
│   │   │   └── Ejercicio.py
├── CLAUDE.md
├── Ejercicio.py
├── SCRIPT PARA CURSO.txt
├── Calculadora de tiempos - urwid
├── README.md
├── [.vscode]/
│   └── settings.json
├── [.github]/
│   └── [workflows]/
└── 01. Aplicativo inscripciones.py
```

---

## 6. Recursos del Proyecto

> ⚠️ **Verifica y actualiza las rutas** según la ubicación real en tu equipo.

| Recurso | Ruta |
|---|---|
| Cuaderno de Python (HTML) | `D:\Bibliotecas\Github\Curso-de-Python\01. RECURSOS\02. CUADERNO Y NOTAS\cuaderno_python.html` |
| Cartilla de Python | `D:\Bibliotecas\Github\Curso-de-Python\01. RECURSOS\02. CUADERNO Y NOTAS\02. Mi cartilla de Python\Mi Cartilla Python v2.docx"` |
| Memory Cards | `D:\Bibliotecas\Github\Curso-de-Python\01. RECURSOS\02. CUADERNO Y NOTAS\03. Memory Cards\Python Memory Cards.pdf` |
| Repositorio GitHub | `https://github.com/warcamilode-cpu/Curso-de-Python` |

---

## 7. Convenciones del Proyecto

- Un archivo `.py` por bloque temático, nombrado como `bloque_00_logica.py`, `bloque_01_fundamentos.py`, etc.
- Los ejercicios se guardan en la carpeta correspondiente de cada bloque.
- Los patrones de código se documentan con comentarios explicativos dentro del archivo del bloque.
- El entorno virtual del proyecto se gestiona con `venv` y el archivo `requirements.txt` se mantiene actualizado.
