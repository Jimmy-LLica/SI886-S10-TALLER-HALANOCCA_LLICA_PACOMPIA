# SI886 – Taller S10: Arquitectura Empresarial (Caso 6)

Taller del curso SI886 sobre **Distribuidora Andina del Sur**. Documenta el análisis
de arquitectura empresarial de la organización y propone una hoja de ruta de mejora
(sección 5 del PETI).

**Autores:** Halanocca · Llica · Pacompia

## Contenido

| Archivo | Descripción |
|---|---|
| `AR01_principios.md` | Seis principios de arquitectura (dato con dueño, segregación de funciones, integración trazable, hoja operativa visible, seguridad por diseño y continuidad comprobada), cada uno con declaración, razón, implicancias y trazabilidad. |
| `AR02_entidades.csv` | Catálogo de entidades de la organización. |
| `AR03_brechas.csv` | Brechas documentadas, clasificadas por capa y agrupadas en paquetes de trabajo (PT). |
| `AR03_brechas.py` | Script que resume las brechas por capa y lista los paquetes de trabajo con su secuencia de dependencias. |
| `AR03_salida.txt` | Salida generada por el script. |
| `SECCION_5_PETI.md` | Sección 5 del PETI (Plan Estratégico de TI). |

## Ejecución

Requiere Python 3 y `pandas`:

```bash
pip install pandas
python AR03_brechas.py
```

El script imprime el total de brechas, el conteo por capa y los paquetes de trabajo,
con la secuencia PT1 → PT2 → PT3 → PT5 (PT4 inicia tras PT1 y avanza en paralelo con PT2).
