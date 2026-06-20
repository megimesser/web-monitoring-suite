# Testsuite

> Automatisierte Test- und Monitoring-Suite für einen Webflow-Kundenauftritt (wohnbautrend.de) und die zugehörigen Gmail-API-Workflows.

Geschrieben in Python. Kombiniert Selenium-basiertes Prüfen der Website mit Gmail-API-Automation über OAuth2.

---

## Motivation

Nach dem Launch der Kundenseite **wohnbautrend.de** (erstellt mit Webflow) brauchte ich eine automatisierte Möglichkeit, die Seite regelmäßig auf Erreichbarkeit, korrekte CMS-Inhalte und funktionierende Filter zu prüfen — statt manuell durchzuklicken. Diese Suite übernimmt diese Checks und meldet Abweichungen, sodass Probleme erkannt werden, bevor der Kunde sie bemerkt.
