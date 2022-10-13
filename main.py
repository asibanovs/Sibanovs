import biblioteka
print(biblioteka.versija)
for prece in biblioteka.saraksts:
 print(prece)
print(biblioteka.summa(2, 3))
bmw = biblioteka.Auto()
bmw.braukt()
import biblioteka as bibl
print(bibl.versija)
for prece in bibl.saraksts:
 print(prece)
print(bibl.summa(2, 3))
bmw = bibl.Auto()
bmw.braukt()
from biblioteka import *
print(versija)
for prece in saraksts:
 print(prece)
print(summa(2, 3))
bmw = Auto()
bmw.braukt()
from biblioteka import versija
print(versija)
print(summa(2, 3))