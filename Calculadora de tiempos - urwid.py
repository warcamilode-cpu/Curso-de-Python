#!/usr/bin/env python3
"""
Suite de Calculadoras — versión urwid (terminal TUI)
Conversión desde PyQt5 — Compatible con iPad + Blink + GitHub Codespaces

Instalar: pip install urwid --break-system-packages
Ejecutar:  python3 suite_calculadoras_tui.py
"""
import urwid
from datetime import datetime


# ═══════════════════════════════════════════════════════════════════════
#  LÓGICA DE CÁLCULO  (idéntica al original — sin dependencias de Qt)
# ═══════════════════════════════════════════════════════════════════════

def dias_30e360(inicio: datetime, fin: datetime) -> int:
    d1, m1, a1 = inicio.day, inicio.month, inicio.year
    d2, m2, a2 = fin.day,   fin.month,   fin.year
    if d1 == 31: d1 = 30
    if d2 == 31: d2 = 30
    return (a2 - a1) * 360 + (m2 - m1) * 30 + (d2 - d1)

def dias_30e360_mas1(inicio: datetime, fin: datetime) -> int:
    return dias_30e360(inicio, fin) + 1

def a_ymd_30e360(dias: int):
    años  = dias // 360
    resto = dias % 360
    meses = resto // 30
    dias_f = resto % 30
    return años, meses, dias_f

def hay_traslape(p1, p2) -> bool:
    (i1, f1), (i2, f2) = p1, p2
    return not (f1 < i2 or f2 < i1)

def unir_periodos(periodos):
    if not periodos: return []
    orden = sorted(periodos, key=lambda x: x[0])
    fusion = [orden[0]]
    for ini, fin in orden[1:]:
        u_ini, u_fin = fusion[-1]
        if ini <= u_fin:
            fusion[-1] = (u_ini, max(u_fin, fin))
        else:
            fusion.append((ini, fin))
    return fusion

def recortar_a_referencia(periodos, ref: datetime):
    result = []
    for ini, fin in periodos:
        if fin < ref: continue
        ini2 = max(ini, ref)
        if ini2 <= fin:
            result.append((ini2, fin))
    return result

def parse_fecha(texto: str) -> datetime:
    texto = texto.strip()
    for fmt in ("%d/%m/%Y", "%d-%m-%Y", "%d/%m/%y"):
        try:
            return datetime.strptime(texto, fmt)
        except ValueError:
            pass
    raise ValueError(f"Fecha inválida '{texto}' — use dd/MM/AAAA")

def fmt_total(dias: int) -> str:
    a, m, d = a_ymd_30e360(dias)
    sem = round(dias / 7, 2)
    return f"{a}a {m}m {d}d  ({dias} días, {sem} sem.)"


# ═══════════════════════════════════════════════════════════════════════
#  PALETA DE COLORES
# ═══════════════════════════════════════════════════════════════════════

PALETTE = [
    ("header",      "white",       "dark blue"),
    ("footer",      "white",       "dark gray"),
    ("tab_active",  "black",       "yellow"),
    ("tab_off",     "white",       "dark gray"),
    ("title",       "light cyan,bold", ""),
    ("section",     "light blue,bold", ""),
    ("label",       "light cyan",  ""),
    ("result",      "light green", ""),
    ("error",       "light red",   ""),
    ("warning",     "yellow",      ""),
    ("btn_normal",  "white",       "dark blue"),
    ("btn_calc",    "black",       "light green"),
    ("btn_danger",  "white",       "dark red"),
    ("row_par",     "light gray",  "dark gray"),
    ("row_impar",   "white",       ""),
]


# ═══════════════════════════════════════════════════════════════════════
#  HELPERS DE CONSTRUCCIÓN DE WIDGETS
# ═══════════════════════════════════════════════════════════════════════

def boton(label: str, on_press, style="btn_normal", data=None):
    b = urwid.Button(label, on_press=on_press, user_data=data)
    return urwid.AttrMap(b, style, focus_map="tab_active")

def sep():
    return urwid.Divider("─")

def titulo_seccion(texto: str):
    return urwid.AttrMap(urwid.Text(f" ◆ {texto}", align="left"), "title")

def lbl(texto: str):
    return urwid.AttrMap(urwid.Text(f" {texto}"), "section")

def resultado_widget():
    return urwid.Text("")


# ═══════════════════════════════════════════════════════════════════════
#  APLICACIÓN PRINCIPAL
# ═══════════════════════════════════════════════════════════════════════

class SuiteCalculadoras:

    TABS = [
        "1-Tiempos",
        "2-Horas",
        "3-Edu.Sup.",
        "4-VA",
    ]

    VA_NIVELES = ["Nivel Profesional", "Nivel Asist./Téc./Asesor"]
    VA_TIPOS   = ["Prof.Relacionada/Relacionada", "Profesional/Laboral"]
    VA_GRUPOS  = [
        ("Grupo 1 (360 días)", 360),
        ("Grupo 2 (720 días)", 720),
        ("Grupo 3 (1080 días)", 1080),
        ("Grupo 4 (1440 días)", 1440),
    ]
    HORAS_TIPOS = ["Totales", "Mensuales", "Semanales", "Diarias"]

    def __init__(self):
        self.tab_actual = 0

        # ── Estado global ──────────────────────────────────────────────
        self._msg_widget = urwid.Text("")

        # ── Estado Tab 1: Tiempos ──────────────────────────────────────
        self.t_ref_date   = urwid.Edit(("label", " Fecha ref. (dd/MM/AAAA): "))
        self.t_periodos   = []      # lista de (emp_edit, ini_edit, fin_edit)
        self.t_resultado  = resultado_widget()

        # ── Estado Tab 2: Horas ────────────────────────────────────────
        self.h_tipo       = 0       # 0=Totales 1=Mensuales 2=Semanales 3=Diarias
        self.h_campos     = []      # se reconstruye al cambiar tipo
        self.h_resultado  = resultado_widget()

        # ── Estado Tab 3: Educación Superior ──────────────────────────
        self.e_sem_sol    = urwid.Edit(("label", " Semestres solicitados:      "))
        self.e_cred_apr   = urwid.Edit(("label", " Créditos aprobados:         "))
        self.e_cred_tot   = urwid.Edit(("label", " Créditos totales:           "))
        self.e_sem_prog   = urwid.Edit(("label", " Semestres del programa:     "))
        self.e_resultado  = resultado_widget()

        # ── Estado Tab 4: VA ───────────────────────────────────────────
        self.va_simo1     = urwid.Edit(("label", " Días SIMO (Prof. Relac.):   "))
        self.va_simo2     = urwid.Edit(("label", " Días SIMO (Prof./Laboral):  "))
        self.va_efec1     = urwid.Text(" Días efectivos PR: —")
        self.va_efec2     = urwid.Text(" Días efectivos PL: —")
        self.va_ef1_val   = 0
        self.va_ef2_val   = 0
        self.va_nivel     = 0       # índice en VA_NIVELES
        self.va_tipo      = 0       # índice en VA_TIPOS
        self.va_grupo     = 0       # índice en VA_GRUPOS
        self.va_resultado = resultado_widget()

        # ── Frame principal ────────────────────────────────────────────
        self.loop = None
        self._frame = self._mk_frame()

    # ───────────────────────────────────────────────────────────────────
    #  FRAME / HEADER / FOOTER
    # ───────────────────────────────────────────────────────────────────

    def _mk_header(self):
        app_title = urwid.AttrMap(
            urwid.Text("  SUITE DE CALCULADORAS — Validación de Requisitos",
                       align="left"), "header")
        tabs = []
        for i, nombre in enumerate(self.TABS):
            style = "tab_active" if i == self.tab_actual else "tab_off"
            b = urwid.Button(f" {nombre} ", on_press=self._cambiar_tab, user_data=i)
            tabs.append(("weight", 1, urwid.AttrMap(b, style, focus_map="tab_active")))
        barra_tabs = urwid.Columns(tabs, dividechars=1)
        return urwid.Pile([app_title, barra_tabs])

    def _mk_footer(self):
        return urwid.AttrMap(
            urwid.Text(
                " q: Salir  │  Tab: Siguiente pestaña  │  Flechas: Navegar  │  Enter: Activar",
                align="center"),
            "footer")

    def _mk_frame(self):
        return urwid.Frame(
            body=self._mk_body(),
            header=self._mk_header(),
            footer=self._mk_footer(),
        )

    def _refresh(self):
        self._frame.header = self._mk_header()
        self._frame.body   = self._mk_body()

    def _mk_body(self):
        handlers = {
            0: self._widgets_tiempos,
            1: self._widgets_horas,
            2: self._widgets_edu,
            3: self._widgets_va,
        }
        widgets = handlers[self.tab_actual]()
        widgets += [sep(), self._msg_widget, urwid.Text("")]
        return urwid.ListBox(urwid.SimpleFocusListWalker(widgets))

    def _set_msg(self, texto: str, tipo: str = "result"):
        self._msg_widget.set_text((tipo, f" {texto}"))

    def _cambiar_tab(self, btn, idx: int):
        self.tab_actual = idx
        self._set_msg("")
        self._refresh()

    # ═══════════════════════════════════════════════════════════════════
    #  TAB 1 — CALCULADORA DE TIEMPOS
    # ═══════════════════════════════════════════════════════════════════

    def _widgets_tiempos(self):
        w = [
            titulo_seccion("CALCULADORA DE TIEMPOS — Periodos Laborales"),
            sep(),
            lbl("Fecha de Grado / Término Materias (dejar vacío si no aplica):"),
            self.t_ref_date,
            sep(),
            lbl("PERIODOS LABORALES:"),
            urwid.Text("  Empresa                    │ Inicio (dd/MM/AAAA) │ Final (dd/MM/AAAA)"),
            urwid.Divider("─"),
        ]
        for i, (emp, ini, fin) in enumerate(self.t_periodos):
            fila = urwid.Columns([
                ("weight", 3, emp),
                ("weight", 2, ini),
                ("weight", 2, fin),
            ], dividechars=1)
            estilo = "row_par" if i % 2 == 0 else "row_impar"
            w.append(urwid.AttrMap(fila, estilo))

        w += [
            urwid.Divider("─"),
            urwid.Columns([
                ("weight", 1, boton(" (+) Agregar ",  self._t_agregar)),
                ("weight", 1, boton(" (-) Eliminar ", self._t_eliminar)),
                ("weight", 1, boton(" Calcular ",     self._t_calcular, "btn_calc")),
                ("weight", 1, boton(" Limpiar Todo ", self._t_limpiar,  "btn_danger")),
            ], dividechars=1),
            sep(),
            lbl("RESULTADOS:"),
            self.t_resultado,
        ]
        return w

    def _t_agregar(self, btn=None):
        emp = urwid.Edit(" Empresa: ")
        ini = urwid.Edit(" Inicio: ")
        fin = urwid.Edit(" Final:  ")
        self.t_periodos.append((emp, ini, fin))
        self._set_msg(f"Periodo {len(self.t_periodos)} agregado. Complete los campos.")
        self._refresh()

    def _t_eliminar(self, btn=None):
        if self.t_periodos:
            self.t_periodos.pop()
            self._set_msg(f"Último periodo eliminado.")
            self._refresh()
        else:
            self._set_msg("No hay periodos para eliminar.", "warning")

    def _t_limpiar(self, btn=None):
        self.t_periodos.clear()
        self.t_ref_date.set_edit_text("")
        self.t_resultado.set_text("")
        self._set_msg("Calculadora de tiempos limpiada.")
        self._refresh()

    def _t_calcular(self, btn=None):
        try:
            ref_txt = self.t_ref_date.edit_text.strip()
            REF = parse_fecha(ref_txt) if ref_txt else None

            periodos = []
            min_date = None

            for emp_w, ini_w, fin_w in self.t_periodos:
                ini = parse_fecha(ini_w.edit_text)
                fin = parse_fecha(fin_w.edit_text)
                if fin < ini:
                    raise ValueError(
                        f"Fecha final < inicial en '{emp_w.edit_text.strip() or 'sin nombre'}'")
                periodos.append((ini, fin))
                if min_date is None or ini < min_date:
                    min_date = ini

            if not periodos:
                raise ValueError("Agrega al menos un periodo antes de calcular.")

            if REF is None:
                REF = min_date if min_date else datetime.now()

            detalles = []
            for idx, ((emp_w, ini_w, fin_w), (ini, fin)) in enumerate(
                    zip(self.t_periodos, periodos)):
                nombre = emp_w.edit_text.strip() or f"Periodo {idx + 1}"
                d      = dias_30e360_mas1(ini, fin)
                ymd    = a_ymd_30e360(d)
                sem    = round(d / 7, 2)
                tras   = any(hay_traslape((ini, fin), p)
                             for j, p in enumerate(periodos) if j != idx)
                ant    = ini < REF
                detalles.append((nombre, ini, fin, d, sem, ymd, tras, ant))

            total_con      = sum(d for (_, _, _, d, _, _, _, _) in detalles)
            fusion_global  = unir_periodos(periodos)
            total_sin      = sum(dias_30e360_mas1(i, f) for i, f in fusion_global)
            recortados     = recortar_a_referencia(periodos, REF)
            total_sin_post = sum(dias_30e360_mas1(i, f)
                                 for i, f in unir_periodos(recortados))

            lineas = ["━" * 58]
            for i, (n, ini, fin, d, sem, (a, m, dd), tras, ant) in enumerate(detalles, 1):
                aviso_t   = "  ⚠ TRASLAPE" if tras else ""
                aviso_ant = "  (ant. a referencia)" if ant else ""
                lineas.append(
                    f"Periodo {i}: {n}{aviso_t}{aviso_ant}\n"
                    f"  {ini.strftime('%d/%m/%Y')} → {fin.strftime('%d/%m/%Y')}\n"
                    f"  {a}a {m}m {dd}d  │  {d} días  │  {sem} semanas"
                )
            lineas += [
                "━" * 58,
                f"Con traslapes        :  {fmt_total(total_con)}",
                f"Sin traslapes        :  {fmt_total(total_sin)}",
                f"Sin tral./post-ref.  :  {fmt_total(total_sin_post)}",
                f"Fecha de referencia  :  {REF.strftime('%d/%m/%Y')}",
            ]
            self.t_resultado.set_text(("result", "\n".join(lineas)))
            self._set_msg(f"✓ Cálculo completado — {len(detalles)} periodo(s).")
        except ValueError as e:
            self.t_resultado.set_text(("error", str(e)))
            self._set_msg(f"✗ {e}", "error")
        self._refresh()

    # ═══════════════════════════════════════════════════════════════════
    #  TAB 2 — CALCULADORA DE HORAS
    # ═══════════════════════════════════════════════════════════════════

    def _widgets_horas(self):
        # Botonera de tipo
        tipo_cols = []
        for i, nombre in enumerate(self.HORAS_TIPOS):
            style = "tab_active" if i == self.h_tipo else "btn_normal"
            b = urwid.Button(f" {nombre} ",
                             on_press=self._h_set_tipo, user_data=i)
            tipo_cols.append(("weight", 1,
                               urwid.AttrMap(b, style, focus_map="tab_active")))

        # Campos dinámicos según tipo seleccionado
        if self.h_tipo == 0:
            self.h_campos = [urwid.Edit(("label", " Horas totales certificadas:   "))]
            desc = "Total horas / 8 = días laborales"
        elif self.h_tipo == 1:
            self.h_campos = [
                urwid.Edit(("label", " Número de meses:              ")),
                urwid.Edit(("label", " Horas mensuales certificadas: ")),
            ]
            desc = "Meses × horas_mes / 8 = días laborales"
        elif self.h_tipo == 2:
            self.h_campos = [
                urwid.Edit(("label", " Número de semanas:            ")),
                urwid.Edit(("label", " Horas semanales certificadas: ")),
            ]
            desc = "Semanas × horas_sem / 8 = días laborales"
        else:
            self.h_campos = [
                urwid.Edit(("label", " Número de días:               ")),
                urwid.Edit(("label", " Horas diarias certificadas:   ")),
            ]
            desc = "Días × horas_día / 8 = días laborales"

        w = [
            titulo_seccion("CONVERSOR DE HORAS LABORALES"),
            sep(),
            lbl("Tipo de cálculo:"),
            urwid.Columns(tipo_cols, dividechars=1),
            sep(),
            urwid.Text(("warning", f"  Fórmula: {desc}")),
            sep(),
        ]
        w += self.h_campos
        w += [
            sep(),
            boton(" CALCULAR ", self._h_calcular, "btn_calc"),
            sep(),
            lbl("RESULTADO:"),
            self.h_resultado,
        ]
        return w

    def _h_set_tipo(self, btn, idx: int):
        self.h_tipo = idx
        self.h_resultado.set_text("")
        self._set_msg("")
        self._refresh()

    def _h_calcular(self, btn=None):
        try:
            vals = [int(ed.edit_text.strip()) for ed in self.h_campos]
            if self.h_tipo == 0:
                dias = round(vals[0] / 8)
            else:
                dias = round(vals[0] * vals[1] / 8)
            self.h_resultado.set_text(
                ("result", f"  Total días laborales equivalentes: {dias}"))
            self._set_msg(f"✓ Resultado: {dias} días laborales.")
        except (ValueError, IndexError):
            self._set_msg("✗ Ingrese valores numéricos enteros en todos los campos.", "error")
        self._refresh()

    # ═══════════════════════════════════════════════════════════════════
    #  TAB 3 — CALCULADORA DE EDUCACIÓN SUPERIOR
    # ═══════════════════════════════════════════════════════════════════

    def _widgets_edu(self):
        return [
            titulo_seccion("CALCULADORA DE EDUCACIÓN SUPERIOR"),
            sep(),
            lbl("SEMESTRES SOLICITADOS:"),
            self.e_sem_sol,
            sep(),
            lbl("VALORES DE MEDICIÓN:"),
            self.e_cred_apr,
            self.e_cred_tot,
            self.e_sem_prog,
            sep(),
            boton(" CALCULAR SEMESTRES ", self._edu_calcular, "btn_calc"),
            sep(),
            lbl("RESULTADO:"),
            self.e_resultado,
            sep(),
            urwid.Text(("warning",
                "  Fórmula: (créditos_aprobados / créditos_totales) × semestres_programa")),
        ]

    def _edu_calcular(self, btn=None):
        try:
            sol  = int(self.e_sem_sol.edit_text.strip())
            apr  = int(self.e_cred_apr.edit_text.strip())
            tot  = int(self.e_cred_tot.edit_text.strip())
            prog = int(self.e_sem_prog.edit_text.strip())
            if tot == 0:
                raise ZeroDivisionError
            total  = (apr / tot) * prog
            cumple = total >= sol
            icono  = "✓" if cumple else "✗"
            estado = "CUMPLE con los semestres" if cumple else "NO CUMPLE con los semestres"
            self.e_resultado.set_text(
                ("result" if cumple else "error",
                 f"  {icono} {estado}\n"
                 f"  Semestres solicitados:    {sol}\n"
                 f"  Semestres equivalentes:   {total:.2f}"))
            self._set_msg(f"✓ {estado} ({total:.2f} ≥ {sol})" if cumple
                          else f"✗ {estado} ({total:.2f} < {sol})",
                          "result" if cumple else "warning")
        except ZeroDivisionError:
            self._set_msg("✗ El número de créditos totales no puede ser 0.", "error")
        except ValueError:
            self._set_msg("✗ Ingrese valores numéricos enteros en todos los campos.", "error")
        self._refresh()

    # ═══════════════════════════════════════════════════════════════════
    #  TAB 4 — CALCULADORA VA
    # ═══════════════════════════════════════════════════════════════════

    def _widgets_va(self):
        nivel_lbl = self.VA_NIVELES[self.va_nivel]
        tipo_lbl  = self.VA_TIPOS[self.va_tipo]
        grupo_lbl = self.VA_GRUPOS[self.va_grupo][0]

        return [
            titulo_seccion("CALCULADORA VA — Según Grupo de Empleo"),
            sep(),
            lbl("1. CONVERSIÓN SIMO → DÍAS EFECTIVOS:"),
            self.va_simo1,
            self.va_simo2,
            boton(" Calcular días efectivos ", self._va_calc_efectivos, "btn_calc"),
            self.va_efec1,
            self.va_efec2,
            sep(),
            lbl("2. NIVEL (presionar para cambiar):"),
            urwid.Text(f"  Seleccionado: {nivel_lbl}"),
            boton(f" Cambiar nivel ↺ ({nivel_lbl}) ",
                  self._va_ciclo_nivel),
            sep(),
            lbl("3. TIPO DE EXPERIENCIA (presionar para cambiar):"),
            urwid.Text(f"  Seleccionado: {tipo_lbl}"),
            boton(f" Cambiar tipo ↺ ({tipo_lbl}) ",
                  self._va_ciclo_tipo),
            sep(),
            lbl("4. GRUPO DE EMPLEO (presionar para cambiar):"),
            urwid.Text(f"  Seleccionado: {grupo_lbl}"),
            boton(f" Cambiar grupo ↺ ({grupo_lbl}) ",
                  self._va_ciclo_grupo),
            sep(),
            boton(" CALCULAR PUNTAJES ", self._va_calc_puntajes, "btn_calc"),
            sep(),
            lbl("RESULTADOS:"),
            self.va_resultado,
        ]

    def _va_calc_efectivos(self, btn=None):
        try:
            s1 = float(self.va_simo1.edit_text.strip())
            s2 = float(self.va_simo2.edit_text.strip())
            self.va_ef1_val = round(s1 * 30)
            self.va_ef2_val = round(s2 * 30)
            self.va_efec1.set_text(
                ("result", f"  Días efectivos Prof. Relacionada: {self.va_ef1_val}"))
            self.va_efec2.set_text(
                ("result", f"  Días efectivos Prof./Laboral:     {self.va_ef2_val}"))
            self._set_msg("✓ Días efectivos calculados correctamente.")
        except ValueError:
            self._set_msg("✗ Ingrese valores numéricos válidos.", "error")
        self._refresh()

    def _va_ciclo_nivel(self, btn=None):
        self.va_nivel = (self.va_nivel + 1) % len(self.VA_NIVELES)
        self._refresh()

    def _va_ciclo_tipo(self, btn=None):
        self.va_tipo = (self.va_tipo + 1) % len(self.VA_TIPOS)
        self._refresh()

    def _va_ciclo_grupo(self, btn=None):
        self.va_grupo = (self.va_grupo + 1) % len(self.VA_GRUPOS)
        self._refresh()

    def _va_calc_puntajes(self, btn=None):
        if self.va_ef1_val == 0 and self.va_ef2_val == 0:
            self._set_msg("✗ Primero calcule los días efectivos.", "error")
            self._refresh()
            return
        dias_base = self.VA_GRUPOS[self.va_grupo][1]
        nivel = self.va_nivel
        tipo  = self.va_tipo

        if nivel == 0:   # Nivel Profesional
            if tipo == 0:
                p1 = min(round(self.va_ef1_val * 40 / dias_base, 2), 40)
                p2 = min(round(self.va_ef2_val * 15 / dias_base, 2), 15)
            else:
                p1 = min(round(self.va_ef1_val * 15 / dias_base, 2), 15)
                p2 = min(round(self.va_ef2_val * 40 / dias_base, 2), 40)
        else:            # Nivel NATA
            if tipo == 0:
                p1 = min(round(self.va_ef1_val * 40 / dias_base, 2), 40)
                p2 = min(round(self.va_ef2_val * 10 / dias_base, 2), 10)
            else:
                p1 = min(round(self.va_ef1_val * 10 / dias_base, 2), 10)
                p2 = min(round(self.va_ef2_val * 40 / dias_base, 2), 40)

        self.va_resultado.set_text(
            ("result",
             f"  Puntaje Prof. Relacionada : {p1}\n"
             f"  Puntaje Prof./Laboral      : {p2}\n"
             f"  ─────────────────────────────────\n"
             f"  Nivel  : {self.VA_NIVELES[nivel]}\n"
             f"  Tipo   : {self.VA_TIPOS[tipo]}\n"
             f"  Grupo  : {self.VA_GRUPOS[self.va_grupo][0]}"))
        self._set_msg(f"✓ Puntajes — PR: {p1}  │  PL: {p2}")
        self._refresh()

    # ═══════════════════════════════════════════════════════════════════
    #  MAIN LOOP
    # ═══════════════════════════════════════════════════════════════════

    def run(self):
        self.loop = urwid.MainLoop(
            self._frame,
            PALETTE,
            unhandled_input=self._teclas_globales,
        )
        self.loop.run()

    def _teclas_globales(self, key):
        if key in ("q", "Q"):
            raise urwid.ExitMainLoop()
        if key == "tab":
            self.tab_actual = (self.tab_actual + 1) % len(self.TABS)
            self._set_msg("")
            self._refresh()


# ═══════════════════════════════════════════════════════════════════════
#  PUNTO DE ENTRADA
# ═══════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    SuiteCalculadoras().run()