# Herramientas que facilitan controles ISO 27001/27002

**Guía rápida · edición 2022 · revisada el 10-10-2026.** Cada fila identifica el control del **Anexo A de ISO/IEC 27001:2022** (el mismo número en ISO/IEC 27002:2022), la tarea manual y **una o más herramientas recomendadas** para facilitarla. Arriba hay recomendaciones directas; debajo está la lista completa de **los 93 controles**, agrupada en secciones desplegables.

| Control | Si se hace manualmente | Herramienta recomendada | Precio público de referencia |
|---|---|---|---|
| **A.5.7 Inteligencia de amenazas** | Elegir fuentes pertinentes, analizar amenazas para la organización y decidir acciones. | [MISP](https://www.misp-project.org/features/): reúne, relaciona y comparte indicadores e información de amenazas. El equipo debe validar su contexto y utilidad. | Software **gratuito y de código abierto**; alojamiento, operación y fuentes comerciales aparte. |
| **A.5.16 Gestión de identidades** | Crear, cambiar y desactivar cuentas; revisar periódicamente quién tiene acceso. | [Microsoft Active Directory Domain Services](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/active-directory-domain-services): centraliza usuarios y grupos en entornos Windows. | No se encontró precio independiente de AD DS: requiere [licencias de Windows Server y CAL](https://www.microsoft.com/en-us/licensing/product-licensing/windows-server). |
| **A.5.19 Seguridad en relaciones con proveedores** | Evaluar evidencias y riesgos de cada proveedor en una ficha. | [UpGuard Vendor Risk](https://www.upguard.com/pricing/vendor-risk) · [reseñas](https://www.g2.com/products/upguard-vendor-risk/reviews): centraliza evaluaciones y seguimiento. | **USD 1.750/mes**, pago anual; útil si el volumen justifica el costo. |
| **A.5.24 Preparación para gestionar incidentes** | Mantener plan, contactos, responsables y bitácora de ejercicios. | [Jira Service Management](https://www.atlassian.com/collections/service/pricing?bundle=jira-service-management) · [reseñas](https://www.g2.com/products/jira-service-management/reviews): coordina tickets y aprobaciones. | Standard: **USD 20/agente/mes**. |
| **A.5.34 Privacidad y datos personales** | Inventariar tratamientos, evaluar riesgos y atender solicitudes de titulares. | [OneTrust Privacy Automation](https://www.onetrust.com/solutions/privacy-automation/) · [reseñas](https://www.g2.com/products/onetrust-privacy-automation/reviews): organiza flujos de datos, evaluaciones y solicitudes. [Tonic Structural](https://www.tonic.ai/pricing) ayuda específicamente a desidentificar datos de prueba. | **OneTrust:** no se encontró precio público fijo; requiere cotización. **Tonic:** no se encontró cifra pública oficial. |
| **A.6.3 Concienciación, educación y formación** | Impartir sesiones y registrar asistencia y aprendizaje. | [KnowBe4 Security Awareness Training](https://www.knowbe4.com/products/security-awareness-training/pricing) · [reseñas](https://www.g2.com/products/knowbe4-security-awareness-training/reviews): campañas y seguimiento. | Desde **USD 2,40/persona/mes** para 25–50 puestos y contrato de 3 años. |
| **A.7.2 Entrada física** | Autorizar personas, entregar llaves y registrar visitantes. | [Kisi](https://www.getkisi.com/pricing) · [reseñas](https://www.g2.com/products/kisi/reviews): credenciales y registros de entrada. | Plataforma desde **USD 99/mes**; hardware e instalación aparte. |
| **A.8.1 Dispositivos de usuario** | Inventariar, configurar y revisar cada equipo. | [Microsoft Intune](https://www.microsoft.com/security/business/microsoft-intune-pricing) · [reseñas](https://www.gartner.com/reviews/market/endpoint-management-tools/vendor/microsoft/product/microsoft-intune): aplica políticas a equipos incorporados. | Plan 1: **USD 8/usuario/mes**, pago anual; puede estar incluido en otra licencia. |
| **A.8.4 Acceso al código fuente** | Mantener lista de colaboradores y revisar cambios. | [GitHub Team](https://github.com/team) · [reseñas](https://www.g2.com/products/github/reviews): permisos y revisión de cambios. | **USD 4/usuario/mes**. |
| **A.8.5 Autenticación segura** | Exigir MFA, revisar métodos de acceso y excepciones. | [Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/identity/authentication/concept-mfa-licensing): MFA para identidades incorporadas; el nivel gratuito permite valores predeterminados de seguridad. | **Gratis** para MFA básico; P1 **USD 7/usuario/mes**, pago anual, para políticas avanzadas. |
| **A.8.6 Gestión de capacidad** | Medir uso y tendencia de CPU, memoria, disco y servicios; planificar ampliaciones. | [Zabbix](https://www.zabbix.com/features): recoge métricas, genera alertas y permite analizar tendencias. | Software autogestionado **gratis**; infraestructura y operación aparte. |
| **A.8.7 Protección contra malware** | Desplegar protección, revisar alertas y responder a infecciones. | [Cortex XDR](https://www.paloaltonetworks.com/cortex/endpoint-protection) · [reseñas](https://www.g2.com/products/palo-alto-networks-cortex-xdr/reviews): prevención y detección en equipos incorporados. | No se encontró precio público oficial; requiere cotización. |
| **A.8.8 Gestión de vulnerabilidades técnicas** | Inventario, priorización, pruebas, parches y verificación. | [Action1](https://www.action1.com/) · [reseñas](https://www.g2.com/products/action1/reviews): identifica faltantes y automatiza parches compatibles.<br>[Vicarius vRx](https://www.vicarius.io/features/patch-management) · [reseñas](https://www.g2.com/products/vrx-by-vicarius/reviews): prioriza, parchea y ofrece otras opciones de remediación. | **Action1:** gratis hasta 200 equipos; no se encontró precio público oficial para más.<br>**Vicarius vRx:** no se encontró precio público oficial actual; requiere cotización. |
| **A.8.9 Gestión de configuración** | Definir configuraciones seguras y comprobar desvíos. | [Microsoft Intune](https://learn.microsoft.com/en-us/intune/device-security/security-baselines/overview) aplica líneas base en equipos compatibles; Wazuh y Vicarius vRx ayudan a detectar desvíos. | Intune Plan 1: **USD 8/usuario/mes**, pago anual; precios de Wazuh y Vicarius según sus filas y licencias. |
| **A.8.11 Enmascaramiento de datos** | Crear y verificar datos ficticios o desidentificados para pruebas. | [Tonic Structural](https://www.tonic.ai/pricing) · [reseñas](https://www.g2.com/products/tonic-ai/reviews): desidentifica datos de prueba. **Respaldo de reseñas menor** que el de otras opciones de esta tabla. | **No se encontró** cifra pública oficial; cotización según datos conectados. |
| **A.8.12 Prevención de fuga de datos** | Clasificar información, definir canales permitidos y revisar excepciones. | [Microsoft Purview DLP](https://learn.microsoft.com/en-us/purview/dlp-learn-about-dlp) · [reseñas](https://www.g2.com/products/microsoft-purview-data-loss-prevention/reviews): aplica políticas DLP en ubicaciones y dispositivos compatibles. | No se encontró precio público independiente; depende del plan y de las funciones licenciadas. |
| **A.8.13 Copias de seguridad** | Programar copias, custodiar soportes y ensayar restauración. | [Veeam Data Platform Essentials](https://www.veeam.com/products/veeam-data-platform/essentials.html) · [reseñas](https://www.g2.com/products/veeam-data-platform/reviews): respaldo y recuperación de cargas compatibles. | Desde **USD 95/licencia/año**, paquetes de 5. |
| **A.8.15 Registro de eventos** | Recoger, proteger y revisar registros de cada sistema. | [Wazuh](https://wazuh.com/) · [reseñas](https://www.g2.com/products/wazuh/reviews): centraliza eventos y alertas. | Software autogestionado **gratis**; infraestructura y operación aparte. |
| **A.8.17 Sincronización de relojes** | Configurar fuentes horarias fiables y comprobar desvíos. | [chrony](https://chrony-project.org/): sincroniza relojes de sistemas compatibles mediante NTP. | Software **gratuito**; servidores de tiempo y operación aparte. |
| **A.8.20 Seguridad de redes** | Mantener y revisar reglas de firewall y VPN. | [Netgate pfSense](https://www.netgate.com/pfsense-plus-software/software-types) · [reseñas](https://www.g2.com/products/netgate-pfsense/reviews): firewall y segmentación. | Community Edition **sin cargo**; Plus desde **USD 129/instancia/año**. |
| **A.8.23 Filtrado web** | Definir categorías, excepciones y comprobar bloqueos. | [Cloudflare Gateway](https://www.cloudflare.com/products/gateway/): filtra consultas DNS y tráfico web de usuarios incorporados. | Plan Zero Trust **gratis hasta 50 usuarios**; verificar funciones y límites del plan. |
| **A.8.24 Uso de criptografía** | Definir qué cifrar, gestionar claves y revisar rotaciones. | [HashiCorp Vault](https://developer.hashicorp.com/vault/docs/secrets/transit): gestiona claves y operaciones criptográficas para aplicaciones integradas. | Edición Community autogestionada **sin licencia empresarial**; no se encontró precio público fijo para Enterprise. |
| **A.8.28 Programación segura** | Revisar código y dependencias antes de publicar. | [Snyk](https://snyk.io/plans/) · [reseñas](https://www.g2.com/products/snyk/reviews): analiza código y dependencias compatibles. | Free **USD 0**; Team desde **USD 25/mes**. |

## Los 93 controles, en una línea cada uno

Abre el tema que te interese. «Sin herramienta seleccionada» significa que esta guía no recomienda un producto concreto para ese control; el trabajo manual descrito sigue siendo necesario. Los nombres y precios de las herramientas citadas están arriba.

<details>
<summary><strong>A.5 · Organizativos (37)</strong></summary>

| Control | Trabajo manual | Herramienta de apoyo |
|---|---|---|
| **A.5.1 Política de seguridad** | Redactar, aprobar, comunicar y revisar versiones. | Sin herramienta seleccionada |
| **A.5.2 Roles de seguridad** | Asignar responsables y revisar RACI. | Sin herramienta seleccionada |
| **A.5.3 Separación de funciones** | Identificar conflictos y revisar accesos. | Sin herramienta seleccionada |
| **A.5.4 Responsabilidades directivas** | Supervisar objetivos y exigir seguimiento. | Sin herramienta seleccionada |
| **A.5.5 Contacto con autoridades** | Mantener contactos, criterios y suplentes. | Sin herramienta seleccionada |
| **A.5.6 Contacto con comunidades especializadas** | Designar participación y registrar aprendizaje. | Sin herramienta seleccionada |
| **A.5.7 Inteligencia de amenazas** | Elegir fuentes, contextualizar señales y decidir acciones. | MISP |
| **A.5.8 Seguridad en proyectos** | Incluir riesgos y revisiones en cada proyecto. | Sin herramienta seleccionada |
| **A.5.9 Inventario de activos e información** | Identificar propietario, ubicación y criticidad. | Microsoft Intune, Action1, Vicarius vRx |
| **A.5.10 Uso aceptable de activos** | Definir reglas y comunicar consecuencias. | Sin herramienta seleccionada |
| **A.5.11 Devolución de activos** | Lista de salida y verificación física. | Sin herramienta seleccionada |
| **A.5.12 Clasificación de información** | Definir niveles y decidir clase por propietario. | Sin herramienta seleccionada |
| **A.5.13 Etiquetado de información** | Aplicar marcas según clasificación. | Sin herramienta seleccionada |
| **A.5.14 Transferencia de información** | Autorizar destinatarios y proteger el envío. | Sin herramienta seleccionada |
| **A.5.15 Control de acceso** | Definir necesidad, aprobar y revisar permisos. | Active Directory DS |
| **A.5.16 Gestión de identidades** | Alta, cambio, baja y reconciliación. | Active Directory DS |
| **A.5.17 Información de autenticación** | Reglas de creación, custodia y recuperación. | Active Directory DS |
| **A.5.18 Derechos de acceso** | Aprobar, revisar y revocar derechos. | Active Directory DS |
| **A.5.19 Seguridad en relaciones con proveedores** | Inventariar y clasificar proveedores. | UpGuard Vendor Risk |
| **A.5.20 Seguridad en contratos con proveedores** | Negociar cláusulas y responsabilidades. | UpGuard Vendor Risk |
| **A.5.21 Cadena de suministro TIC** | Identificar subproveedores y dependencias. | UpGuard Vendor Risk |
| **A.5.22 Seguimiento de servicios de proveedores** | Revisar SLA, incidentes y cambios. | UpGuard Vendor Risk |
| **A.5.23 Uso seguro de nube** | Evaluar arquitectura, responsabilidad compartida y salida. | Sin herramienta seleccionada |
| **A.5.24 Preparación ante incidentes** | Definir roles, playbooks y ejercicios. | Jira Service Management |
| **A.5.25 Evaluación de eventos** | Definir severidad y decidir escalamiento. | Jira Service Management, Wazuh |
| **A.5.26 Respuesta a incidentes** | Contener, comunicar, erradicar y recuperar. | Jira Service Management |
| **A.5.27 Aprendizaje de incidentes** | Analizar causas y verificar mejoras. | Jira Service Management |
| **A.5.28 Recolección de evidencia** | Establecer custodia, integridad y retención. | Wazuh |
| **A.5.29 Seguridad durante interrupciones** | Priorizar funciones y reglas temporales. | Sin herramienta seleccionada |
| **A.5.30 Preparación TIC para continuidad** | Definir RTO/RPO y probar recuperación. | Veeam Data Platform Essentials |
| **A.5.31 Requisitos legales y contractuales** | Mantener matriz legal y revisar cambios. | Sin herramienta seleccionada |
| **A.5.32 Propiedad intelectual** | Identificar licencias, titulares y permisos. | Sin herramienta seleccionada |
| **A.5.33 Protección de registros** | Definir retención, acceso y destrucción. | Sin herramienta seleccionada |
| **A.5.34 Privacidad y datos personales** | Mapear tratamientos y bases, minimizar datos. | OneTrust Privacy Automation, Tonic Structural (datos de prueba) |
| **A.5.35 Revisión independiente** | Encargar revisión externa y gestionar hallazgos. | Sin herramienta seleccionada |
| **A.5.36 Cumplimiento de políticas** | Muestrear prácticas y corregir desvíos. | Sin herramienta seleccionada |
| **A.5.37 Procedimientos operativos** | Documentar pasos, responsables y actualización. | Sin herramienta seleccionada |

</details>

<details>
<summary><strong>A.6 · De personas (8)</strong></summary>

| Control | Trabajo manual | Herramienta de apoyo |
|---|---|---|
| **A.6.1 Verificación previa** | Definir verificaciones legales, proporcionales y consentidas. | Sin herramienta seleccionada |
| **A.6.2 Términos de empleo** | Incluir deberes de seguridad en acuerdos. | Sin herramienta seleccionada |
| **A.6.3 Formación y conciencia** | Enseñar, reforzar y medir aprendizaje. | KnowBe4 Security Awareness Training |
| **A.6.4 Proceso disciplinario** | Definir reglas justas y aplicar con RR. HH. | Sin herramienta seleccionada |
| **A.6.5 Responsabilidades al salir o cambiar** | Recordar deberes y cerrar accesos/activos. | Sin herramienta seleccionada |
| **A.6.6 Acuerdos de confidencialidad** | Definir alcance, firmar y revisar vigencia. | Sin herramienta seleccionada |
| **A.6.7 Trabajo remoto** | Fijar condiciones, medios y revisión. | Sin herramienta seleccionada |
| **A.6.8 Reporte de eventos** | Dar canal sencillo y entrenar su uso. | Sin herramienta seleccionada |

</details>

<details>
<summary><strong>A.7 · Físicos (14)</strong></summary>

| Control | Trabajo manual | Herramienta de apoyo |
|---|---|---|
| **A.7.1 Perímetro físico** | Delimitar zonas, inspeccionar barreras. | Sin herramienta seleccionada |
| **A.7.2 Entrada física** | Autorizar, registrar y revocar entradas. | Kisi |
| **A.7.3 Oficinas y salas** | Definir zonas y revisar cierres. | Sin herramienta seleccionada |
| **A.7.4 Vigilancia física** | Vigilar entradas y responder alertas. | Kisi |
| **A.7.5 Amenazas ambientales** | Evaluar incendio, agua, temperatura y ubicación. | Sin herramienta seleccionada |
| **A.7.6 Trabajo en áreas seguras** | Autorizar actividades y supervisar visitantes. | Kisi |
| **A.7.7 Mesa y pantalla limpias** | Inspeccionar puestos y bloquear pantallas. | Sin herramienta seleccionada |
| **A.7.8 Ubicación y protección de equipos** | Evitar exposición a golpes, calor o robo. | Sin herramienta seleccionada |
| **A.7.9 Activos fuera de instalaciones** | Autorizar préstamo y proteger transporte. | Microsoft Intune |
| **A.7.10 Medios de almacenamiento** | Inventariar, restringir, transportar y destruir. | Sin herramienta seleccionada |
| **A.7.11 Servicios de soporte** | Evaluar energía, climatización y redundancia. | Sin herramienta seleccionada |
| **A.7.12 Cableado** | Inspeccionar rutas y proteger puntos expuestos. | Sin herramienta seleccionada |
| **A.7.13 Mantenimiento de equipos** | Programar, autorizar y registrar trabajos. | Sin herramienta seleccionada |
| **A.7.14 Eliminación/reutilización segura** | Borrar o destruir y verificar medios. | Sin herramienta seleccionada |

</details>

<details>
<summary><strong>A.8 · Tecnológicos (34)</strong></summary>

| Control | Trabajo manual | Herramienta de apoyo |
|---|---|---|
| **A.8.1 Dispositivos de usuario** | Configurar, cifrar, actualizar y revisar. | Microsoft Intune |
| **A.8.2 Acceso privilegiado** | Aprobar privilegios mínimos y revisarlos. | Active Directory DS |
| **A.8.3 Restricción de información** | Definir permisos por necesidad. | Active Directory DS |
| **A.8.4 Acceso a código fuente** | Autorizar colaboradores y revisar repositorios. | GitHub Team |
| **A.8.5 Autenticación segura** | Exigir MFA y mecanismos adecuados. | Microsoft Entra ID |
| **A.8.6 Capacidad** | Medir consumo, prever crecimiento y actuar. | Zabbix |
| **A.8.7 Malware** | Definir prevención, actualización y respuesta. | Cortex XDR |
| **A.8.8 Vulnerabilidades técnicas** | Descubrir, priorizar, parchear y verificar. | Action1, Vicarius vRx |
| **A.8.9 Configuración** | Mantener líneas base, comprobar y corregir desvíos. | Microsoft Intune, Wazuh, Vicarius vRx |
| **A.8.10 Eliminación de información** | Definir plazos y comprobar borrado. | Microsoft Intune (solo dispositivos incorporados) |
| **A.8.11 Enmascaramiento** | Clasificar datos, aplicar reglas y probar reidentificación. | Tonic Structural |
| **A.8.12 Prevención de fuga** | Mapear canales, aplicar reglas y revisar alertas. | Microsoft Purview DLP |
| **A.8.13 Respaldo** | Establecer frecuencia, cifrar y probar restauración. | Veeam Data Platform Essentials |
| **A.8.14 Redundancia** | Diseñar y ensayar conmutación. | Sin herramienta seleccionada |
| **A.8.15 Registro de eventos** | Elegir eventos, proteger y retener logs. | Wazuh |
| **A.8.16 Monitoreo** | Definir casos de uso y responder. | Wazuh |
| **A.8.17 Sincronización de relojes** | Configurar hora fiable y revisar desvíos. | chrony (sistemas compatibles) |
| **A.8.18 Utilidades privilegiadas** | Restringir herramientas administrativas. | Microsoft Intune App Control (Windows administrado) |
| **A.8.19 Instalación de software** | Autorizar aplicaciones y cambios. | Microsoft Intune, Action1 |
| **A.8.20 Seguridad de redes** | Definir reglas, segmentar y revisar tráfico. | Netgate pfSense |
| **A.8.21 Servicios de red** | Contratar, configurar y supervisar servicios. | Netgate pfSense |
| **A.8.22 Segmentación de redes** | Diseñar zonas y probar aislamiento. | Netgate pfSense |
| **A.8.23 Filtrado web** | Definir categorías, excepciones y revisar bloqueos. | Cloudflare Gateway |
| **A.8.24 Criptografía** | Elegir algoritmos, llaves y rotación. | HashiCorp Vault (claves y aplicaciones integradas) |
| **A.8.25 Desarrollo seguro** | Definir revisiones y puertas de entrega. | Snyk, GitHub Team |
| **A.8.26 Requisitos de seguridad de aplicaciones** | Traducir riesgos en criterios verificables. | Sin herramienta seleccionada |
| **A.8.27 Arquitectura segura** | Revisar límites de confianza y decisiones. | Sin herramienta seleccionada |
| **A.8.28 Programación segura** | Establecer pautas y revisar código. | Snyk |
| **A.8.29 Pruebas de seguridad** | Definir alcance y comprobar correcciones. | Snyk |
| **A.8.30 Desarrollo tercerizado** | Pactar obligaciones, revisar entregables. | Sin herramienta seleccionada |
| **A.8.31 Entornos separados** | Separar identidades, redes y datos. | Sin herramienta seleccionada |
| **A.8.32 Cambios** | Solicitar, aprobar, desplegar y revertir. | Jira Service Management, GitHub Team |
| **A.8.33 Información de prueba** | Evitar PII real o reducirla de forma demostrable. | Tonic Structural |
| **A.8.34 Protección durante auditorías técnicas** | Pactar alcance, ventanas y custodia de resultados. | Sin herramienta seleccionada |

</details>


## ¿A cuántos controles ayuda cada herramienta?

**Conteo orientativo de esta guía:** **23 herramientas**, **60 relaciones herramienta–control** y **50 controles distintos de 93** con algún apoyo posible; en los otros **43** no se seleccionó una herramienta en esta edición. Un mismo control puede aparecer en varias herramientas. Los números indican **apoyo parcial**, nunca que el producto cumpla o certifique el control. Las funciones dependen del plan, la configuración y los activos incorporados.

| Herramienta | Controles a los que puede aportar | N.º |
|---|---|---:|
| MISP | A.5.7 | **1** |
| Active Directory DS | A.5.15, A.5.16, A.5.17, A.5.18, A.8.2, A.8.3 | **6** |
| Jira Service Management | A.5.24–A.5.27, A.8.32 | **5** |
| Microsoft Intune | A.5.9, A.7.9, A.8.1, A.8.9, A.8.10, A.8.18, A.8.19 | **7** |
| Wazuh | A.5.25, A.5.28, A.8.9, A.8.15, A.8.16 | **5** |
| UpGuard Vendor Risk | A.5.19–A.5.22 | **4** |
| Snyk | A.8.25, A.8.28, A.8.29 | **3** |
| Kisi | A.7.2, A.7.4, A.7.6 | **3** |
| GitHub Team | A.8.4, A.8.25, A.8.32 | **3** |
| Action1 | A.5.9, A.8.8, A.8.19 | **3** |
| Tonic Structural | A.5.34, A.8.11, A.8.33 | **3** |
| Netgate pfSense | A.8.20–A.8.22 | **3** |
| Vicarius vRx | A.5.9, A.8.8, A.8.9 | **3** |
| Veeam Data Platform Essentials | A.5.30, A.8.13 | **2** |
| KnowBe4 Security Awareness Training | A.6.3 | **1** |
| OneTrust Privacy Automation | A.5.34 | **1** |
| Microsoft Entra ID | A.8.5 | **1** |
| Zabbix | A.8.6 | **1** |
| Cortex XDR | A.8.7 | **1** |
| Microsoft Purview DLP | A.8.12 | **1** |
| chrony | A.8.17 | **1** |
| Cloudflare Gateway | A.8.23 | **1** |
| HashiCorp Vault | A.8.24 | **1** |

**Ejemplo — Vicarius:** su inventario de activos aporta a **A.5.9**; detección de vulnerabilidades y despliegue de parches aportan juntos a **A.8.8**; la evaluación de configuraciones aporta a **A.8.9**. Son **tres controles**, aunque se mencionen cuatro funciones. [Funciones oficiales de Vicarius](https://www.vicarius.io/features/vulnerability-management).

**Configuración y cambios:** **A.8.9** trata de definir y conservar configuraciones seguras y revisar desvíos; **A.8.32** trata de solicitar, aprobar, probar y desplegar cambios. Cambiar una configuración puede activar ambos controles, pero son actividades distintas.

**Antes de contratar:** una herramienta **facilita** una parte del control; comprarla no equivale a cumplirlo. Evalúa al proveedor y el riesgo nuevo: datos y privilegios que recibirá, subprocesadores y ubicación, seguridad y continuidad, costo total, soporte, salida y borrado de datos. Define quién operará el producto y cómo comprobarás que funciona. Los precios son referencias de lista en USD consultadas en octubre de 2026; pueden variar por región, impuestos, volumen y contrato.
