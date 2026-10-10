# Otros marcos — Gobernanza, Controles, Auditoría y Resiliencia

Referencia de marcos complementarios a ISO/IEC 27001 y NIST: gobierno de TI, controles técnicos priorizados, informes de auditoría, gestión de riesgo y continuidad de negocio.

---

## COBIT 2019 — Gobierno de TI empresarial

Marco de **gobierno y gestión de TI** de ISACA. Separa **Governance (EDM)** y **Management (APO, BAI, DSS, MEA)** en dominios de objetivos.

| Dominio | Enfoque |
|---|---|
| **EDM** | Evaluar, Dirigir y Monitorear (gobierno) |
| **APO** | Alinear, Planificar y Organizar |
| **BAI** | Construir, Adquirir e Implementar |
| **DSS** | Entregar, Dar Servicio y Soporte |
| **MEA** | Monitorear, Evaluar y Analizar |

> Se integra con ISO/IEC 27001 mediante mapeos de objetivos de gobierno a controles de seguridad.

---

## CIS Critical Security Controls v8.1

18 controles de **priorización defensiva** basados en ataques reales, con niveles de implementación (IG1/IG2/IG3):

| # | Control | # | Control |
|---|---|---|---|
| 1 | Inventario de activos empresariales | 10 | Defensas contra malware |
| 2 | Inventario de software | 11 | Recuperación de datos |
| 3 | Protección de datos | 12 | Gestión de infraestructura de red |
| 4 | Configuración segura | 13 | Monitoreo y defensa de red |
| 5 | Gestión de cuentas | 14 | Concienciación y formación |
| 6 | Gestión de control de acceso | 15 | Gestión de proveedores |
| 7 | Gestión continua de vulnerabilidades | 16 | Seguridad de aplicaciones |
| 8 | Gestión de registros de auditoría | 17 | Gestión de respuesta a incidentes |
| 9 | Protecciones de navegador y correo | 18 | Pruebas de penetración |

> Excelente **capa de implementación técnica** que se mapea a ISO/IEC 27001, NIST CSF y PCI DSS.

---

## SOC 2 (Trust Services Criteria)

Marco de aseguramiento para proveedores de servicios, emitido por el AICPA. Cinco criterios de confianza:

- **Security** (obligatorio) · **Availability** · **Processing Integrity** · **Confidentiality** · **Privacy**

Se reporta mediante informe **Tipo I** (diseño) o **Tipo II** (eficacia operativa en un periodo).

---

## ISO 31000 — Gestión de riesgo

Principios, marco y proceso genérico de gestión de riesgo, aplicable a cualquier organización y no solo a seguridad de la información:

```text
Comunicación y consulta (transversal)
Alcance, contexto y criterios
  → Identificación → Análisis → Evaluación → Tratamiento
  → Monitoreo y revisión (transversal) → Registro e informe
```

Se complementa con **ISO/IEC 27005** para el riesgo específico de seguridad de la información.

---

## ISO 22301 — Continuidad de negocio

Sistema de gestión de continuidad de negocio (**BCMS**). Cubre análisis de impacto (**BIA**), objetivos de tiempo de recuperación (**RTO/RPO**), estrategias y planes de continuidad, y ejercicios/pruebas.

---

## ITIL 4 — Gestión de servicios

Marco de gestión de servicios de TI (prácticas de gestión de incidentes, problemas, cambios y continuidad), útil para alinear el SOC/NOC con el negocio.

---

## Relación entre marcos

```text
Gobernanza          → COBIT 2019, ISO 31000
Controles técnicos  → CIS Controls v8, NIST SP 800-53
Aseguramiento       → SOC 2, ISO/IEC 27001 (auditoría)
Resiliencia         → ISO 22301, ISO/IEC 27031
Servicio            → ITIL 4
```

<p align="center"><sub>COBIT 2019 · CIS v8 · SOC 2 · ISO 31000 · ISO 22301 · ITIL 4</sub></p>
