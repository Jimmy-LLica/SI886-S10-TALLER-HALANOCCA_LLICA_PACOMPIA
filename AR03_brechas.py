"""Resume las brechas del caso 6 y deriva paquetes en orden de dependencia.

Uso: python AR03_brechas.py
Requiere: pandas
"""
from pathlib import Path
import sys
import pandas as pd

sys.stdout.reconfigure(encoding='utf-8')

base = Path(__file__).parent
df = pd.read_csv(base / 'AR03_brechas.csv', encoding='utf-8-sig').fillna('')
assert len(df) >= 10
print(f'Brechas documentadas: {len(df)}')
print('\nBrechas por capa:')
print(df.groupby('Capa').size().to_string())
print('\nPaquetes de trabajo:')
for paquete, grupo in df.groupby('Paquete', sort=True):
    print(f'{paquete}: {", ".join(grupo.ID.astype(str))}')
print('\nSecuencia por dependencias: PT1 -> PT2 -> PT3 -> PT5')
print('PT4 inicia después de PT1 y puede avanzar en paralelo con PT2.')
print('Esfuerzo: cualitativo y propuesto; requiere estimación presupuestal posterior.')
