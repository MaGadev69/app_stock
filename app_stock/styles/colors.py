from enum import Enum
class Color(Enum):
    ACCENT = "#d5d8dc"  # este color corresponde a un gris claro
    PRIMARY = "#121113" # este color corresponde a un gris oscuro
    SECONDARY = "#ebeaf814"  # este color corresponde a un gris claro
    
class TextColor(Enum):
    ACCENT = "#EA5940"    # Rojo oscuro, usado para resaltar elementos importantes.
    PRIMARY = "#212529"   # Gris oscuro, usado para texto principal.
    SECONDARY = "#212589" # Gris oscuro, usado para texto secundario.
    TERTIARY = "#D3D3D3" # Gris claro, usado para texto terciario.
    QUATERNARY = "#FFFFFF" # Blanco, usado para texto en fondo oscuro.