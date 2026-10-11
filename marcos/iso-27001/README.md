# ISO/IEC 27001 — Sistema de Gestión de Seguridad de la Información (SGSI)

Referencia del estándar internacional para establecer, implementar, mantener y mejorar un **Sistema de Gestión de Seguridad de la Información (SGSI)**, junto con su familia de normas de apoyo.

---

## ISO/IEC 27001:2022 — requisitos

Define los requisitos del SGSI. Su estructura sigue el **Anexo SL** (High-Level Structure) común a los sistemas de gestión ISO:

**Guía práctica:** [herramientas frente a gestión manual para los 93 controles de ISO/IEC 27002:2022](herramientas-vs-manual-iso-27002.md). Incluye precios públicos, reseñas, límites de cada herramienta y riesgos que deben evaluarse al contratar proveedores.

1. Objeto y campo de aplicación
2. Referencias normativas
3. Términos y definiciones
4. **Contexto de la organización**
5. **Liderazgo**
6. **Planificación**
7. **Apoyo**
8. **Operación**
9. **Evaluación del desempeño**
10. **Mejora**

### Anexo A — 93 controles en 4 temas

| Tema | Cláusula | N.º de controles |
|---|---|---:|
| **Organizacionales** | A.5 | 37 |
| **Personas** | A.6 | 8 |
| **Físicos** | A.7 | 14 |
| **Tecnológicos** | A.8 | 34 |
| **Total** | | **93** |

> En la revisión 2022 los controles se reorganizaron desde las 14 cláusulas del Anexo A de 2013 hacia estos 4 temas, con 11 controles nuevos (p. ej. *threat intelligence*, *cloud services*, *data masking*, *data leakage prevention*, *secure coding*, *monitoring activities*, *web filtering*, *configuration management*, *information deletion*, *physical security monitoring*, *ICT readiness for business continuity*).

### Documentación mínima esperada

- Alcance del SGSI
- Política de seguridad de la información
- Metodología de evaluación y tratamiento de riesgo
- **Declaración de Aplicabilidad (SoA)**
- Plan de tratamiento de riesgo
- Objetivos de seguridad y planificación
- Evidencia de competencia, concienciación y comunicación
- Resultados de seguimiento, auditoría interna, revisión por la dirección y no conformidades

---

## Familia ISO/IEC 27000 (apoyo relevante)

| Norma | Propósito |
|---|---|
| **ISO/IEC 27000** | Visión general y vocabulario |
| **ISO/IEC 27002:2022** | Guía de implementación de los 93 controles del Anexo A |
| **ISO/IEC 27003** | Directrices de implementación del SGSI |
| **ISO/IEC 27004** | Medición del desempeño del SGSI (métricas) |
| **ISO/IEC 27005** | Gestión de riesgos de seguridad de la información |
| **ISO/IEC 27017 / 27018** | Controles de seguridad y privacidad en cloud |
| **ISO/IEC 27019** | Seguridad en sistemas de control industrial del sector energía |
| **ISO/IEC 27032 / 27033** | Ciberseguridad y seguridad de redes |
| **ISO/IEC 27035** | Gestión de incidentes de seguridad de la información |
| **ISO/IEC 27037** | Identificación, recolección y preservación de evidencia digital |
| **ISO/IEC 27701** | Extensión de privacidad (PIMS), alineada a ISO 27001/27002 |
| **ISO/IEC 27031 / ISO 22301** | Continuidad de TIC y continuidad de negocio |

---

## Ciclo de vida del SGSI (PDCA)

```text
Plan  → contexto, riesgos, objetivos, SoA
Do    → operación de controles, competencia, documentación
Check → monitoreo, auditoría interna, revisión por la dirección
Act   → no conformidades, acciones correctivas, mejora continua
```

---

## Relación con otras normas

- **ISO/IEC 27001 ↔ NIST CSF 2.0** — mapeo de funciones (Govern/Identify/Protect/Detect/Respond/Recover) a cláusulas y controles del Anexo A.
- **ISO/IEC 27001 ↔ ISO/IEC 27005** — 27001 exige un proceso de gestión de riesgo; 27005 lo detalla.
- **ISO/IEC 27001 ↔ IEC 62443** — para entornos OT/ICS, 27019 y 62443 complementan el SGSI con controles específicos de sistemas de control.

---

## Uso responsable

Este documento es material de referencia. La norma oficial es de pago y debe consultarse directamente en ISO/IEC. Las plantillas de [`../../plantillas`](../../plantillas) son adaptables y deben validarse según el alcance y el contexto de cada organización.

<p align="center"><sub>ISO/IEC 27001:2022 · SGSI · 93 controles · Anexo A</sub></p>
