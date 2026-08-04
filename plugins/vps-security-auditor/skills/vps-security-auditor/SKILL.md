---
name: vps-security-auditor
description: Audita firewall, puertos, SSH, usuarios, fail2ban y actualizaciones de un VPS por SSH sin aplicar cambios.
---
# VPS Security Auditor
Confirma host, usuario, puerto y huella antes de conectar. Ejecuta lecturas acotadas (`ss`, firewall, servicios SSH/fail2ban, usuarios no privilegiados y paquetes pendientes), redacta rutas sensibles y separa evidencia de recomendaciones. No modifica reglas, usuarios, servicios ni paquetes; cualquier hardening debe convertirse en plan con impacto, rollback y confirmación.
