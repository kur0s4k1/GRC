# GRC — Gobernanza, Riesgo y Cumplimiento

Portafolio de **Governance, Risk & Compliance**: marcos de referencia, normativas legales y estándares industriales, metodología de gestión de riesgo, controles y plantillas listas para implementar en un SGSI alineado a **ISO/IEC 27001** y a las principales regulaciones sectoriales.

> Del control al cumplimiento: cada norma mapeada a controles accionables, evidencias esperadas y métricas de madurez.

---

## Estructura del repositorio

```text
GRC/
├── marcos/                 # Frameworks y estándares de seguridad
│   ├── iso-27001/          # ISO/IEC 27001, 27002, 27005, familia 27000
│   ├── nist/               # NIST CSF 2.0, SP 800-53, 800-171, 800-30
│   ├── otros-marcos/       # COBIT, CIS v8, SOC 2, ISO 31000, 22301
│   └── industriales/       # IEC 62443, NIST 800-82, NERC CIP, IEC 61508/61511
├── normativas-legales/     # Chile, UE, EE.UU. — mapeo regulatorio
├── riesgo/                 # Metodología de análisis y tratamiento de riesgo
└── plantillas/             # Políticas, SoA, registro de riesgos, KPIs
```

| Sección | Contenido |
|---|---|
| [`marcos/iso-27001`](marcos/iso-27001) | [Ruta para implementar y mantener el SGSI](marcos/iso-27001/implementar-y-mantener-sgsi.md), controles Anexo A (93), declaración de aplicabilidad, familia ISO 27000, [herramientas por control](marcos/iso-27001/herramientas-vs-manual-iso-27002.md) y [herramientas transversales](marcos/iso-27001/herramientas-transversales-sgsi.md) |
| [`marcos/nist`](marcos/nist) | CSF 2.0, SP 800-53 Rev.5, SP 800-171, gestión de riesgo (800-30) |
| [`marcos/otros-marcos`](marcos/otros-marcos) | COBIT 2019, CIS Controls v8.1, SOC 2, ISO 31000, ISO 22301 |
| [`marcos/industriales`](marcos/industriales) | IEC 62443 (OT/ICS), NIST SP 800-82, NERC CIP, IEC 61508/61511, ISO 27019, PCI DSS |
| [`normativas-legales`](normativas-legales) | Ley 21.663 y 21.719 (Chile), GDPR, NIS2, DORA, CRA, HIPAA |
| [`riesgo`](riesgo) | Metodología ISO 31000 / ISO/IEC 27005, escalas, tratamiento, apetito de riesgo |
| [`plantillas`](plantillas) | Política de seguridad, SoA, registro de riesgos, plan de tratamiento, KPI/KRI |

---

## 🎯 Enfoque

- **Gobernanza** — roles, políticas, comités, métricas y mejora continua del SGSI.
- **Riesgo** — identificación, análisis, evaluación y tratamiento bajo ISO 31000 / ISO/IEC 27005.
- **Cumplimiento** — mapeo de requisitos legales, regulatorios y contractuales a controles verificables.
- **Resiliencia** — continuidad de negocio (ISO 22301), gestión de incidentes (ISO 27035) y ciberseguridad OT/ICS.
- **Puente con lo técnico** — cada control se traduce en evidencia auditable y en telemetría de seguridad.

---

## 📚 Alcance normativo cubierto

**Seguridad de la información (general):** ISO/IEC 27001 · ISO/IEC 27002 · ISO/IEC 27005 · ISO/IEC 27701 · ISO 31000 · ISO 22301 · NIST CSF 2.0 · NIST SP 800-53 · CIS Controls v8 · COBIT 2019 · SOC 2 · ITIL 4.

**Industriales / OT-ICS:** IEC 62443 (ISA-99) · NIST SP 800-82 Rev.3 · NERC CIP · IEC 61508 (SIL) · IEC 61511 · ISO/IEC 27019 · IEEE 1686 · API 1164 · Modelo Purdue.

**Regulatorias (por jurisdicción):** Chile — Ley 21.663 (Marco de Ciberseguridad), Ley 21.719 (Protección de Datos), Ley 19.628. UE — GDPR, NIS2, DORA, Cyber Resilience Act. EE.UU. — HIPAA, FISMA, SOX, GLBA. Pago — PCI DSS v4.0.

---

## ⚠️ Aviso

El contenido de este repositorio es material **de referencia y educativo** sobre marcos de gobernanza, riesgo y cumplimiento. No reproduce texto normativo de pago ni sustituye la lectura de la norma oficial; las plantillas son adaptables y deben validarse según el contexto, el alcance y la jurisdicción de cada organización.

---

## Licencia

Distribuido bajo licencia **MIT** — ver [`LICENSE`](LICENSE).

<p align="center"><sub>GRC · ISO/IEC 27001 · Riesgo · Cumplimiento · Resiliencia OT/ICS</sub></p>
