# Principios de arquitectura de Distribuidora Andina del Sur

## P01 Dato con dueño y fuente

**Declaración:** Cada entidad crítica tendrá una fuente autoritativa y un cargo responsable.

**Razón:** Cliente presenta 500 registros de diferencia y stock difiere 4,7 %.

**Implicancias:** Definir dueño, reglas de calidad y conciliación antes de integrar o analizar.

**Trazabilidad:** Inventario actual §5; ficha C y F.

## P02 Segregación de funciones

**Declaración:** Quien registra una compra o pago no podrá aprobarla.

**Razón:** Se detectaron compras fraccionadas bajo S/ 5 000 y un mismo usuario registraba y aprobaba.

**Implicancias:** Rediseñar perfiles, aprobar excepciones y auditar cambios.

**Trazabilidad:** Ficha G y H.

## P03 Integración trazable

**Declaración:** Los intercambios entre aplicaciones tendrán responsable, contrato y registro de errores.

**Razón:** Portal se digita manualmente; fuerza de ventas sincroniza de noche.

**Implicancias:** Sustituir doble digitación y controlar sincronización y reconciliación.

**Trazabilidad:** Inventario actual §4.

## P04 Hoja operativa visible

**Declaración:** Toda hoja que sostenga un proceso se inventariará y gobernará como aplicación.

**Razón:** Ubicaciones, conteos y precios operan en hojas paralelas.

**Implicancias:** Asignar responsable y controles hasta su migración o retiro.

**Trazabilidad:** Inventario actual §2 y §7.

## P05 Seguridad por diseño

**Declaración:** El acceso y tratamiento de datos responderán a su clasificación y necesidad.

**Razón:** Portal sin soporte, red plana, cambios directos y MFA solo en correo.

**Implicancias:** Controlar perfiles, cambios, segmentación y datos personales desde el diseño.

**Trazabilidad:** Ficha F y H; inventario §6.

## P06 Continuidad comprobada

**Declaración:** Toda capacidad crítica tendrá respaldo y restauración probada.

**Razón:** Respaldos solo a disco local, sin prueba integral; Ilo sin enlace de respaldo.

**Implicancias:** Definir pruebas, recuperación y alternativas operativas verificables.

**Trazabilidad:** Ficha F; inventario §6.

Los principios son propuestas del equipo basadas en la ficha y el inventario; requieren aprobación organizacional.
