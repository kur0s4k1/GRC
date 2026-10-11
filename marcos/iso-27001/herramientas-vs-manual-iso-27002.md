# Herramientas que facilitan controles ISO 27001/27002

**Guía rápida · edición 2022 · revisada el 10-10-2026.** Cada fila identifica el control del **Anexo A de ISO/IEC 27001:2022** (el mismo número en ISO/IEC 27002:2022), la tarea manual y **una herramienta recomendada** para facilitarla. La tabla muestra recomendaciones concretas, no una lista obligatoria de compras.

| Control | Si se hace manualmente | Herramienta recomendada | Precio público de referencia |
|---|---|---|---|
| **A.5.16 Gestión de identidades** | Crear, cambiar y desactivar cuentas; revisar periódicamente quién tiene acceso. | [Microsoft Active Directory Domain Services](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/active-directory-domain-services): centraliza usuarios y grupos en entornos Windows. | No se encontró precio independiente de AD DS: requiere [licencias de Windows Server y CAL](https://www.microsoft.com/en-us/licensing/product-licensing/windows-server). |
| **A.5.19 Seguridad en relaciones con proveedores** | Evaluar evidencias y riesgos de cada proveedor en una ficha. | [UpGuard Vendor Risk](https://www.upguard.com/pricing/vendor-risk) · [reseñas](https://www.g2.com/products/upguard-vendor-risk/reviews): centraliza evaluaciones y seguimiento. | **USD 1.750/mes**, pago anual; útil si el volumen justifica el costo. |
| **A.5.24 Preparación para gestionar incidentes** | Mantener plan, contactos, responsables y bitácora de ejercicios. | [Jira Service Management](https://www.atlassian.com/collections/service/pricing?bundle=jira-service-management) · [reseñas](https://www.g2.com/products/jira-service-management/reviews): coordina tickets y aprobaciones. | Standard: **USD 20/agente/mes**. |
| **A.6.3 Concienciación, educación y formación** | Impartir sesiones y registrar asistencia y aprendizaje. | [KnowBe4 Security Awareness Training](https://www.knowbe4.com/products/security-awareness-training/pricing) · [reseñas](https://www.g2.com/products/knowbe4-security-awareness-training/reviews): campañas y seguimiento. | Desde **USD 2,40/persona/mes** para 25–50 puestos y contrato de 3 años. |
| **A.7.2 Entrada física** | Autorizar personas, entregar llaves y registrar visitantes. | [Kisi](https://www.getkisi.com/pricing) · [reseñas](https://www.g2.com/products/kisi/reviews): credenciales y registros de entrada. | Plataforma desde **USD 99/mes**; hardware e instalación aparte. |
| **A.8.1 Dispositivos de usuario** | Inventariar, configurar y revisar cada equipo. | [Microsoft Intune](https://www.microsoft.com/security/business/microsoft-intune-pricing) · [reseñas](https://www.gartner.com/reviews/market/endpoint-management-tools/vendor/microsoft/product/microsoft-intune): aplica políticas a equipos incorporados. | Plan 1: **USD 8/usuario/mes**, pago anual; puede estar incluido en otra licencia. |
| **A.8.4 Acceso al código fuente** | Mantener lista de colaboradores y revisar cambios. | [GitHub Team](https://github.com/team) · [reseñas](https://www.g2.com/products/github/reviews): permisos y revisión de cambios. | **USD 4/usuario/mes**. |
| **A.8.8 Gestión de vulnerabilidades técnicas** | Inventario, priorización, pruebas, parches y verificación. | [Action1](https://www.action1.com/) · [reseñas](https://www.g2.com/products/action1/reviews): identifica faltantes y automatiza parches compatibles. | **Gratis hasta 200 equipos**; no se encontró precio público oficial para más. |
| **A.8.11 Enmascaramiento de datos** | Crear y verificar datos ficticios o desidentificados para pruebas. | [Tonic Structural](https://www.tonic.ai/pricing) · [reseñas](https://www.g2.com/products/tonic-ai/reviews): desidentifica datos de prueba. **Respaldo de reseñas menor** que el de otras opciones de esta tabla. | **No se encontró** cifra pública oficial; cotización según datos conectados. |
| **A.8.13 Copias de seguridad** | Programar copias, custodiar soportes y ensayar restauración. | [Veeam Data Platform Essentials](https://www.veeam.com/products/veeam-data-platform/essentials.html) · [reseñas](https://www.g2.com/products/veeam-data-platform/reviews): respaldo y recuperación de cargas compatibles. | Desde **USD 95/licencia/año**, paquetes de 5. |
| **A.8.15 Registro de eventos** | Recoger, proteger y revisar registros de cada sistema. | [Wazuh](https://wazuh.com/) · [reseñas](https://www.g2.com/products/wazuh/reviews): centraliza eventos y alertas. | Software autogestionado **gratis**; infraestructura y operación aparte. |
| **A.8.20 Seguridad de redes** | Mantener y revisar reglas de firewall y VPN. | [Netgate pfSense](https://www.netgate.com/pfsense-plus-software/software-types) · [reseñas](https://www.g2.com/products/netgate-pfsense/reviews): firewall y segmentación. | Community Edition **sin cargo**; Plus desde **USD 129/instancia/año**. |
| **A.8.28 Programación segura** | Revisar código y dependencias antes de publicar. | [Snyk](https://snyk.io/plans/) · [reseñas](https://www.g2.com/products/snyk/reviews): analiza código y dependencias compatibles. | Free **USD 0**; Team desde **USD 25/mes**. |

**Ejemplo de otra opción para A.8.8:** [Vicarius vRx](https://www.vicarius.io/features/patch-management) reúne priorización, parcheo y otras formas de remediación; tiene [reseñas de usuarios](https://www.g2.com/products/vrx-by-vicarius/reviews). **No se encontró un precio público oficial actual**; requiere cotización. Action1 aparece como primera recomendación por su entrada gratuita y mayor volumen de reseñas, no porque sea adecuado para toda infraestructura.

## ¿A cuántos controles ayuda cada herramienta?

**Conteo orientativo de esta guía:** **14 herramientas**, **50 relaciones herramienta–control** y **40 controles distintos de 93** con algún apoyo posible. Un mismo control puede aparecer en varias herramientas. Los números indican **apoyo parcial**, nunca que el producto cumpla o certifique el control. Las funciones dependen del plan, la configuración y los activos incorporados.

| Herramienta | Controles a los que puede aportar | N.º |
|---|---|---:|
| Active Directory DS | A.5.15, A.5.16, A.5.17, A.5.18, A.8.2, A.8.3 | **6** |
| Jira Service Management | A.5.24–A.5.27, A.8.32 | **5** |
| Microsoft Intune | A.5.9, A.7.9, A.8.1, A.8.9, A.8.19 | **5** |
| Wazuh | A.5.25, A.5.28, A.8.9, A.8.15, A.8.16 | **5** |
| UpGuard Vendor Risk | A.5.19–A.5.22 | **4** |
| Snyk | A.8.8, A.8.25, A.8.28, A.8.29 | **4** |
| Kisi | A.7.2, A.7.4, A.7.6 | **3** |
| GitHub Team | A.8.4, A.8.25, A.8.32 | **3** |
| Action1 | A.5.9, A.8.8, A.8.19 | **3** |
| Tonic Structural | A.5.34, A.8.11, A.8.33 | **3** |
| Netgate pfSense | A.8.20–A.8.22 | **3** |
| Vicarius vRx | A.5.9, A.8.8, A.8.9 | **3** |
| Veeam Data Platform Essentials | A.5.30, A.8.13 | **2** |
| KnowBe4 Security Awareness Training | A.6.3 | **1** |

**Ejemplo — Vicarius:** su inventario de activos aporta a **A.5.9**; detección de vulnerabilidades y despliegue de parches aportan juntos a **A.8.8**; la evaluación de configuraciones aporta a **A.8.9**. Son **tres controles**, aunque se mencionen cuatro funciones. [Funciones oficiales de Vicarius](https://www.vicarius.io/features/vulnerability-management).

**Antes de contratar:** una herramienta **facilita** una parte del control; comprarla no equivale a cumplirlo. Evalúa al proveedor y el riesgo nuevo: datos y privilegios que recibirá, subprocesadores y ubicación, seguridad y continuidad, costo total, soporte, salida y borrado de datos. Define quién operará el producto y cómo comprobarás que funciona. Los precios son referencias de lista en USD consultadas en octubre de 2026; pueden variar por región, impuestos, volumen y contrato.
