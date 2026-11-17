# Estrategia técnica — AI Job Hunter

## 1. Objetivo

Este documento define la estrategia técnica definitiva del PMV: tecnologías, arquitectura, estructura del repositorio, componentes, flujo de datos y criterios de implementación.

La especificación funcional se mantiene en docs/pmv-specification.md y el trabajo pendiente en docs/plan-de-tareas.md.

## 2. Stack tecnológico

| Componente | Tecnología |
|---|---|
| Lenguaje | Python 3.12+ |
| Backend/API | FastAPI |
| Base de datos | PostgreSQL |
| ORM | SQLAlchemy 2 |
| Migraciones | Alembic |
| Validación/configuración | Pydantic 2 / Pydantic Settings |
| Cliente HTTP | httpx |
| Scheduler | APScheduler |
| Matching | Motor determinista + análisis semántico con IA |
| Frontend PMV | Jinja2 + HTMX + Bootstrap |
| Tests | pytest |
| Calidad de código | Ruff |
| Entorno/paquetes | Python virtualenv + requirements.txt inicialmente |
| Contenedores | Docker + Docker Compose |
| Control de versiones | Git + GitHub |
| CI | GitHub Actions |

El PMV utilizará una arquitectura monolítica modular. No se introducen microservicios, React/Next.js, Kubernetes, Celery ni Redis salvo que una necesidad técnica posterior lo justifique.

## 3. Arquitectura

Flujo principal:

InfoJobs → Collector → Normalizer → PostgreSQL → Matching Engine → Filtro de relevancia → Resumen → Interfaz web.

El Scheduler inicia periódicamente el proceso.

InfoJobs queda aislado detrás de una interfaz de collector para poder añadir otros portales posteriormente sin modificar el núcleo del sistema.

## 4. Estructura

    AI-Job-Hunter/
    ├── README.md
    ├── .gitignore
    ├── .env.example
    ├── requirements.txt
    ├── Dockerfile
    ├── docker-compose.yml
    ├── .github/
    │   └── workflows/
    │       └── ci.yml
    ├── docs/
    │   ├── pmv-specification.md
    │   ├── technical-strategy.md
    │   ├── database.md
    │   └── plan-de-tareas.md
    ├── src/
    │   └── job_hunter/
    │       ├── __init__.py
    │       ├── main.py
    │       ├── config.py
    │       ├── api/
    │       │   └── routes/
    │       ├── database/
    │       │   ├── connection.py
    │       │   ├── models/
    │       │   └── repositories/
    │       ├── domain/
    │       │   ├── models/
    │       │   └── enums.py
    │       ├── scrapers/
    │       │   ├── base.py
    │       │   └── infojobs.py
    │       ├── matching/
    │       │   ├── engine.py
    │       │   ├── rules.py
    │       │   └── ai.py
    │       ├── services/
    │       │   ├── offer_service.py
    │       │   ├── matching_service.py
    │       │   └── search_service.py
    │       ├── scheduler/
    │       │   └── scheduler.py
    │       └── web/
    │           ├── templates/
    │           └── static/
    ├── tests/
    │   ├── database/
    │   ├── matching/
    │   ├── scrapers/
    │   └── services/
    └── data/

## 5. Base de datos

La arquitectura definitiva utilizará PostgreSQL y SQLAlchemy 2.

Entidades previstas:

- UserProfile
- Education
- Experience
- Certification
- Skill
- Preference
- Search
- Offer
- OfferAnalysis
- MatchScore
- OfferHistory

Offer utilizará el identificador externo del portal como identidad principal cuando esté disponible. En caso contrario se utilizará una estrategia alternativa basada en URL, empresa, título y ubicación.

El sistema distinguirá ofertas nuevas, existentes sin cambios, existentes modificadas, cerradas y expiradas.

Una oferta sin cambios no deberá volver a analizarse con IA innecesariamente.

## 6. Matching híbrido

El score será de 0 a 100 y combinará reglas deterministas con análisis semántico.

Factores iniciales:

- ubicación;
- experiencia;
- formación;
- competencias;
- salario;
- jornada/turno;
- contrato;
- sector.

Los pesos y penalizaciones serán configurables y se validarán durante el desarrollo con ofertas reales.

La IA no será la única fuente del score.

Flujo:

Oferta → filtros deterministas → score base → análisis semántico cuando proceda → score final → filtro de relevancia.

El resultado será explicable: la interfaz mostrará la puntuación y los principales motivos positivos y negativos.

## 7. Uso de IA

La IA se utilizará para:

- interpretación semántica de requisitos;
- comparación entre experiencia y descripción;
- detección de equivalencias entre términos;
- generación del resumen;
- explicación de por qué una oferta encaja.

No se utilizará IA cuando filtros deterministas permitan descartar claramente una oferta.

## 8. Pipeline

    search()
        ↓
    collect_offers()
        ↓
    normalize_offers()
        ↓
    save_or_update()
        ↓
    detect_changes()
        ↓
    match_profile()
        ↓
    apply_filters()
        ↓
    generate_summary()
        ↓
    update_status()

Cada etapa tendrá responsabilidades separadas y será testeable de forma independiente.

## 9. Scheduler

La frecuencia será configurable mediante SCAN_INTERVAL_MINUTES=60.

Valores previstos: 30, 60, 120, 180 y 360 minutos.

Se utilizará APScheduler y no esperas manuales con sleep().

## 10. Interfaz

El PMV utilizará Jinja2 + HTMX + Bootstrap.

La pantalla principal mostrará:

- ofertas nuevas;
- ofertas relevantes;
- última búsqueda;
- próxima búsqueda;
- filtros;
- ofertas ordenadas por relevancia;
- score;
- resumen;
- motivos de coincidencia;
- botón APLICAR.

APLICAR abrirá la oferta original de InfoJobs. El PMV no realizará candidaturas automáticas.

## 11. Seguridad

- secretos mediante variables de entorno;
- API keys fuera del repositorio;
- credenciales de base de datos fuera del código;
- minimización de datos personales;
- base de datos protegida;
- no publicar el perfil completo;
- no almacenar contraseñas de portales;
- no automatizar candidaturas en el PMV.

## 12. Docker

El entorno deberá poder arrancarse con:

    docker compose up

La composición inicial tendrá aplicación Python y PostgreSQL.

## 13. Tests

Se incorporarán desde las primeras fases.

Áreas prioritarias:

- reglas de matching;
- cálculo del score;
- deduplicación;
- persistencia;
- detección de cambios;
- parsing y normalización;
- servicios;
- pipeline.

Caso crítico: si la misma oferta se recibe dos veces, debe existir una única oferta en la base de datos.

## 14. CI

GitHub Actions ejecutará:

1. instalación de dependencias;
2. comprobaciones de calidad;
3. tests;
4. build de la aplicación.

## 15. Alcance

### Incluido

- InfoJobs;
- perfil profesional;
- preferencias;
- PostgreSQL;
- deduplicación;
- historial;
- matching;
- IA;
- score;
- filtro de relevancia;
- resumen;
- scheduler;
- interfaz;
- APLICAR;
- tests;
- Docker;
- CI.

### Fuera del PMV

- LinkedIn;
- Indeed;
- Adecco;
- Eurofirms;
- candidatura automática;
- generación automática de CV;
- cartas automáticas;
- gestión completa de candidaturas;
- predicción de contratación;
- agente autónomo.

## 16. Orden de implementación

1. Arquitectura y configuración
2. Base de datos
3. Perfil y preferencias
4. Integración con InfoJobs
5. Deduplicación e historial
6. Matching
7. IA
8. Scheduler
9. Interfaz
10. Tests e integración
11. Docker y CI
12. Prueba final del PMV

No se implementará el collector de InfoJobs antes de cerrar la arquitectura de persistencia y dominio.

## 17. Validación del stack frente a proyectos similares

Se revisaron repositorios públicos de agregadores de empleo, sistemas de matching y asistentes de búsqueda laboral. Se repiten especialmente FastAPI/Python en backend, PostgreSQL + SQLAlchemy en persistencia, Alembic para migraciones, Docker, pytest y GitHub Actions. Los proyectos de mayor escala suelen añadir Celery + Redis para procesamiento distribuido y React/Next.js para interfaces SPA; otros proyectos de un solo usuario utilizan Jinja2 con FastAPI y PostgreSQL.

Ejemplos revisados:

- Job Service: FastAPI + PostgreSQL + SQLAlchemy y runner programado para agregación de ofertas.
- CareerPilot: FastAPI + PostgreSQL + pgvector + SQLAlchemy + Next.js.
- Job Radar: FastAPI + PostgreSQL + Celery + Redis + Next.js.
- agenticJobSearch: FastAPI + Jinja2 + PostgreSQL + SQLAlchemy + Alembic + Docker + pytest + GitHub Actions.
- Smart Job Recommendation System: FastAPI + PostgreSQL + SQLAlchemy + Alembic + scikit-learn.

La conclusión es que el stack inicialmente definido es correcto para el PMV, pero se incorporan dos herramientas que aparecen repetidamente en proyectos más maduros: **Alembic** para migraciones y **Ruff** para calidad de código.

No se adopta Celery + Redis porque el PMV será inicialmente una aplicación de un solo usuario con búsquedas periódicas cada 60 minutos. Añadir un broker y workers distribuidos aumentaría considerablemente la complejidad sin aportar una ventaja proporcional. Tampoco se adopta React/Next.js: Jinja2 + HTMX mantiene el PMV como monolito sencillo y permite construir la interfaz necesaria sin introducir un segundo runtime.

## 18. Decisión técnica definitiva

**Python 3.12+ + FastAPI + PostgreSQL + SQLAlchemy 2 + Alembic + Pydantic 2 + httpx + APScheduler + Jinja2/HTMX/Bootstrap + matching híbrido + IA + pytest + Ruff + Docker + GitHub Actions.**

Arquitectura: **monolito modular**, preparado para incorporar nuevos portales posteriormente.

Principio de decisión: utilizar herramientas ampliamente presentes en proyectos similares, pero evitar componentes de infraestructura distribuidos que el PMV no necesita todavía.
