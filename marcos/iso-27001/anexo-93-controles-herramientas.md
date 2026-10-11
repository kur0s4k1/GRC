# ISO/IEC 27002:2022: apoyo manual y herramientas para los 93 controles

**Para una lectura rápida:** [herramientas recomendadas en controles donde más ayudan](herramientas-vs-manual-iso-27002.md).

**Revisión:** 10 de octubre de 2026. **Alcance:** los 93 controles de ISO/IEC 27002:2022, alineados por número con el Anexo A de ISO/IEC 27001:2022. Los nombres de la matriz son resúmenes propios en español, no el texto normativo. Referencia del [índice de controles](https://www.opensecurityarchitecture.org/frameworks/iso-27002-2022/) y de la [estructura de 93 controles de ISO](https://committee.iso.org/files/live/sites/jtc1sc27/files/resources/ISO-IEC%20JTC%201-SC%2027_N22755_SC27%20Journal%20Vol%202%20Issue%202%20%28update%20Dec%202022%29.pdf).

**Cómo leer esto.** Una herramienta puede facilitar una actividad o producir evidencia, pero **no cubre por sí sola el control**. La organización sigue siendo responsable de definir el alcance, operar el proceso, revisar excepciones, verificar resultados y tratar riesgos residuales. La alternativa «manual» tampoco equivale automáticamente a cumplimiento. Las opciones se deben seleccionar según contexto y evaluación de riesgos; no hay obligación de comprar software para cada control.

**Precios.** Importes de lista en USD consultados el 10-10-2026, salvo indicación. Son ejemplos de planes concretos, no presupuestos: pueden variar por región, impuestos, volumen, modalidad, funciones, instalación o contrato. «No se encontró» significa que no hallé un precio público oficial para el producto/plan citado; no significa que sea gratuito. Las reseñas enlazadas son una señal de experiencia de usuarios, no una certificación ni una prueba de cobertura. Algunas plataformas incluyen reseñas incentivadas: leer también las críticas recientes y comprobar que correspondan al producto y plan evaluados.

## Catálogo de herramientas

La matriz usa los códigos de esta tabla. Cada enlace «producto/precio» lleva a la fuente oficial y «reseñas» a una página de usuarios. En productos de alcance amplio, la recomendación se limita a la función indicada.

| Código | Herramienta y aporte concreto | Precio público oficial consultado | Riesgo o límite que debe evaluarse | Enlaces |
|---|---|---|---|---|
| DOC | Confluence: políticas, procedimientos y revisiones documentales | Standard: **USD 5,42/usuario/mes** | Permisos incorrectos o documentación obsoleta | [Producto y precio](https://www.atlassian.com/software/confluence/pricing) · [Reseñas](https://www.g2.com/products/confluence/reviews) |
| FLU | Jira Service Management: solicitudes, incidentes, cambios y aprobaciones | Standard: **USD 20/agente/mes** | Flujos mal configurados, tickets con datos sensibles | [Producto y precio](https://www.atlassian.com/collections/service/pricing?bundle=jira-service-management) · [Reseñas](https://www.g2.com/products/jira-service-management/reviews) |
| ID | Okta Workforce Identity: SSO, MFA y ciclo de identidades | Starter Suite: desde **USD 6/usuario/mes**, anual | Concentración de identidad, bloqueo por falla del proveedor | [Producto y precio](https://www.okta.com/pricing/) · [Reseñas](https://www.g2.com/products/okta/reviews) |
| SEC | 1Password Business: secretos y credenciales compartidas | **USD 8,99/usuario/mes**, facturación anual | Acceso privilegiado a bóvedas y dependencia del servicio | [Producto y precio](https://1password.com/pricing/business) · [Reseñas](https://www.g2.com/products/1password/reviews) |
| FOR | KnowBe4 Security Awareness Training: campañas y registro de formación | Foundation: desde **USD 2,40/persona/mes**, 25–50 puestos y contrato de 3 años | Métricas de clics no demuestran conducta segura; datos laborales | [Producto y precio](https://www.knowbe4.com/products/security-awareness-training/pricing) · [Reseñas](https://www.g2.com/products/knowbe4-security-awareness-training/reviews) |
| PRO | UpGuard Vendor Risk: evaluación y seguimiento de proveedores | Standard: **USD 1.750/mes**, anual, hasta 50 proveedores | Calificación externa incompleta; costo alto para pocos proveedores | [Producto y precio](https://www.upguard.com/pricing/vendor-risk) · [Reseñas](https://www.g2.com/products/upguard-vendor-risk/reviews) |
| MDM | Microsoft Intune Plan 1: inventario, configuración y protección de equipos | **USD 8/usuario/mes**, compromiso anual; puede venir incluido en otras licencias | Cobertura solo de dispositivos incorporados; políticas mal aplicadas | [Producto y precio](https://www.microsoft.com/security/business/microsoft-intune-pricing) · [Reseñas](https://www.gartner.com/reviews/market/endpoint-management-tools/vendor/microsoft/product/microsoft-intune) |
| PAR | Action1: parches, estado de endpoints y remediación | Primeros **200 endpoints gratis**; precio para más equipos: **no se encontró** cifra pública oficial | Agente con privilegios y cobertura real de aplicaciones/sistemas | [Producto](https://www.action1.com/) · [Reseñas](https://www.g2.com/products/action1/reviews) |
| VRX | Vicarius vRx: priorización, parcheo y remediación | **No se encontró** precio público oficial actual; requiere cotización por alcance | Agente y motor de remediación con acceso elevado; validar falsos positivos | [Producto](https://www.vicarius.io/features/patch-management) · [Cotización](https://www.vicarius.io/get-started) · [Reseñas](https://www.g2.com/products/vrx-by-vicarius/reviews) |
| SIEM | Wazuh: centralización de eventos, alertas y configuración | Software autogestionado: **gratis**; alojamiento, operación y soporte no incluidos | Afinación, falsos positivos, almacenamiento y acceso a registros | [Producto](https://wazuh.com/) · [Reseñas](https://www.g2.com/products/wazuh/reviews) |
| BAK | Veeam Data Platform Essentials: respaldo y recuperación de cargas compatibles | Precio de lista desde **USD 95/licencia/año**, paquetes de 5 hasta 50 cargas | Copias comprometidas, costos de almacenamiento, restauración no probada | [Producto y precio](https://www.veeam.com/products/veeam-data-platform/essentials.html) · [Reseñas](https://www.g2.com/products/veeam-data-platform/reviews) |
| MON | Paessler PRTG: capacidad, disponibilidad y sensores conectados | PRTG 500: **USD 200/mes**, pago anual; edición gratuita hasta 100 sensores | Sensores mal ubicados, alarmas ignoradas; el hardware se paga aparte | [Producto y precio](https://www.paessler.com/pricing) · [Reseñas](https://www.g2.com/products/paessler-prtg/reviews) |
| FIS | Kisi: gestión de acceso físico y registro de entradas | Plataforma desde **USD 99/mes**; lectores, controladores e instalación aparte | Disponibilidad de nube/energía, acceso físico de emergencia y privacidad | [Producto y precio](https://www.getkisi.com/pricing) · [Reseñas](https://www.g2.com/products/kisi/reviews) |
| COD | GitHub Team: repositorios, revisión y reglas de ramas | **USD 4/usuario/mes**; funciones avanzadas pueden requerir otro plan | Exposición de código/secretos y permisos de repositorio | [Producto y precio](https://github.com/team) · [Reseñas](https://www.g2.com/products/github/reviews) |
| APP | Snyk: análisis de código, dependencias, contenedores e IaC | Free: **USD 0**; Team desde **USD 25/mes** para equipos pequeños, con límites | Hallazgos no corregidos, cobertura de lenguajes y costos de consumo | [Producto y precio](https://snyk.io/plans/) · [Reseñas](https://www.g2.com/products/snyk/reviews) |
| RED | Netgate pfSense: firewall, VPN y segmentación | Community Edition: **sin cargo**; Plus desde **USD 129/instancia/año** | Reglas erróneas, punto único de falla, mantenimiento de hardware | [Producto y precio](https://www.netgate.com/pfsense-plus-software/software-types) · [Reseñas](https://www.g2.com/products/netgate-pfsense/reviews) |
| DAT | Tonic Structural: desidentificación y datos de prueba | **No se encontró** cifra pública oficial para Structural; cotización según datos conectados | Datos sensibles transferidos, errores de desidentificación y reidentificación | [Producto y precio](https://www.tonic.ai/pricing) · [Reseñas](https://www.g2.com/products/tonic-ai/reviews) |

**Lectura crítica de reputación.** En G2, las páginas consultadas muestran, por ejemplo, Action1 **4,9/5 con más de 1.200 reseñas**, Vicarius vRx **4,9/5 con 63**, Wazuh **4,5/5 con 72** y Tonic.ai **4,2/5 con 38**. El tamaño de muestra varía mucho; estas cifras son instantáneas y pueden cambiar. [Action1](https://www.g2.com/products/action1/reviews) · [Vicarius](https://www.g2.com/products/vrx-by-vicarius/reviews) · [Wazuh](https://www.g2.com/products/wazuh/reviews) · [Tonic.ai](https://www.g2.com/products/tonic-ai/reviews). **Nymiz** es una opción interesante para anonimización, pero encontré solo [9 reseñas de producto en G2](https://www.g2.com/sellers/nymiz); por ahora la dejaría como candidata a probar, sin afirmar reputación comunitaria consolidada. [Producto oficial](https://www.nymiz.com/).

## Matriz de los 93 controles

«Sin herramienta validada» evita presentar como compra obligatoria una práctica humana o una categoría para la que aún no se investigó un producto con suficiente respaldo. Los productos de la columna final ayudan únicamente en la tarea descrita, no en el control entero.

### 5. Controles organizativos (37)

| Control | Operación manual mínima | Herramienta que facilita una parte |
|---|---|---|
| 5.1 Política de seguridad | Redactar, aprobar, comunicar y revisar versiones | DOC: control documental y acuse de revisión |
| 5.2 Roles de seguridad | Asignar responsables y revisar RACI | DOC: publicar RACI; FLU: asignar responsables de tareas |
| 5.3 Separación de funciones | Identificar conflictos y revisar accesos | ID: roles y aprobaciones; FLU: flujo de doble aprobación |
| 5.4 Responsabilidades directivas | Supervisar objetivos y exigir seguimiento | DOC: acuerdos y actas; FLU: acciones pendientes |
| 5.5 Contacto con autoridades | Mantener contactos, criterios y suplentes | DOC: directorio protegido; no sustituye la comunicación real |
| 5.6 Contacto con comunidades especializadas | Designar participación y registrar aprendizaje | DOC: registro de fuentes; sin herramienta validada específica |
| 5.7 Inteligencia de amenazas | Revisar fuentes relevantes y decidir acciones | SIEM: correlacionar indicadores propios; no reemplaza análisis de inteligencia |
| 5.8 Seguridad en proyectos | Incluir riesgos y revisiones en cada proyecto | FLU: hitos y aprobaciones; APP: hallazgos técnicos si hay desarrollo |
| 5.9 Inventario de activos e información | Identificar propietario, ubicación y criticidad | MDM: equipos gestionados; FLU: registro de activos no técnicos |
| 5.10 Uso aceptable de activos | Definir reglas y comunicar consecuencias | DOC: política y acuse; MDM: aplicar algunas restricciones |
| 5.11 Devolución de activos | Lista de salida y verificación física | FLU: checklist de baja; MDM: bloqueo/borrado remoto si procede |
| 5.12 Clasificación de información | Definir niveles y decidir clase por propietario | DOC: criterio y registro; sin herramienta validada específica de clasificación |
| 5.13 Etiquetado de información | Aplicar marcas según clasificación | DOC: plantillas; la marca no demuestra tratamiento correcto |
| 5.14 Transferencia de información | Autorizar destinatarios y proteger el envío | SEC: intercambio de secretos; ID: acceso a servicios; revisar canal y cifrado |
| 5.15 Control de acceso | Definir necesidad, aprobar y revisar permisos | ID: SSO/MFA y grupos; el dueño del dato decide autorización |
| 5.16 Gestión de identidades | Alta, cambio, baja y reconciliación | ID: identidades; FLU: solicitudes y aprobaciones |
| 5.17 Información de autenticación | Reglas de creación, custodia y recuperación | SEC: bóvedas; ID: MFA y políticas de autenticación |
| 5.18 Derechos de acceso | Aprobar, revisar y revocar derechos | ID: asignación/revocación; FLU: evidencia de revisión |
| 5.19 Seguridad en relaciones con proveedores | Inventariar y clasificar proveedores | PRO: expedientes y señales externas; la decisión es humana |
| 5.20 Seguridad en contratos con proveedores | Negociar cláusulas y responsabilidades | DOC: versiones; PRO: evidencias; requiere revisión jurídica |
| 5.21 Cadena de suministro TIC | Identificar subproveedores y dependencias | PRO: seguimiento externo; APP: dependencias de software propias |
| 5.22 Seguimiento de servicios de proveedores | Revisar SLA, incidentes y cambios | PRO: vigilancia; FLU: hallazgos y acciones |
| 5.23 Uso seguro de nube | Evaluar arquitectura, responsabilidad compartida y salida | PRO: evaluar proveedor; ID: acceso; SIEM: actividad; ninguno cubre todo |
| 5.24 Preparación ante incidentes | Definir roles, playbooks y ejercicios | DOC: planes; FLU: flujo de incidentes |
| 5.25 Evaluación de eventos | Definir severidad y decidir escalamiento | SIEM: alertas; FLU: triage y decisión documentada |
| 5.26 Respuesta a incidentes | Contener, comunicar, erradicar y recuperar | FLU: coordinación; SIEM: datos de investigación |
| 5.27 Aprendizaje de incidentes | Analizar causas y verificar mejoras | FLU: acciones; DOC: lecciones y cambios de procedimiento |
| 5.28 Recolección de evidencia | Establecer custodia, integridad y retención | SIEM: registros; FLU: cadena de custodia; requiere proceso forense |
| 5.29 Seguridad durante interrupciones | Priorizar funciones y reglas temporales | DOC: planes; BAK: recuperar datos; MON: detectar degradación |
| 5.30 Preparación TIC para continuidad | Definir RTO/RPO y probar recuperación | BAK: restauraciones; MON: disponibilidad; pruebas reales obligatorias |
| 5.31 Requisitos legales y contractuales | Mantener matriz legal y revisar cambios | DOC: registro; sin herramienta validada que interprete toda la ley |
| 5.32 Propiedad intelectual | Identificar licencias, titulares y permisos | COD: licencias/repositorio; revisión legal y contractual humana |
| 5.33 Protección de registros | Definir retención, acceso y destrucción | DOC: versiones; BAK: disponibilidad; verificar retención legal |
| 5.34 Privacidad y datos personales | Mapear tratamientos y bases, minimizar datos | DAT: datos de prueba; PRO: evaluar encargados; requiere análisis legal |
| 5.35 Revisión independiente | Encargar revisión externa y gestionar hallazgos | FLU: seguimiento; la independencia no la da la plataforma |
| 5.36 Cumplimiento de políticas | Muestrear prácticas y corregir desvíos | SIEM: evidencias técnicas; FLU: hallazgos; auditoría humana |
| 5.37 Procedimientos operativos | Documentar pasos, responsables y actualización | DOC: procedimientos versionados; FLU: ejecución recurrente |

### 6. Controles de personas (8)

| Control | Operación manual mínima | Herramienta que facilita una parte |
|---|---|---|
| 6.1 Verificación previa | Definir verificaciones legales, proporcionales y consentidas | FLU: checklist; sin servicio de screening recomendado universalmente |
| 6.2 Términos de empleo | Incluir deberes de seguridad en acuerdos | DOC: versión y acuse; revisión laboral humana |
| 6.3 Formación y conciencia | Enseñar, reforzar y medir aprendizaje | FOR: campañas y registros; sesiones adaptadas siguen siendo necesarias |
| 6.4 Proceso disciplinario | Definir reglas justas y aplicar con RR. HH. | DOC: política; ninguna herramienta decide una medida disciplinaria |
| 6.5 Responsabilidades al salir o cambiar | Recordar deberes y cerrar accesos/activos | FLU: flujo de salida; ID: revocación; MDM: equipo |
| 6.6 Acuerdos de confidencialidad | Definir alcance, firmar y revisar vigencia | DOC: plantillas y registro; firma y validez dependen del contexto |
| 6.7 Trabajo remoto | Fijar condiciones, medios y revisión | MDM: configuración de equipo; ID: acceso; FOR: formación |
| 6.8 Reporte de eventos | Dar canal sencillo y entrenar su uso | FLU: canal/ticket; FOR: enseñar a reportar |

### 7. Controles físicos (14)

| Control | Operación manual mínima | Herramienta que facilita una parte |
|---|---|---|
| 7.1 Perímetro físico | Delimitar zonas, inspeccionar barreras | FIS: acceso a puertas; no reemplaza muros/cerramientos |
| 7.2 Entrada física | Autorizar, registrar y revocar entradas | FIS: credenciales y registros; política de visitantes manual |
| 7.3 Oficinas y salas | Definir zonas y revisar cierres | FIS: puertas controladas; inspección física necesaria |
| 7.4 Vigilancia física | Vigilar entradas y responder alertas | FIS: eventos/cámaras según plan; revisar privacidad y retención |
| 7.5 Amenazas ambientales | Evaluar incendio, agua, temperatura y ubicación | MON: alertas si hay sensores compatibles; equipamiento aparte |
| 7.6 Trabajo en áreas seguras | Autorizar actividades y supervisar visitantes | FIS: acceso; instrucciones y supervisión humanas |
| 7.7 Mesa y pantalla limpias | Inspeccionar puestos y bloquear pantallas | MDM: bloqueo automático; inspección y hábitos manuales |
| 7.8 Ubicación y protección de equipos | Evitar exposición a golpes, calor o robo | MON: temperatura/disponibilidad; ubicación física se decide en sitio |
| 7.9 Activos fuera de instalaciones | Autorizar préstamo y proteger transporte | MDM: cifrado y borrado; FLU: custodia y devolución |
| 7.10 Medios de almacenamiento | Inventariar, restringir, transportar y destruir | MDM: algunas políticas de medio extraíble; destrucción física aparte |
| 7.11 Servicios de soporte | Evaluar energía, climatización y redundancia | MON: alertas; UPS y mantenimiento se contratan aparte |
| 7.12 Cableado | Inspeccionar rutas y proteger puntos expuestos | Sin herramienta validada; planos e inspecciones son centrales |
| 7.13 Mantenimiento de equipos | Programar, autorizar y registrar trabajos | FLU: órdenes y evidencias; proveedor técnico sigue siendo necesario |
| 7.14 Eliminación/reutilización segura | Borrar o destruir y verificar medios | MDM: borrado de ciertos equipos; certificado/verificación adicional |

### 8. Controles tecnológicos (34)

| Control | Operación manual mínima | Herramienta que facilita una parte |
|---|---|---|
| 8.1 Dispositivos de usuario | Configurar, cifrar, actualizar y revisar | MDM: políticas e inventario; PAR: actualizaciones compatibles |
| 8.2 Acceso privilegiado | Aprobar privilegios mínimos y revisarlos | ID: grupos/MFA; SEC: credenciales; revisar uso real |
| 8.3 Restricción de información | Definir permisos por necesidad | ID: identidad; COD: permisos de repositorio; configuración por sistema |
| 8.4 Acceso a código fuente | Autorizar colaboradores y revisar repositorios | COD: reglas de rama y revisión; revisar permisos y secretos |
| 8.5 Autenticación segura | Exigir MFA y mecanismos adecuados | ID: MFA/SSO; SEC: contraseñas; recuperación requiere controles propios |
| 8.6 Capacidad | Medir consumo, prever crecimiento y actuar | MON: tendencias y alertas; planificación humana |
| 8.7 Malware | Definir prevención, actualización y respuesta | SIEM: detectar señales; MDM: configuración; sin producto antimalware validado aquí |
| 8.8 Vulnerabilidades técnicas | Descubrir, priorizar, parchear y verificar | VRX o PAR: remediación; APP: dependencias; el riesgo requiere priorización |
| 8.9 Configuración | Mantener baselines, cambios y desvíos | MDM: endpoints; SIEM: algunas comprobaciones; RED: reglas de red |
| 8.10 Eliminación de información | Definir plazos y comprobar borrado | MDM: borrado de equipos; BAK: revisar retención de copias |
| 8.11 Enmascaramiento | Clasificar datos, aplicar reglas y probar reidentificación | DAT: datos de prueba; muestras y evaluación de privacidad imprescindibles |
| 8.12 Prevención de fuga | Mapear canales, aplicar reglas y revisar alertas | Sin DLP específico validado; MDM/ID solo apoyan acceso y dispositivos |
| 8.13 Respaldo | Establecer frecuencia, cifrar y probar restauración | BAK: copias y recuperación; pruebas periódicas |
| 8.14 Redundancia | Diseñar y ensayar conmutación | MON: detectar caída; infraestructura redundante se diseña aparte |
| 8.15 Registro de eventos | Elegir eventos, proteger y retener logs | SIEM: centralizar y alertar; confirmar cobertura/retención |
| 8.16 Monitoreo | Definir casos de uso y responder | SIEM: alertas; MON: estado técnico; analista valida señales |
| 8.17 Sincronización de relojes | Configurar hora fiable y revisar desvíos | MON: avisar desvíos si se configura; NTP requiere fuente y operación |
| 8.18 Utilidades privilegiadas | Restringir herramientas administrativas | ID: acceso; SIEM: uso; lista autorizada/manual |
| 8.19 Instalación de software | Autorizar aplicaciones y cambios | MDM: catálogo/restricciones; PAR: versiones admitidas |
| 8.20 Seguridad de redes | Definir reglas, segmentar y revisar tráfico | RED: firewall/VPN; SIEM: telemetría; arquitectura propia |
| 8.21 Servicios de red | Contratar, configurar y supervisar servicios | RED: política de red propia; PRO: proveedor externo; MON: disponibilidad |
| 8.22 Segmentación de redes | Diseñar zonas y probar aislamiento | RED: reglas/VLAN; pruebas de comunicación manuales |
| 8.23 Filtrado web | Definir categorías, excepciones y revisar bloqueos | RED: reglas DNS/web según configuración; validar alcance real |
| 8.24 Criptografía | Elegir algoritmos, llaves y rotación | SEC: secretos; MDM: cifrado de equipos; gestión de llaves aparte |
| 8.25 Desarrollo seguro | Definir revisiones y puertas de entrega | COD: revisión/CI; APP: análisis; proceso de desarrollo humano |
| 8.26 Requisitos de seguridad de aplicaciones | Traducir riesgos en criterios verificables | FLU: requisitos; COD: revisión; APP: hallazgos parciales |
| 8.27 Arquitectura segura | Revisar límites de confianza y decisiones | DOC: decisiones; RED/ID: algunas medidas; revisión experta |
| 8.28 Programación segura | Establecer pautas y revisar código | COD: peer review; APP: SAST/SCA; falsos positivos y omisiones |
| 8.29 Pruebas de seguridad | Definir alcance y comprobar correcciones | APP: pruebas automatizadas; FLU: hallazgos; pruebas manuales necesarias |
| 8.30 Desarrollo tercerizado | Pactar obligaciones, revisar entregables | PRO: proveedor; COD: entregas y revisión; contrato y validación humana |
| 8.31 Entornos separados | Separar identidades, redes y datos | COD: ramas/entornos; ID: accesos; DAT: datos de prueba; diseño aparte |
| 8.32 Cambios | Solicitar, aprobar, desplegar y revertir | FLU: aprobaciones; COD: PR y despliegues; verificar resultado |
| 8.33 Información de prueba | Evitar PII real o reducirla de forma demostrable | DAT: desidentificación; verificar calidad y riesgo de reidentificación |
| 8.34 Protección durante auditorías técnicas | Pactar alcance, ventanas y custodia de resultados | FLU: autorizaciones; SIEM: trazas; supervisión humana |

## Evaluación mínima del proveedor y del riesgo introducido

Antes de usar cualquiera de los servicios anteriores, documentar al menos: datos y privilegios que recibirá; ubicación y retención de datos; subprocesadores; autenticación, roles y registros administrativos; controles y evidencia de seguridad del proveedor; notificación de incidentes; disponibilidad y continuidad; integración y reversibilidad; portabilidad y borrado al salir; licencias, costos de crecimiento y soporte; restricciones legales/contractuales; riesgos de configuración, dependencia, fallas y concentración. Aprobar con el dueño del riesgo y revisar periódicamente. Para herramientas **autohospedadas**, evaluar también el origen del software, actualizaciones, soporte, vulnerabilidades y capacidad operativa propia.

**Limitaciones de esta versión:** es un catálogo de apoyo, no una evaluación técnica de cada producto ni una declaración de aplicabilidad. No se probaron productos en un entorno real. Varias actividades físicas, legales y de personal no tienen una recomendación de software porque el acto de comprarlo aportaría poco o aún falta evidencia suficiente. En una siguiente iteración pueden añadirse alternativas por presupuesto y región, y pruebas prácticas con escenarios reproducibles.
