#!/usr/bin/env python3
"""Generate the offline control finder from the repository's editorial guide."""

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "marcos/iso-27001/herramientas-vs-manual-iso-27002.md"
OUTPUT = ROOT / "docs/data.js"

# Prices are reference prices from the guide's October 2026 review, not live quotes.
# risk describes an additional supplier or deployment risk to assess, not a defect.
TOOLS = {
    "MISP": ("https://www.misp-project.org/features/", "Gratis; infraestructura y operación aparte", "gratis", "Autogestionado", "Calidad y licencia de las fuentes de inteligencia"),
    "Active Directory DS": ("https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/active-directory-domain-services", "Windows Server y CAL; sin precio independiente", "licencia", "Local o nube propia", "Privilegios del directorio y continuidad de la autenticación"),
    "Jira Service Management": ("https://www.atlassian.com/collections/service/pricing?bundle=jira-service-management", "Standard: USD 20/agente/mes", "pago", "SaaS", "Datos de incidentes y accesos del proveedor"),
    "Microsoft Intune": ("https://www.microsoft.com/security/business/microsoft-intune-pricing", "Plan 1: USD 8/usuario/mes, anual", "pago", "SaaS", "Agentes y permisos de administración de equipos"),
    "Wazuh": ("https://wazuh.com/", "Gratis; infraestructura y operación aparte", "gratis", "Autogestionado", "Telemetría sensible, retención y protección de logs"),
    "UpGuard Vendor Risk": ("https://www.upguard.com/pricing/vendor-risk", "Desde USD 1.750/mes, anual", "pago", "SaaS", "Datos de terceros y dependencia de sus evaluaciones"),
    "Snyk": ("https://snyk.io/plans/", "Free USD 0; Team desde USD 25/mes", "freemium", "SaaS", "Acceso a repositorios, dependencias y resultados"),
    "Kisi": ("https://www.getkisi.com/pricing", "Desde USD 99/mes; hardware aparte", "pago", "SaaS + hardware", "Continuidad del acceso físico y datos de entradas"),
    "GitHub Team": ("https://github.com/team", "USD 4/usuario/mes", "pago", "SaaS", "Acceso a código y permisos de integración"),
    "Action1": ("https://www.action1.com/", "Gratis hasta 200 equipos; más: cotización", "freemium", "SaaS", "Agente con capacidad de despliegue y privilegios remotos"),
    "Tonic Structural": ("https://www.tonic.ai/pricing", "No se encontró precio público", "cotizacion", "SaaS", "Acceso a datos de origen y posibilidad de reidentificación"),
    "Netgate pfSense": ("https://www.netgate.com/pfsense-plus-software/software-types", "CE gratis; Plus desde USD 129/instancia/año", "freemium", "Autogestionado", "Cambios de red y disponibilidad del firewall"),
    "Vicarius vRx": ("https://www.vicarius.io/features/patch-management", "No se encontró precio público; cotización", "cotizacion", "SaaS", "Agente y automatización de cambios con privilegios"),
    "Veeam Data Platform Essentials": ("https://www.veeam.com/products/veeam-data-platform/essentials.html", "Desde USD 95/licencia/año; paquetes de 5", "pago", "Autogestionado", "Acceso privilegiado a respaldos y repositorios"),
    "KnowBe4 Security Awareness Training": ("https://www.knowbe4.com/products/security-awareness-training/pricing", "Desde USD 2,40/persona/mes; contrato de 3 años", "pago", "SaaS", "Datos de personas y resultados de formación"),
    "OneTrust Privacy Automation": ("https://www.onetrust.com/solutions/privacy-automation/", "No se encontró precio público; cotización", "cotizacion", "SaaS", "Datos personales y flujos de tratamiento compartidos"),
    "Microsoft Entra ID": ("https://learn.microsoft.com/en-us/entra/identity/authentication/concept-mfa-licensing", "MFA básico gratis; P1 USD 7/usuario/mes", "freemium", "SaaS", "Dependencia de identidad y privilegios administrativos"),
    "Zabbix": ("https://www.zabbix.com/features", "Gratis; infraestructura y operación aparte", "gratis", "Autogestionado", "Credenciales de monitoreo y carga de agentes"),
    "Cortex XDR": ("https://www.paloaltonetworks.com/cortex/endpoint-protection", "No se encontró precio público; cotización", "cotizacion", "SaaS", "Agente de equipo, telemetría y acceso de respuesta"),
    "Microsoft Purview DLP": ("https://learn.microsoft.com/en-us/purview/dlp-learn-about-dlp", "Según licencia y funciones; sin precio independiente", "licencia", "SaaS", "Inspección de contenido, privacidad y falsos positivos"),
    "chrony": ("https://chrony-project.org/", "Gratis; operación aparte", "gratis", "Local", "Confianza y disponibilidad de fuentes horarias"),
    "Cloudflare Gateway": ("https://www.cloudflare.com/products/gateway/", "Gratis hasta 50 usuarios; verificar límites", "freemium", "SaaS", "Visibilidad de navegación y dependencia del proveedor"),
    "HashiCorp Vault": ("https://developer.hashicorp.com/vault/docs/secrets/transit", "Community sin licencia; Enterprise: cotización", "freemium", "Autogestionado", "Disponibilidad y custodia de claves maestras"),
}

DESCRIPTIONS = {
    "MISP": "Relaciona y comparte indicadores e información de amenazas.",
    "Active Directory DS": "Centraliza usuarios, grupos y permisos en entornos Windows.",
    "Jira Service Management": "Coordina tickets, aprobaciones e incidentes.",
    "Microsoft Intune": "Administra dispositivos y aplica políticas a equipos incorporados.",
    "Wazuh": "Centraliza eventos, alertas y revisiones de configuración.",
    "UpGuard Vendor Risk": "Organiza evaluaciones y seguimiento de proveedores.",
    "Snyk": "Analiza código y dependencias compatibles.",
    "Kisi": "Gestiona credenciales y registra entradas físicas.",
    "GitHub Team": "Facilita permisos de repositorio y revisión de cambios.",
    "Action1": "Detecta faltantes y despliega parches compatibles.",
    "Tonic Structural": "Genera datos de prueba desidentificados.",
    "Netgate pfSense": "Administra firewall, VPN y segmentación de red.",
    "Vicarius vRx": "Prioriza vulnerabilidades y automatiza opciones de remediación.",
    "Veeam Data Platform Essentials": "Respalda y recupera cargas compatibles.",
    "KnowBe4 Security Awareness Training": "Gestiona campañas y seguimiento de formación.",
    "OneTrust Privacy Automation": "Organiza tratamientos, evaluaciones y solicitudes de titulares.",
    "Microsoft Entra ID": "Aplica MFA y políticas de identidad.",
    "Zabbix": "Recoge métricas, alerta y muestra tendencias de capacidad.",
    "Cortex XDR": "Previene y detecta amenazas en equipos incorporados.",
    "Microsoft Purview DLP": "Aplica políticas de prevención de fuga en ubicaciones compatibles.",
    "chrony": "Sincroniza relojes de sistemas compatibles mediante NTP.",
    "Cloudflare Gateway": "Filtra consultas DNS y tráfico web de usuarios incorporados.",
    "HashiCorp Vault": "Gestiona secretos y operaciones criptográficas para aplicaciones integradas.",
}

CHECKS = {
    "A.5.7": "Registrar una señal relevante, su análisis y la decisión tomada.",
    "A.5.9": "Contrastar una muestra de activos reales con propietario y criticidad en el inventario.",
    "A.5.16": "Probar altas, cambios y bajas; revisar una muestra de cuentas huérfanas.",
    "A.5.19": "Revisar la evaluación de un proveedor y una acción de seguimiento.",
    "A.5.34": "Trazar un tratamiento y una solicitud de titular con evidencia de respuesta.",
    "A.8.7": "Confirmar cobertura de equipos y una alerta gestionada.",
    "A.8.8": "Elegir un hallazgo, aplicar la corrección y verificarlo con un nuevo análisis.",
    "A.8.9": "Comparar equipos con una línea base aprobada y resolver un desvío.",
    "A.8.11": "Comprobar utilidad del dato de prueba y riesgo de reidentificación.",
    "A.8.12": "Probar con datos sintéticos el bloqueo o la alerta en un canal definido.",
    "A.8.13": "Restaurar una muestra y medir integridad y tiempo de recuperación.",
    "A.8.15": "Buscar un evento esperado y verificar integridad, acceso y retención.",
    "A.8.20": "Comprobar una regla de red con tráfico permitido y denegado.",
    "A.8.32": "Seguir un cambio desde aprobación hasta despliegue y reversión.",
}


def expand_controls(value):
    result = []
    for part in value.split(","):
        part = part.strip()
        match = re.fullmatch(r"A\.(\d)\.(\d+)\s*[–-]\s*A\.(\d)\.(\d+)", part)
        if match:
            group, start, end_group, end = map(int, match.groups())
            if group != end_group:
                raise ValueError(f"Range crosses group: {part}")
            result.extend(f"A.{group}.{number}" for number in range(start, end + 1))
        elif re.fullmatch(r"A\.[5-8]\.\d+", part):
            result.append(part)
        else:
            raise ValueError(f"Invalid control: {part}")
    return result


def build():
    source = SOURCE.read_text(encoding="utf-8")
    controls = []
    full = source.split("## Los 93 controles, en una línea cada uno", 1)[1].split("## ¿A cuántos controles ayuda cada herramienta?", 1)[0]
    for line in full.splitlines():
        match = re.fullmatch(r"\| \*\*(A\.[5-8]\.\d+) ([^*]+)\*\* \| ([^|]+) \| ([^|]+) \|", line)
        if match:
            identifier, title, manual, _ = match.groups()
            controls.append({"id": identifier, "title": title, "manual": manual.strip(), "tools": [], "check": CHECKS.get(identifier, "Elegir una muestra, comprobar el resultado y guardar evidencia fechada.")})
    ids = {control["id"] for control in controls}
    if len(controls) != 93 or len(ids) != 93:
        raise ValueError(f"Expected 93 unique controls, got {len(controls)} rows/{len(ids)} unique")

    stats = source.split("## ¿A cuántos controles ayuda cada herramienta?", 1)[1]
    tools = {}
    for line in stats.splitlines():
        match = re.fullmatch(r"\| ([^|]+) \| ([^|]+) \| \*\*(\d+)\*\* \|", line)
        if not match:
            continue
        name, refs, declared = match.groups()
        refs = expand_controls(refs)
        if len(refs) != int(declared):
            raise ValueError(f"Wrong count for {name}")
        if not set(refs) <= ids:
            raise ValueError(f"Unknown control for {name}")
        tools[name] = dict(zip(("url", "price", "pricing", "hosting", "risk"), TOOLS[name]))
        tools[name]["description"] = DESCRIPTIONS[name]
        for control in controls:
            if control["id"] in refs:
                control["tools"].append(name)
    if set(tools) != set(TOOLS) or set(tools) != set(DESCRIPTIONS):
        raise ValueError(f"Tool metadata mismatch: {set(TOOLS) ^ set(tools)}")
    relationships = sum(len(control["tools"]) for control in controls)
    assisted = sum(bool(control["tools"]) for control in controls)
    if (len(tools), relationships, assisted) != (23, 60, 50):
        raise ValueError(f"Unexpected totals: {len(tools)} tools, {relationships} relationships, {assisted} assisted")
    return {"reviewed": "11-10-2026", "controls": controls, "tools": tools}


if __name__ == "__main__":
    data = build()
    OUTPUT.parent.mkdir(exist_ok=True)
    OUTPUT.write_text("window.GRC_DATA = " + json.dumps(data, ensure_ascii=False, separators=(",", ":")) + ";\n", encoding="utf-8")
    print(f"Generated {OUTPUT.relative_to(ROOT)}: 93 controls, 23 tools, 60 relationships")
