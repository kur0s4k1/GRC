# Estándares Industriales (OT / ICS / SCADA)

Referencia de los estándares específicos de **entornos industriales y de control**: plantas, manufactura, energía, agua, oil & gas, transporte y utilities. Los entornos OT priorizan **disponibilidad y seguridad física** sobre confidencialidad, por lo que requieren controles propios más allá del SGSI general.

---

## IEC 62443 (ISA-99) — Seguridad en sistemas de automatización y control industrial

Estándar de referencia para **ciberseguridad OT**. Estructura en cuatro series:

| Serie | Alcance |
|---|---|
| **62443-1-x** | Generalidades, terminología, conceptos y modelos |
| **62443-2-x** | Requisitos del **sistema de gestión de seguridad** del operador (2-1) y de patch management (2-3) |
| **62443-3-x** | Seguridad de **sistemas** — 3-2 evaluación de riesgo y diseño; 3-3 requisitos de seguridad de sistema |
| **62443-4-x** | Seguridad del **producto** — 4-1 ciclo de vida seguro de desarrollo; 4-2 requisitos técnicos por componente |

### Conceptos clave

- **Zonas y conductos (zones & conduits)** — segmentación lógica de activos por criticidad y control de flujos mediante conductos.
- **Security Levels (SL 0–4)**: SL1 (protección contra amenaza casual), SL2 (intencional simple), SL3 (sofisticada), SL4 (estatal/nación).
- **FR (Foundational Requirements)**: 7 requisitos — IAC, Use Control, Data Integrity, Data Confidentiality, Restricted Data Flow, Timely Response to Events, Resource Availability.
- **SL-T / SL-C / SL-A**: objetivo, capacidad y nivel alcanzado de cada zona.

---

## NIST SP 800-82 Rev.3 — Guía de seguridad OT

Guía práctica de **NIST** para seguridad de sistemas de control industrial, con arquitecturas de referencia, controles (derivados de SP 800-53) y consideraciones para nubes y despliegues remotos. Complementa a IEC 62443.

---

## Modelo Purdue — Arquitectura de referencia ISA-95

**Segmentación por niveles** de la red industrial (referencia, no control):

```text
Nivel 4/5  ─ Empresa (ERP, DMZ IT)          ┐ IT
Nivel 3.5  ─ IT/OT DMZ (historiador, jumphost)┘
Nivel 3    ─ Operaciones / MES / site
Nivel 2    ─ Supervisión (SCADA, HMI)
Nivel 1    ─ Control (PLC, RTU, DCS)
Nivel 0    ─ Proceso físico (sensores, actuadores)
```

> La convergencia IT/OT hace crítico el aislamiento del Nivel 0–2 y el uso de DMZ industriales.

---

## Otros estándares industriales relevantes

| Estándar | Sector / propósito |
|---|---|
| **IEC 61508** | Seguridad funcional (Safety Integrity Level, SIL 1–4) |
| **IEC 61511** | Seguridad funcional en la industria de procesos |
| **ISO/IEC 27019** | Seguridad de la información en sistemas de control del **sector energía** |
| **NERC CIP** | Protección de infraestructura crítica eléctrica en Norteamérica (CIP-002 a CIP-014) |
| **IEEE 1686** | Seguridad de IEDs (dispositivos electrónicos inteligentes) en subestaciones |
| **IEEE 1402 / NESC** | Seguridad física en subestaciones eléctricas |
| **API 1164** | Ciberseguridad de SCADA en ductos (oil & gas) |
| **IEC 61850 / DNP3** | Protocolos de comunicación en subestaciones y control remoto |
| **OPC UA (IEC 62541)** | Protocolo de interoperabilidad industrial con modelo de seguridad |
| **IEC 62351** | Seguridad de las comunicaciones en sistemas de potencia (con IEC 61850/DNP3) |
| **ISO 22301 / ISO 27031** | Continuidad de negocio y continuidad de TIC (aplicable a OT) |
| **NIS2 / DORA / CRA (UE)** | Regulación sectorial que alcanza operadores de infraestructura crítica |

---

## Puente OT ↔ ISO/IEC 27001

- **ISO/IEC 27019** adapta 27002 al sector energía — punto de unión natural.
- **IEC 62443-2-1** define un **SMSS** (Security Management System for IACS) que se mapea a las cláusulas 4–10 de ISO/IEC 27001.
- En un SGSI ya implantado, los controles de Anexo A se complementan con las zonas/conductos y los SL de 62443 para el alcance OT.

---

## Uso responsable

Material de referencia. Las normas IEC/ISO/IEEE son de pago; consultar el texto oficial para requisitos normativos completos.

<p align="center"><sub>IEC 62443 · NIST 800-82 · NERC CIP · IEC 61508/61511 · ISO 27019 · Purdue</sub></p>
