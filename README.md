# curso-de-python

Repositorio personal de aprendizaje de Python — Ronqui · SoiTTech  
Plan estructurado de 14 semanas, desde lógica de programación hasta análisis de datos y automatización.

---

## Sobre este repositorio

Este repositorio documenta mi proceso de aprendizaje de Python aplicado a casos reales de **SoiTTech**, incluyendo ejercicios progresivos, scripts de producción y recursos de referencia.

Todo el código está organizado por semana y etapa. Cada carpeta contiene los ejercicios practicados, el script de la semana y notas personales.

---

## Plan de estudio — 14 semanas

### Etapa 0 — Lógica de programación
> Base conceptual antes de escribir código

| Semana | Tema | Estado |
|--------|------|--------|
| 00 | Pensamiento algorítmico — pseudocódigo, diagramas de flujo, descomposición | ✅ |
| 01 | Lógica booleana — operadores, tablas de verdad, prioridad, condiciones | ✅ |

---

### Etapa 1 — Estructuras de datos
> Listas, diccionarios, tuplas y sets a fondo

| Semana | Tema | Estado |
|--------|------|--------|
| 02 | Listas — métodos, slicing, comprehension, patrones | ✅ |
| 03 | Diccionarios — get, keys, values, items, comprensiones | 🔄 |
| 04 | Tuplas y Sets — unpacking, operaciones de conjuntos | ⬜ |

---

### Etapa 2 — Funciones y manejo de errores
> Código reutilizable y robusto

| Semana | Tema | Estado |
|--------|------|--------|
| 05 | Funciones — def, return, *args, **kwargs, lambda | ⬜ |
| 06 | Manejo de errores — try, except, finally, raise | ⬜ |

---

### Etapa 3 — Archivos, módulos y OOP
> Aplicaciones reales

| Semana | Tema | Estado |
|--------|------|--------|
| 07 | Archivos y JSON — open, read, write, json.load, csv | ⬜ |
| 08 | Módulos y paquetes — os, pathlib, datetime, random | ⬜ |
| 09 | Clases y objetos — class, __init__, self, herencia | ⬜ |

---

### Etapa 4 — Automatización y datos
> Objetivo final del curso

| Semana | Tema | Estado |
|--------|------|--------|
| 10 | Automatización — os, shutil, subprocess, scripts | ⬜ |
| 11 | Pandas básico — DataFrame, filtros, groupby, Excel | ⬜ |
| 12 | Visualización — Matplotlib, Plotly, gráficas reales | ⬜ |
| 13 | Proyecto integrador — reporte automático SoiTTech | ⬜ |

---

## 📁 Estructura del repositorio

```
curso-de-python/
│
├── semana-00/          # Pensamiento algorítmico
│   ├── ejercicios/
│   ├── notas.md
│   └── script.py
│
├── semana-01/          # Lógica booleana
│   ├── ejercicios/
│   └── notas.md
│
├── semana-02/          # Listas a fondo
│   ├── ejercicios/
│   ├── script_planeacion_v1.py
│   └── notas.md
│
├── ...
│
├── recursos/
│   ├── cuaderno_python.html    # Cuaderno interactivo de apuntes
│   ├── python_cards_v2.pdf     # Tarjetas de referencia para imprimir
│   └── plan_completo.md
│
└── README.md
```

---

## 🔑 Patrones clave aprendidos

Los patrones más importantes trabajados durante el curso:

```python
# 1. Nombre por valor máximo/mínimo
pos    = valores.index(max(valores))
nombre = nombres[pos]

# 2. Filtrar con zip + list comprehension
cumplen = [n for n, v in zip(nombres, valores) if v >= meta]

# 3. Acumular en listas dentro de un for
aprobadas  = []
pendientes = []
for estado in estados:
    if estado == "aprobada":
        aprobadas.append(estado)
    else:
        pendientes.append(estado)

# 4. enumerate + zip desempaquetado
for i, (nombre, valor) in enumerate(zip(nombres, valores), start=1):
    print(f"{i}. {nombre} — {valor}")

# 5. Operador ternario
estado = "✅ Cumplió" if valor >= meta else "❌ No cumplió"

# 6. Reporte de conteo desde lista
total     = len(estados)
aprobadas = estados.count("aprobada")
porcentaje = aprobadas / total

# 7. Capacidad vs demanda
capacidad  = [m * d for m, d in zip(metas_dia, dias)]
diferencia = [c - x for c, x in zip(capacidad, carpetas)]
en_riesgo  = [e for e, d in zip(etapas, diferencia) if d < 0]
```

---

## 🛠️ Stack técnico

| Herramienta | Uso |
|---|---|
| Python 3.x | Lenguaje principal |
| rich | Tablas formateadas en terminal |
| pandas | Análisis de datos (Etapa 4) |
| matplotlib / plotly | Visualización (Etapa 4) |
| openpyxl | Exportar a Excel |
| GitHub Codespaces | Entorno de desarrollo (iPad) |

---

## 📂 Script de referencia

El script `script_planeacion.py` es el hilo conductor de todo el curso.  
Evoluciona semana a semana desde un script básico hasta un reporte automatizado completo:

| Versión | Estado | Descripción |
|---|---|---|
| v1 | ✅ | Variables hardcodeadas, 3 tablas con formato |
| v2 | 🔄 | Funciones, validación de entrada |
| v3 | ⬜ | Input del usuario, manejo de errores |
| v4 | ⬜ | Exportar a Excel con Pandas |
| v5 | ⬜ | Gráfica de avance con Matplotlib |

---

## 📖 Recursos

- 📓 **Cuaderno interactivo** — apuntes por semana y por tema, con buscador
- 🃏 **Tarjetas de referencia** — 28 tarjetas para imprimir y argolear
- 📋 **Checklist antes de codificar** — hábito de pseudocódigo antes de abrir el editor

---

## 👤 Autor

**Ronqui** — SoiTTech Colombia  
Estudiante de pregrado · Desarrollador de aplicaciones de escritorio · Automatización con Python

---

*Repositorio en construcción activa — actualizado semana a semana.*
