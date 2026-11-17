# AI Job Hunter — Lista de tareas del proyecto

> Lista maestra de implementación del PMV. Marca una tarea como completada únicamente cuando esté implementada y probada satisfactoriamente.

## 0. Preparación del proyecto

- [x] Crear repositorio de GitHub
- [x] Crear estructura inicial del proyecto
- [x] Definir especificación del PMV
- [x] Establecer documentación del proyecto en español
- [ ] Definir estrategia técnica definitiva
- [ ] Definir stack tecnológico
- [ ] Configurar entorno de desarrollo local
- [ ] Configurar ejecución del proyecto
- [ ] Configurar sistema de logs
- [ ] Definir estrategia de tests

## 1. Configuración de la aplicación

- [ ] Crear sistema centralizado de configuración
- [ ] Configurar `SCAN_INTERVAL_MINUTES`
- [ ] Configurar `MINIMUM_MATCH_SCORE`
- [ ] Configurar `MAXIMUM_DISTANCE_KM`
- [ ] Configurar `MINIMUM_SALARY`
- [ ] Configurar puestos preferidos
- [ ] Configurar puestos excluidos
- [ ] Configurar sectores preferidos
- [ ] Configurar sectores excluidos
- [ ] Configurar contratos preferidos
- [ ] Configurar horarios preferidos
- [ ] Validar correctamente los valores de configuración
- [ ] Documentar todas las variables configurables

## 2. Base de datos

### Diseño

- [ ] Diseñar modelo de datos
- [ ] Diseñar tabla de perfil profesional
- [ ] Diseñar tabla de formación
- [ ] Diseñar tabla de experiencia profesional
- [ ] Diseñar tabla de carnets y acreditaciones
- [ ] Diseñar tabla de competencias
- [ ] Diseñar tabla de idiomas
- [ ] Diseñar tabla de software
- [ ] Diseñar tabla de preferencias laborales
- [ ] Diseñar tabla de ofertas
- [ ] Diseñar tabla de historial de ofertas
- [ ] Diseñar tabla de ejecuciones de búsqueda
- [ ] Diseñar relaciones entre tablas
- [ ] Definir identificadores y restricciones únicas

### Implementación

- [ ] Configurar conexión con la base de datos
- [ ] Crear modelos ORM
- [ ] Crear tablas mediante migraciones
- [ ] Implementar operaciones CRUD
- [ ] Implementar índices necesarios
- [ ] Probar inserción y lectura de datos
- [ ] Probar actualización de datos
- [ ] Probar eliminación cuando corresponda
- [ ] Probar integridad y restricciones
- [ ] Evitar duplicados

## 3. Perfil profesional

- [ ] Crear modelo de perfil profesional
- [ ] Implementar nombre y apellidos
- [ ] Implementar localización
- [ ] Implementar código postal
- [ ] Implementar radio máximo
- [ ] Implementar disponibilidad laboral
- [ ] Implementar formación
- [ ] Implementar cursos y certificaciones
- [ ] Implementar experiencia profesional
- [ ] Implementar funciones realizadas
- [ ] Implementar herramientas utilizadas
- [ ] Implementar competencias adquiridas
- [ ] Implementar carnets y acreditaciones
- [ ] Implementar tipos de carretilla
- [ ] Implementar competencias técnicas
- [ ] Implementar idiomas y niveles
- [ ] Implementar software y niveles
- [ ] Crear interfaz para editar el perfil
- [ ] Validar y guardar el perfil correctamente
- [ ] Comprobar que el perfil persiste después de reiniciar la aplicación

## 4. Preferencias laborales

- [ ] Crear interfaz de preferencias
- [ ] Configurar provincia
- [ ] Configurar ciudad
- [ ] Configurar código postal
- [ ] Configurar radio máximo
- [ ] Configurar salario mínimo
- [ ] Configurar salario deseado
- [ ] Configurar jornada
- [ ] Configurar horarios
- [ ] Configurar turnos
- [ ] Configurar tipos de contrato
- [ ] Configurar puestos deseados
- [ ] Configurar puestos excluidos
- [ ] Configurar sectores preferidos
- [ ] Configurar sectores excluidos
- [ ] Guardar preferencias en la base de datos
- [ ] Recuperar preferencias al iniciar la aplicación

## 5. Integración con InfoJobs

### Arquitectura del recopilador

- [ ] Definir interfaz común para recopiladores de portales
- [ ] Crear módulo independiente de InfoJobs
- [ ] Separar recopilación, normalización y persistencia
- [ ] Preparar arquitectura para futuros portales
- [ ] Documentar limitaciones y método de acceso utilizado

### Recopilación

- [ ] Implementar búsqueda/recopilación de ofertas de InfoJobs
- [ ] Obtener identificador de oferta
- [ ] Obtener URL
- [ ] Obtener empresa
- [ ] Obtener puesto
- [ ] Obtener localización
- [ ] Obtener salario
- [ ] Obtener contrato
- [ ] Obtener jornada
- [ ] Obtener horario
- [ ] Obtener descripción
- [ ] Obtener requisitos
- [ ] Obtener experiencia requerida
- [ ] Obtener formación requerida
- [ ] Obtener competencias requeridas
- [ ] Obtener fecha de publicación
- [ ] Normalizar los datos obtenidos
- [ ] Gestionar campos ausentes
- [ ] Gestionar errores de recopilación
- [ ] Implementar control de rate limits y errores
- [ ] Verificar que el método de acceso respeta las condiciones y controles de InfoJobs

## 6. Persistencia y deduplicación de ofertas

- [ ] Guardar ofertas nuevas
- [ ] Identificar ofertas mediante ID de InfoJobs
- [ ] Crear mecanismo alternativo de identificación cuando sea necesario
- [ ] Detectar ofertas ya conocidas
- [ ] Detectar ofertas nuevas
- [ ] Detectar ofertas actualizadas
- [ ] Registrar fecha de detección
- [ ] Registrar fecha de última actualización
- [ ] Conservar historial de cambios relevantes
- [ ] Evitar volver a insertar una misma oferta
- [ ] Evitar volver a analizar ofertas sin cambios

## 7. Historial de búsquedas

- [ ] Registrar fecha y hora de cada búsqueda
- [ ] Registrar duración
- [ ] Registrar número de ofertas encontradas
- [ ] Registrar número de ofertas nuevas
- [ ] Registrar número de ofertas actualizadas
- [ ] Registrar número de ofertas analizadas
- [ ] Registrar número de ofertas por encima del umbral
- [ ] Registrar estado de ejecución
- [ ] Registrar errores
- [ ] Crear consulta del historial
- [ ] Mostrar historial de búsquedas en la interfaz

## 8. Motor de matching

- [ ] Diseñar estructura del motor de coincidencia
- [ ] Definir factores iniciales de coincidencia
- [ ] Definir pesos iniciales
- [ ] Definir penalizaciones
- [ ] Implementar puntuación de 0 a 100
- [ ] Comparar localización
- [ ] Comparar salario
- [ ] Comparar jornada
- [ ] Comparar horario
- [ ] Comparar contrato
- [ ] Comparar puesto
- [ ] Comparar sector
- [ ] Comparar experiencia
- [ ] Comparar formación
- [ ] Comparar competencias
- [ ] Comparar carnets y acreditaciones
- [ ] Comparar idiomas cuando corresponda
- [ ] Generar explicación de la puntuación
- [ ] Permitir modificar factores sin rehacer la aplicación
- [ ] Probar el scoring con ofertas reales
- [ ] Ajustar pesos después de las pruebas

## 9. Filtro de relevancia

- [ ] Implementar umbral mínimo de coincidencia
- [ ] Hacer configurable el umbral
- [ ] Aplicar preferencias de localización
- [ ] Aplicar preferencias salariales
- [ ] Aplicar preferencias de jornada
- [ ] Aplicar preferencias de horario
- [ ] Aplicar preferencias de contrato
- [ ] Aplicar puestos preferidos
- [ ] Aplicar puestos excluidos
- [ ] Aplicar sectores preferidos
- [ ] Aplicar sectores excluidos
- [ ] Verificar que las ofertas descartadas no aparecen en la vista principal

## 10. Resumen de ofertas

- [ ] Crear generador de resumen breve
- [ ] Mostrar puesto
- [ ] Mostrar empresa
- [ ] Mostrar localización
- [ ] Mostrar salario cuando esté disponible
- [ ] Mostrar horario
- [ ] Mostrar puntuación
- [ ] Mostrar motivos principales de coincidencia
- [ ] Mantener el resumen fácil de revisar rápidamente
- [ ] Probar resúmenes con diferentes tipos de ofertas

## 11. Botón APLICAR

- [ ] Mostrar botón APLICAR en cada oferta relevante
- [ ] Enlazar con la URL original de InfoJobs
- [ ] Verificar que el enlace corresponde a la oferta correcta
- [ ] Abrir la oferta sin modificar la candidatura
- [ ] Confirmar que el PMV no realiza el envío automático

## 12. Scheduler / actualización automática

- [ ] Implementar scheduler
- [ ] Leer intervalo desde configuración
- [ ] Establecer 60 minutos como valor inicial
- [ ] Permitir 30 minutos
- [ ] Permitir 60 minutos
- [ ] Permitir 120 minutos
- [ ] Permitir 180 minutos
- [ ] Permitir 360 minutos
- [ ] Ejecutar búsquedas automáticamente
- [ ] Registrar cada ejecución
- [ ] Gestionar errores sin detener permanentemente el scheduler
- [ ] Evitar ejecuciones duplicadas
- [ ] Mostrar última búsqueda
- [ ] Mostrar próxima búsqueda

## 13. Interfaz principal

- [ ] Crear interfaz web
- [ ] Mostrar número de ofertas nuevas
- [ ] Mostrar puntuación mínima configurada
- [ ] Mostrar última búsqueda
- [ ] Mostrar próxima búsqueda
- [ ] Mostrar filtros
- [ ] Mostrar ofertas relevantes
- [ ] Ordenar por coincidencia
- [ ] Priorizar ofertas nuevas
- [ ] Incorporar fecha de publicación en la ordenación
- [ ] Mostrar resumen de cada oferta
- [ ] Incorporar botón APLICAR
- [ ] Mostrar estado de cada oferta
- [ ] Permitir marcar ofertas como vistas
- [ ] Permitir marcar ofertas como descartadas
- [ ] Crear vista de historial

## 14. Estados de las ofertas

- [ ] Implementar estado NUEVA
- [ ] Implementar estado ANALIZADA
- [ ] Implementar estado RELEVANTE
- [ ] Implementar estado DESCARTADA
- [ ] Implementar estado VISTA
- [ ] Implementar estado APLICADA
- [ ] Implementar estado CERRADA
- [ ] Implementar estado EXPIRADA
- [ ] Implementar transiciones de estado correctamente

## 15. Seguridad y privacidad

- [ ] Mantener secretos fuera del repositorio
- [ ] Configurar variables de entorno
- [ ] Evitar credenciales en el código
- [ ] No almacenar contraseñas de portales
- [ ] Proteger el perfil profesional
- [ ] Minimizar datos personales almacenados
- [ ] Proteger la base de datos
- [ ] Revisar logs para evitar exposición de datos sensibles
- [ ] Revisar dependencias
- [ ] Documentar medidas de seguridad
- [ ] Verificar que el sistema no intenta saltarse CAPTCHAs, controles de acceso, límites o mecanismos anti-automatización

## 16. Tests

### Unitarios

- [ ] Testear configuración
- [ ] Testear modelos de base de datos
- [ ] Testear deduplicación
- [ ] Testear detección de ofertas nuevas
- [ ] Testear detección de cambios
- [ ] Testear matching
- [ ] Testear filtros
- [ ] Testear estados de ofertas
- [ ] Testear scheduler

### Integración

- [ ] Testear flujo recopilación → normalización
- [ ] Testear flujo normalización → base de datos
- [ ] Testear flujo base de datos → matching
- [ ] Testear flujo matching → filtros
- [ ] Testear flujo completo de una búsqueda
- [ ] Testear repetición de una oferta ya conocida
- [ ] Testear actualización de una oferta existente

### Validación final

- [ ] Ejecutar todos los tests
- [ ] Corregir errores encontrados
- [ ] Confirmar que los tests pasan de forma reproducible

## 17. Observabilidad y errores

- [ ] Implementar logging estructurado
- [ ] Registrar inicio y fin de cada búsqueda
- [ ] Registrar errores del recopilador
- [ ] Registrar errores de base de datos
- [ ] Registrar errores del matching
- [ ] Registrar errores del scheduler
- [ ] Diferenciar errores recuperables de errores críticos
- [ ] Evitar que un error puntual detenga todo el sistema
- [ ] Crear información suficiente para diagnosticar fallos

## 18. Documentación

- [x] Documentar especificación del PMV
- [ ] Documentar arquitectura
- [ ] Documentar instalación
- [ ] Documentar configuración
- [ ] Documentar estructura del proyecto
- [ ] Documentar base de datos
- [ ] Documentar motor de matching
- [ ] Documentar recopilador de InfoJobs
- [ ] Documentar scheduler
- [ ] Documentar interfaz
- [ ] Documentar tests
- [ ] Documentar solución de problemas
- [ ] Actualizar README con el estado real del proyecto

## 19. Integración completa del PMV

- [ ] Conectar perfil con preferencias
- [ ] Conectar recopilador con base de datos
- [ ] Conectar deduplicación con historial
- [ ] Conectar ofertas con motor de matching
- [ ] Conectar matching con filtros
- [ ] Conectar filtros con interfaz
- [ ] Conectar scheduler con recopilador
- [ ] Conectar interfaz con APLICAR
- [ ] Verificar persistencia completa
- [ ] Verificar recuperación ante errores
- [ ] Verificar que una oferta nueva recorre todo el flujo correctamente

## 20. Prueba final del PMV

- [ ] Ejecutar una búsqueda real
- [ ] Comprobar que se obtienen ofertas
- [ ] Comprobar que se almacenan correctamente
- [ ] Comprobar detección de nuevas ofertas
- [ ] Comprobar deduplicación
- [ ] Comprobar análisis de coincidencia
- [ ] Comprobar puntuaciones
- [ ] Comprobar filtros
- [ ] Comprobar resúmenes
- [ ] Comprobar botón APLICAR
- [ ] Comprobar historial
- [ ] Comprobar ejecución automática
- [ ] Comprobar configuración del intervalo
- [ ] Comprobar que no se reanalizan ofertas sin cambios
- [ ] Comprobar que los errores quedan registrados
- [ ] Ejecutar una prueba completa de extremo a extremo
- [ ] Confirmar que se cumplen todos los criterios de éxito del PMV

## 21. Criterio de finalización

El PMV podrá considerarse terminado cuando se pueda ejecutar de forma fiable:

**InfoJobs → recopilación → normalización → base de datos → detección de nuevas/actualizadas → matching → filtros → interfaz → APLICAR → nueva búsqueda automática.**

Todas las tareas críticas de las secciones anteriores deberán estar completadas y verificadas.
