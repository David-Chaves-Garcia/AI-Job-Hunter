# AI Job Hunter — Especificación del PMV v1.0

## 1. Objetivo del proyecto

Desarrollar una aplicación que funcione como un **asistente inteligente de búsqueda de empleo**, capaz de recopilar periódicamente ofertas de trabajo de **InfoJobs**, compararlas con el perfil profesional y las preferencias del usuario y mostrar únicamente aquellas ofertas con un alto grado de coincidencia.

El objetivo principal del PMV es:

> **Reducir el tiempo necesario para encontrar ofertas de empleo relevantes, automatizando la búsqueda, análisis y filtrado de ofertas de InfoJobs.**

El sistema no realizará inicialmente la candidatura de forma automática. El usuario podrá acceder directamente a la oferta mediante un botón **APLICAR**.

---

# 2. Alcance del PMV

La primera versión estará limitada a **InfoJobs**.

El sistema deberá realizar las siguientes funciones:

1. Recoger y almacenar el perfil profesional del usuario.
2. Permitir configurar preferencias laborales.
3. Recopilar ofertas de InfoJobs.
4. Guardar las ofertas en una base de datos.
5. Detectar ofertas nuevas.
6. Evitar duplicados.
7. Analizar la coincidencia entre cada oferta y el perfil del usuario.
8. Asignar una puntuación de coincidencia.
9. Filtrar las ofertas según las preferencias del usuario.
10. Mostrar las ofertas relevantes en una interfaz.
11. Mostrar un resumen breve de cada oferta.
12. Permitir acceder directamente a la oferta mediante **APLICAR**.
13. Ejecutar automáticamente nuevas búsquedas en un intervalo configurable.
14. Mantener un historial de ofertas encontradas y analizadas.

---

# 3. Perfil profesional del usuario

La aplicación deberá disponer de un perfil profesional estructurado.

## 3.1 Datos personales

El PMV almacenará únicamente los datos necesarios para el funcionamiento del sistema.

- Nombre
- Apellidos
- Localización
- Código postal
- Radio máximo de desplazamiento
- Disponibilidad laboral

**La fotografía identificativa queda fuera del PMV.**

Podrá incorporarse en versiones posteriores si resulta útil para la gestión de candidaturas.

---

## 3.2 Formación

El usuario podrá registrar:

- Titulación
- Centro educativo
- Fecha de inicio
- Fecha de finalización
- Cursos
- Certificaciones
- Formación adicional

Ejemplo:

```text
Grado en Empresa y Tecnología
Universidad de Santiago de Compostela
```

---

## 3.3 Experiencia profesional

Cada experiencia deberá contener:

- Empresa
- Puesto
- Fecha de inicio
- Fecha de finalización
- Duración
- Sector
- Funciones
- Herramientas utilizadas
- Competencias adquiridas

Ejemplo:

```text
Empresa: IKEA
Puesto: Mozo de almacén
Duración: 3 meses

Funciones:
- Picking
- Preparación de pedidos
- Gestión de stock
- Uso de PDA
```

---

## 3.4 Carnets y acreditaciones

El sistema permitirá registrar:

- Carnet de conducir
- Carnet de carretilla
- Tipos de carretilla
- Certificaciones profesionales
- Otros permisos o acreditaciones

Cada elemento podrá tener información adicional cuando sea relevante.

---

## 3.5 Competencias

El usuario podrá registrar:

### Competencias técnicas

- Power BI
- Excel
- SQL
- PDA
- Gestión de stock
- Etc.

### Idiomas

- Idioma
- Nivel

### Software

- Programa
- Nivel

---

# 4. Preferencias laborales

El usuario deberá poder configurar qué tipo de ofertas quiere encontrar.

Las preferencias serán modificables desde la interfaz.

## 4.1 Localización

- Provincia
- Ciudad
- Código postal
- Radio máximo en kilómetros

Ejemplo:

```text
Castellón
Radio: 25 km
```

---

## 4.2 Salario

- Salario mínimo
- Salario deseado

---

## 4.3 Jornada

- Jornada completa
- Jornada parcial

---

## 4.4 Horario

- Mañana
- Tarde
- Noche
- Turnos
- Turno fijo
- Turnos rotativos

---

## 4.5 Contrato

- Indefinido
- Temporal
- ETT
- Prácticas
- Otros

---

## 4.6 Puestos

El usuario podrá definir:

**Puestos deseados**

y

**Puestos excluidos.**

---

## 4.7 Sectores

El usuario podrá establecer:

- Sectores preferidos
- Sectores excluidos

---

# 5. Recopilación de ofertas de InfoJobs

El sistema tendrá un módulo específico encargado de obtener las ofertas de InfoJobs.

Este módulo deberá ser independiente del resto de la aplicación para facilitar futuras incorporaciones de otros portales.

En el futuro podrán añadirse:

- Indeed
- LinkedIn
- Adecco
- Eurofirms
- Otros

sin modificar el núcleo del sistema.

---

# 6. Información almacenada de cada oferta

Cada oferta deberá almacenarse con la mayor cantidad posible de información útil.

Como mínimo:

- Identificador de la oferta
- Portal
- URL
- Empresa
- Puesto
- Localización
- Salario
- Tipo de contrato
- Jornada
- Horario
- Descripción
- Requisitos
- Experiencia requerida
- Formación requerida
- Competencias requeridas
- Fecha de publicación
- Fecha de detección
- Fecha de última actualización
- Estado

---

# 7. Base de datos

El sistema deberá utilizar una base de datos para almacenar tanto las ofertas actuales como el historial.

La base de datos deberá permitir:

- Detectar duplicados.
- Detectar nuevas ofertas.
- Conservar ofertas antiguas.
- Registrar cuándo se encontró una oferta.
- Registrar cuándo se analizó.
- Guardar la puntuación obtenida.
- Conservar el historial de cambios.
- Evitar procesar repetidamente la misma oferta.

---

# 8. Historial de búsqueda

El sistema deberá conservar un historial de las búsquedas realizadas.

Ejemplo:

```text
17/11/2026 — 10:00
Ofertas encontradas: 87
Ofertas nuevas: 12
Ofertas analizadas: 12
Ofertas con match ≥80: 5
```

La aplicación deberá poder consultar posteriormente este historial.

---

# 9. Identificación de ofertas nuevas

Cada oferta deberá tener un identificador único.

Preferentemente se utilizará el identificador proporcionado por InfoJobs.

Cuando esto no sea suficiente, podrá utilizarse una combinación de elementos como:

- URL
- Empresa
- Título
- Localización

El sistema deberá distinguir entre:

### Oferta conocida

Ya existe en la base de datos.

### Oferta nueva

No existe previamente en la base de datos.

### Oferta actualizada

Existe, pero ha sufrido cambios relevantes.

---

# 10. Sistema de coincidencia

Cada oferta será comparada automáticamente con el perfil profesional y las preferencias del usuario.

El sistema generará una puntuación:

```text
0 — 100
```

Ejemplo:

```text
OPERARIO DE PRODUCCIÓN

Coincidencia: 91/100

Localización      ✓
Salario           ✓
Horario           ✓
Experiencia       ✓
Formación         ✓
Carnets           ✓
Sector            ✓
```

La fórmula definitiva del scoring **no se establecerá en esta fase de documentación**.

Se diseñará durante el desarrollo y se probará utilizando ofertas reales.

El sistema deberá estar diseñado para poder modificar posteriormente:

- Factores
- Pesos
- Penalizaciones
- Umbral mínimo

sin necesidad de reconstruir toda la aplicación.

---

# 11. Filtro de coincidencia

El usuario podrá definir una coincidencia mínima.

Ejemplo:

```text
Mostrar ofertas con:
Coincidencia ≥ 80
```

Por defecto podrá establecerse un valor inicial, pero deberá ser modificable desde la interfaz.

---

# 12. Resumen de la oferta

Cada oferta que supere los filtros deberá mostrar un resumen muy breve.

Ejemplo:

```text
OPERARIO DE PRODUCCIÓN

Empresa: Empresa X
Localización: Castellón
Salario: 30.000–34.000 €
Horario: Turnos rotativos

Coincidencia: 91 %

Puesto industrial de producción. Se requiere
experiencia previa y se valora carnet de carretilla.

[ APLICAR ]
```

El resumen deberá permitir comprender rápidamente:

- Qué puesto es.
- Quién contrata.
- Dónde.
- Cuánto paga, si está disponible.
- Qué horario tiene.
- Por qué encaja con el perfil.

---

# 13. Botón APLICAR

Cada oferta deberá incluir un botón:

**APLICAR**

Al pulsarlo, el usuario será dirigido a la URL original de la oferta en InfoJobs.

El PMV no automatizará el envío de la candidatura.

El objetivo es reducir el número de pasos necesarios para pasar de:

```text
Oferta encontrada
```

a:

```text
Oferta lista para solicitar
```

---

# 14. Actualización automática

El sistema realizará búsquedas periódicas en InfoJobs.

El intervalo deberá ser **configurable**.

Por defecto:

```text
60 minutos
```

Pero el usuario podrá modificarlo.

Ejemplos:

```text
30 minutos
60 minutos
120 minutos
180 minutos
360 minutos
```

El sistema no deberá asumir que el intervalo es fijo.

Internamente deberá existir una configuración similar a:

```text
scan_interval_minutes = 60
```

De esta forma, modificar la frecuencia no requerirá modificar la arquitectura del programa.

---

# 15. Proceso de actualización

Cada ciclo de actualización seguirá aproximadamente este proceso:

```text
INICIO
   │
   ▼
Consultar InfoJobs
   │
   ▼
Obtener ofertas
   │
   ▼
Comparar con base de datos
   │
   ├── Ya existe ──► Comprobar cambios
   │
   └── Nueva ─────► Guardar
                        │
                        ▼
                  Analizar con IA
                        │
                        ▼
                  Calcular score
                        │
                        ▼
                 Aplicar filtros
                        │
                        ▼
                Mostrar si cumple
```

---

# 16. Control de ofertas ya procesadas

El sistema no deberá volver a analizar innecesariamente una oferta que ya ha sido procesada.

Ejemplo:

```text
Oferta #123456
Detectada: 17/11/2026 10:00
Analizada: Sí
Score: 87
```

En la siguiente búsqueda:

```text
Oferta #123456
Ya conocida
→ No volver a analizar si no ha cambiado
```

Esto permitirá reducir:

- Consumo de recursos
- Coste de IA
- Tiempo de procesamiento
- Consultas innecesarias

---

# 17. Ofertas nuevas

Las ofertas detectadas por primera vez deberán marcarse como nuevas.

Ejemplo:

```text
NUEVAS OFERTAS

7 nuevas ofertas encontradas

┌───────────────────────────┐
│ OPERARIO DE PRODUCCIÓN    │
│ Match: 94 %               │
│ [APLICAR]                 │
└───────────────────────────┘

┌───────────────────────────┐
│ MOZO DE ALMACÉN           │
│ Match: 89 %               │
│ [APLICAR]                 │
└───────────────────────────┘
```

Las ofertas nuevas que no alcancen el nivel mínimo de coincidencia no se mostrarán en la vista principal.

---

# 18. Interfaz principal

La interfaz deberá priorizar la rapidez de revisión.

El usuario debería poder entrar y entender inmediatamente:

- Cuántas ofertas nuevas hay.
- Cuáles tienen mayor coincidencia.
- Qué puestos son.
- Dónde están.
- Qué salario ofrecen.
- Cuáles debería revisar.

Ejemplo conceptual:

```text
┌───────────────────────────────────────────────┐
│ AI JOB HUNTER                                 │
│                                               │
│ Nuevas: 5       Coincidencia mínima: 80 %     │
│ Última búsqueda: hace 12 minutos              │
│ Próxima búsqueda: en 48 minutos               │
│                                               │
│ [ FILTROS ]                                   │
├───────────────────────────────────────────────┤
│                                               │
│ 94 %  OPERARIO DE PRODUCCIÓN                  │
│       Empresa X · Castellón                   │
│       32.000 € · Turnos                       │
│                                               │
│       Puesto industrial de producción...      │
│                                               │
│       [ APLICAR ]                             │
│                                               │
├───────────────────────────────────────────────┤
│                                               │
│ 88 %  MOZO DE ALMACÉN                        │
│       Empresa Y · Oropesa                    │
│       28.000 € · Mañana                       │
│                                               │
│       [ APLICAR ]                             │
│                                               │
└───────────────────────────────────────────────┘
```

---

# 19. Ordenación

Las ofertas se ordenarán inicialmente por:

1. Puntuación de coincidencia.
2. Novedad.
3. Fecha de publicación.

La lógica podrá modificarse posteriormente.

---

# 20. Estados de las ofertas

Cada oferta podrá tener diferentes estados internos.

Ejemplo:

```text
NUEVA
ANALIZADA
RELEVANTE
DESCARTADA
VISTA
APLICADA
CERRADA
EXPIRADA
```

El usuario podrá marcar manualmente determinadas ofertas como vistas o descartadas.

---

# 21. Arquitectura conceptual

El PMV deberá separar claramente la adquisición de datos, el procesamiento y la interfaz.

```text
                  ┌─────────────────┐
                  │ PERFIL USUARIO  │
                  └────────┬────────┘
                           │
                           ▼
                  ┌─────────────────┐
                  │ PREFERENCIAS    │
                  └────────┬────────┘
                           │
                           ▼
                    ┌──────────────┐
                    │   INFOJOBS   │
                    └──────┬───────┘
                           │
                           ▼
                  ┌─────────────────┐
                  │ RECOPILADOR     │
                  │ DE OFERTAS      │
                  └────────┬────────┘
                           │
                           ▼
                  ┌─────────────────┐
                  │ BASE DE DATOS   │
                  │ + HISTORIAL     │
                  └────────┬────────┘
                           │
                           ▼
                  ┌─────────────────┐
                  │ DEDUPLICACIÓN   │
                  └────────┬────────┘
                           │
                           ▼
                  ┌─────────────────┐
                  │ MOTOR DE        │
                  │ MATCHING / IA   │
                  └────────┬────────┘
                           │
                           ▼
                  ┌─────────────────┐
                  │ FILTRO          │
                  └────────┬────────┘
                           │
                           ▼
                  ┌─────────────────┐
                  │ INTERFAZ        │
                  └────────┬────────┘
                           │
                           ▼
                      [APLICAR]
```

---

# 22. Configuración del sistema

Las variables importantes deberán ser configurables.

Como mínimo:

```text
scan_interval_minutes
minimum_match_score
maximum_distance_km
minimum_salary
preferred_contracts
preferred_shifts
preferred_job_titles
excluded_job_titles
preferred_sectors
excluded_sectors
```

Esto permitirá modificar el comportamiento del sistema sin modificar el código fuente.

---

# 23. Seguridad y privacidad

El sistema almacenará información profesional y personal del usuario.

El PMV deberá:

- Evitar almacenar información innecesaria.
- Proteger la base de datos.
- No exponer el perfil públicamente.
- Separar credenciales de configuración.
- Utilizar variables de entorno para secretos y claves API.
- Evitar almacenar contraseñas de portales de empleo.

La autenticación de cuentas de terceros no formará parte del PMV.

---

# 24. Limitaciones del PMV

La primera versión estará deliberadamente limitada.

No incluirá inicialmente:

- LinkedIn
- Indeed
- Adecco
- Eurofirms
- Aplicación automática a ofertas
- Generación automática de CV
- Cartas de presentación automáticas
- Respuestas automáticas a formularios
- Gestión automática de entrevistas
- Predicción de probabilidad de contratación

Estas funcionalidades podrán incorporarse en versiones posteriores.

---

# 25. Evolución prevista

### V1 — PMV

```text
InfoJobs
   ↓
Recopilación
   ↓
Base de datos
   ↓
IA + Matching
   ↓
Filtros
   ↓
Interfaz
   ↓
APLICAR
```

### V2

Añadir otros portales:

```text
InfoJobs
LinkedIn
Indeed
Adecco
Eurofirms
       ↓
Motor común de análisis
```

### V3

Añadir gestión de candidatura:

```text
Oferta
 ↓
CV adaptado
 ↓
Respuestas preparadas
 ↓
Revisión del usuario
 ↓
Aplicación
```

### V4

Añadir seguimiento:

```text
Candidatura
 ↓
Seguimiento
 ↓
Entrevista
 ↓
Resultado
```

### V5

Convertir el sistema en un agente de búsqueda de empleo capaz de optimizar progresivamente la estrategia de búsqueda a partir de los resultados obtenidos.

---

# 26. Criterio de éxito del PMV

El PMV será considerado funcional cuando pueda realizar de forma fiable el siguiente ciclo:

```text
1. Consultar InfoJobs
2. Obtener ofertas
3. Guardarlas en la base de datos
4. Identificar cuáles son nuevas
5. Analizarlas
6. Calcular su coincidencia
7. Aplicar las preferencias
8. Mostrar únicamente las relevantes
9. Mostrar un resumen
10. Permitir acceder a la oferta mediante APLICAR
11. Repetir el proceso automáticamente según el intervalo configurado
```

El resultado final deberá permitir al usuario sustituir una revisión manual continua de InfoJobs por un sistema que **vigila el portal, procesa las ofertas y presenta únicamente las oportunidades relevantes**.