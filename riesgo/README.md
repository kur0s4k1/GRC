# Gestión de Riesgo — Metodología

Metodología de análisis, evaluación y tratamiento de riesgo de seguridad de la información, alineada a **ISO 31000** e **ISO/IEC 27005**, y compatible con **NIST SP 800-30** y **NIST CSF 2.0 (Govern)**.

---

## Proceso de gestión de riesgo

```text
1. Establecimiento del contexto   (alcance, criterios, apetito de riesgo)
2. Identificación de riesgos      (activos, amenazas, vulnerabilidades, impacto)
3. Análisis de riesgos            (probabilidad × impacto, causas y consecuencias)
4. Evaluación de riesgos          (comparación con criterios; nivel de riesgo)
5. Tratamiento de riesgos         (mitigar / evitar / transferir / aceptar)
6. Aceptación y comunicación      (propietario del riesgo, aprobación)
7. Monitoreo y revisión           (KRI/KPI, reevaluación periódica)
```

Procesos **transversales**: comunicación y consulta, y seguimiento y revisión.

---

## Escalas de valoración

### Probabilidad (Likelihood)

| Valor | Nivel | Descripción |
|:--:|---|---|
| 1 | Rara | Puede ocurrir solo en circunstancias excepcionales |
| 2 | Improbable | Podría ocurrir en algún momento |
| 3 | Posible | Podría ocurrir ocasionalmente |
| 4 | Probable | Probablemente ocurrirá en la mayoría de circunstancias |
| 5 | Casi segura | Se espera que ocurra |

### Impacto (Consequences)

| Valor | Nivel | Descripción |
|:--:|---|---|
| 1 | Insignificante | Sin efecto material |
| 2 | Menor | Efecto limitado, sin pérdida de servicio |
| 3 | Moderado | Degradación parcial o exposición acotada |
| 4 | Mayor | Interrupción relevante o exposición significativa de datos |
| 5 | Severo | Interrupción crítica, incumplimiento legal o impacto físico/safety |

### Nivel de riesgo = Probabilidad × Impacto

| | **1** | **2** | **3** | **4** | **5** |
|---|---|---|---|---|---|
| **5** | 5 🟠 | 10 🔴 | 15 🔴 | 20 🔴 | 25 🔴 |
| **4** | 4 🟡 | 8 🟠 | 12 🔴 | 16 🔴 | 20 🔴 |
| **3** | 3 🟡 | 6 🟠 | 9 🟠 | 12 🔴 | 15 🔴 |
| **2** | 2 🟢 | 4 🟡 | 6 🟠 | 8 🟠 | 10 🔴 |
| **1** | 1 🟢 | 2 🟢 | 3 🟡 | 4 🟡 | 5 🟠 |

🟢 Bajo (1–3) · 🟡 Medio-bajo (4–6) · 🟠 Medio-alto (8–10) · 🔴 Alto (12–25)

---

## Opciones de tratamiento

| Opción | Cuándo aplica |
|---|---|
| **Mitigar** | Aplicar controles para reducir probabilidad o impacto |
| **Evitar** | Eliminar la actividad o el activo que genera el riesgo |
| **Transferir** | Seguro, ciberseguro o tercerización con SLA |
| **Aceptar** | Riesgo residual dentro del apetito de riesgo (con aprobación del propietario) |

Cada tratamiento debe registrar: control seleccionado, responsable, fecha objetivo, costo, riesgo residual y estado.

---

## Registro y métricas

- **Registro de riesgos** — ver plantilla [`../plantillas/registro-riesgos.csv`](../plantillas/registro-riesgos.csv).
- **Plan de tratamiento** — acciones, responsables, plazos y estado.
- **KRI (Key Risk Indicators)** — señales tempranas (p. ej. vulnerabilidades críticas abiertas, tiempo de remediación).
- **KPI (Key Performance Indicators)** — desempeño del programa (cobertura de control, cumplimiento de SLA).

---

## Apetito y tolerancia al riesgo

- **Apetito de riesgo**: nivel de riesgo que la organización está dispuesta a asumir para lograr sus objetivos.
- **Tolerancia**: desviación aceptable respecto al objetivo.
- **Capacidad**: riesgo máximo asumible sin comprometer la viabilidad.

---

## Integración con otros marcos

- **ISO/IEC 27005** — metodología detallada para riesgo de seguridad de la información.
- **NIST SP 800-30 / 800-37** — evaluación de riesgo y RMF.
- **ISO 31000** — marco genérico, aplicable a riesgos no técnicos.
- **IEC 62443-3-2** — evaluación de riesgo en entornos OT/ICS.

<p align="center"><sub>ISO 31000 · ISO/IEC 27005 · NIST SP 800-30 · Riesgo residual</sub></p>
