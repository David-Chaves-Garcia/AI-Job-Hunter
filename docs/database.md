# Diseño de base de datos

Documento inicial para el diseño de persistencia de AI Job Hunter.

## Principios

- PostgreSQL como base de datos principal.
- SQLAlchemy 2 como ORM.
- Identidad externa del portal para deduplicación.
- Separación entre oferta, análisis, score, estado e historial.
- No reanalizar ofertas sin cambios.
- Mantener trazabilidad de búsquedas y modificaciones.

## Entidades previstas

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

El esquema detallado, relaciones, índices y restricciones se definirán durante la implementación de la fase de base de datos.
