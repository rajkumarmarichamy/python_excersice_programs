# creating a file (converts) with functions and importing the same file in current file

import converts
#or
from converts import lbs_to_kg
from converts import kg_to_lbs

print(lbs_to_kg(56))
print(kg_to_lbs(100))

print(converts.lbs_to_kg(100))



