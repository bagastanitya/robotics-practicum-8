import sys
import numpy as np
import yaml
from PIL import Image

pgm = sys.argv[1] if len(sys.argv) > 1 else 'lab_map_slow.pgm'
yml = pgm.replace('.pgm', '.yaml')
with open(yml) as f:
 res = yaml.safe_load(f)['resolution']

img = np.array(Image.open(pgm))
print('ukuran peta (baris x kolom):', img.shape)
occupied = img < 100
unknown = (img > 200) & (img < 210)
print('occupied cells:', occupied.sum())
print('unknown cells:', unknown.sum())
print('unknown (%):', round(100 * unknown.sum() / img.size, 1))

# ukur jarak antar dua dinding pada satu baris (atau kolom)
mode = sys.argv[3] if len(sys.argv) > 3 else 'baris'
if mode == 'kolom':
 n = int(sys.argv[2]) if len(sys.argv) > 2 else img.shape[1] // 2
 line = occupied[:, n]
else:
 n = int(sys.argv[2]) if len(sys.argv) > 2 else img.shape[0] // 2
 line = occupied[n]
idx = np.where(line)[0]
if len(idx) >= 2:
 print(mode, n, '-> jarak antar dinding (m):', (idx.max() - idx.min()) *res)
else:
 print(mode, n, 'tidak memotong dua dinding; coba nomor lain')
