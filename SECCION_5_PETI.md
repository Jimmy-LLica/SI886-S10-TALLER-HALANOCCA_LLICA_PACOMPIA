# 5 Arquitectura empresarial

## 5.1 Principios de arquitectura

Ver AR01_principios.md: P01 a P06, sujetos a aprobación.

## 5.2 Arquitectura actual

Negocio: seis procesos de la ficha; aplicación: ERP, móvil, OSE, portal y tres hojas operativas; tecnología: servidor propio en Tacna, nube del proveedor, hosting compartido, 70 estaciones, 24 móviles y enlace de Ilo sin respaldo. La cooperación proceso-aplicación y las entidades están detalladas en el informe y AR02_entidades.csv. Cuatro de seis entidades carecen de fuente confiable verificada y tres de seis de dueño documentado.

## 5.3 Arquitectura objetivo

Separar aprobación y registro, conciliar y gobernar inventario y maestros, controlar el almacén transaccionalmente, integrar portal y móvil, segmentar red y probar restauraciones. Se deriva del objetivo TI de la ficha y de los hallazgos del inventario. La visión y las capacidades de las secciones 2.2 y 3.1.5 quedan por contrastar.

## 5.4 Análisis de brechas

AR03_brechas.csv contiene catorce brechas. PT1 gobierna perfiles y datos; PT2 concilia almacén; PT3 integra canales; PT4 asegura continuidad; PT5 entrega indicadores. Orden: PT1→PT2→PT3→PT5, con PT4 paralelo después de PT1. Son insumos para el portafolio de la sección 7.1, no proyectos aprobados.
