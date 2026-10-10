# Declaración de Aplicabilidad (SoA) — Plantilla

**Organización:** `<ORGANIZACIÓN>`
**SGSI / Alcance:** `<ALCANCE>`
**Versión:** `1.0` · **Fecha:** `AAAA-MM-DD` · **Responsable:** `<NOMBRE / ROL>`
**Base normativa:** ISO/IEC 27001:2022 — Anexo A (93 controles)

> Instrucciones: para cada control indicar si es **aplicable (S/N)**, su **justificación**, el **estado de implementación** y la **evidencia**. Los controles no aplicables deben justificarse (exclusión válida).

---

## A.5 — Controles organizacionales (37)

| Control | Título | Aplicable | Justificación | Estado | Evidencia |
|---|---|:--:|---|---|---|
| A.5.1 | Políticas de seguridad de la información | S | Requisito base del SGSI | Implementado | `POL-SEG-001` |
| A.5.2 | Roles y responsabilidades de seguridad | S | Definición de RACI | Implementado | Matriz RACI |
| A.5.3 | Segregación de funciones | S | Reducir fraude/error | Parcial | Descripción de puestos |
| … | … | | | | |

## A.6 — Controles de personas (8)

| Control | Título | Aplicable | Justificación | Estado | Evidencia |
|---|---|:--:|---|---|---|
| A.6.1 | Selección | S | Debida diligencia previa | Implementado | Política RRHH |
| A.6.2 | Términos y condiciones de empleo | S | Obligaciones de confidencialidad | Implementado | Contrato / NDA |
| A.6.3 | Concienciación, educación y formación | S | Factor humano | En curso | Programa de formación |
| … | … | | | | |

## A.7 — Controles físicos (14)

| Control | Título | Aplicable | Justificación | Estado | Evidencia |
|---|---|:--:|---|---|---|
| A.7.1 | Perímetros de seguridad física | S | Data center propio | Implementado | Plano + control acceso |
| A.7.4 | Monitoreo de seguridad física | S | Detección de intrusión | Implementado | CCTV + logs |
| … | … | | | | |

## A.8 — Controles tecnológicos (34)

| Control | Título | Aplicable | Justificación | Estado | Evidencia |
|---|---|:--:|---|---|---|
| A.8.2 | Derechos de acceso privilegiado | S | Mínimo privilegio | Parcial | PAM / revisión de accesos |
| A.8.5 | Autenticación segura | S | Proteger identidades | Implementado | MFA + política |
| A.8.8 | Gestión de vulnerabilidades técnicas | S | Reducción de superficie | Implementado | Escaneos + SLA remediación |
| A.8.15 | Registro (logging) | S | Detección y forense | Implementado | SIEM / retención |
| A.8.24 | Uso de criptografía | S | Confidencialidad | Implementado | Política criptográfica |
| … | … | | | | |

---

## Resumen de aplicabilidad

| Tema | Total | Aplicables | No aplicables | Implementados | Parciales | Pendientes |
|---|---:|---:|---:|---:|---:|---:|
| A.5 Organizacionales | 37 | | | | | |
| A.6 Personas | 8 | | | | | |
| A.7 Físicos | 14 | | | | | |
| A.8 Tecnológicos | 34 | | | | | |
| **Total** | **93** | | | | | |

## Exclusiones y justificación

| Control | Motivo de exclusión |
|---|---|
| _ej. A.7.x_ | _No se gestionan instalaciones físicas propias; servicio 100% cloud con controles heredados del proveedor._ |

---

**Aprobado por:** `<NOMBRE>` · **Fecha:** `AAAA-MM-DD`
