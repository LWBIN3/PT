# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 00:26:58 2024

@author: chenb
"""




e = {
    'H': 'Hydrogen',
    'He': 'Helium',
    'Li': 'Lithium',
    'Be': 'Beryllium',
    'B': 'Boron',
    'C': 'Carbon',
    'N': 'Nitrogen',
    'O': 'Oxygen',
    'F': 'Fluorine',
    'Ne': 'Neon',
    'Na': 'Sodium',
    'Mg': 'Magnesium',
    'Al': 'Aluminium',
    'Si': 'Silicon',
    'P': 'Phosphorus',
    'S': 'Sulfur',
    'Cl': 'Chlorine',
    'Ar': 'Argon',
    'K': 'Potassium',
    'Ca': 'Calcium',
    'Sc': 'Scandium',
    'Ti': 'Titanium',
    'V': 'Vanadium',
    'Cr': 'Chromium',
    'Mn': 'Manganese',
    'Fe': 'Iron',
    'Co': 'Cobalt',
    'Ni': 'Nickel',
    'Cu': 'Copper',
    'Zn': 'Zinc',
    'Ga': 'Gallium',
    'Ge': 'Germanium',
    'As': 'Arsenic',
    'Se': 'Selenium',
    'Br': 'Bromine',
    'Kr': 'Krypton',
    'Rb': 'Rubidium',
    'Sr': 'Strontium',
    'Y': 'Yttrium',
    'Zr': 'Zirconium',
    'Nb': 'Niobium',
    'Mo': 'Molybdenum',
    'Tc': 'Technetium',
    'Ru': 'Ruthenium',
    'Rh': 'Rhodium',
    'Pd': 'Palladium',
    'Ag': 'Silver',
    'Cd': 'Cadmium',
    'In': 'Indium',
    'Sn': 'Tin',
    'Sb': 'Antimony',
    'Te': 'Tellurium',
    'I': 'Iodine',
    'Xe': 'Xenon'
}
keys=list(e.keys())
# secondkeys=keys[1]
# secondvalues=e[secondkeys]
# for a in range(0,54):
#     short=keys[a]
#     full=e[short]
#     a=a+1
#     print(f'<button class="mat simple element-alkali-metal" data-element="{short}"><div class="num">{a}</div><div class="mat"><a title="{full}" href="https://zh.wikipedia.org/zh-tw/{full}"><span class="element-symbol">{short}</span></a></div></button>')
# c=1
# r=5
# for a in range(18,54):
#     short=keys[a]
#     a=a+1
#     print(f'.mat.simple[data-element="{short}"] {{ grid-column: {c}; grid-row:{r} ; }}')
#     c=c+1
#     if c==19:
#         c=1
#         r=r+1
     
for a in range(0, 54):
    short = keys[a]
    full = e[short]
    element_number = a + 1
    print(f'''<div class="mat simple element-non-metal" data-element="{short}" data-number="{element_number}" data-name="{full}"> <a title="{full}" href="https://zh.wikipedia.org/zh-tw/{full}"> <div class="num">{element_number}</div> <div class="element-symbol">{short}</div> <div class="element-name">{full}</div> </a> </div>''')
    


    
    