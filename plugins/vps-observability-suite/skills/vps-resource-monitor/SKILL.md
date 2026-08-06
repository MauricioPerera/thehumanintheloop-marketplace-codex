---
name: vps-resource-monitor
description: Mide CPU, RAM, disco, inodos, procesos y carga de un VPS por SSH con umbrales y evidencia temporal.
---
# VPS Resource Monitor
Usa lecturas nativas (`uptime`, `free`, `df`, `vmstat`, `ps`, `ss`) y Docker si existe. Reporta timestamp, unidad, umbral, tendencia y limitaciones. No instala agentes, mata procesos ni cambia sysctl; las acciones correctivas requieren un plan separado.
