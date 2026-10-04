# Validia

Demo en Tkinter con dos componentes reutilizables: un campo de texto con validación en tiempo real y un generador de *slugs*.

## Características

- **ValidatedEntry**: `tk.Entry` que valida con una expresión regular (`fullmatch`) mientras escribes.
  - Borde y fondo gris/blanco si está vacío, verde si es válido, rojo si es inválido.
  - Propiedad `.valid` para consultar el estado.
- **slug(text)**: convierte texto a formato URL: quita acentos, elimina símbolos, pasa a minúsculas y une palabras con guiones.
  - `"Canción Nueva!"` → `"cancion-nueva"`
- **Demo** con interfaz de tarjetas: validación de correo y slug en vivo.

## Requisitos

- Python 3.8 o superior
- Tkinter (incluido con Python; en Linux: `sudo apt install python3-tk`)

No requiere dependencias externas.

## Estructura

```
.
├── demo.py
└── guiutils/
    ├── __init__.py
    ├── validated_entry.py
    └── slugifier.py
```

## Uso

```bash
python3 demo.py
```

### Usar los componentes en tu propio código

```python
import tkinter as tk
from guiutils.validated_entry import ValidatedEntry
from guiutils.slugifier import slug

root = tk.Tk()

entry = ValidatedEntry(root, pattern=r"^\d{4}$", width=20)  # 4 dígitos
entry.pack(padx=10, pady=10)

print(entry.valid)             # False
print(slug("Hola Mundo ¡Ñandú!"))  # hola-mundo-nandu

root.mainloop()
```

## Parámetros de `ValidatedEntry`

| Parámetro | Descripción |
|-----------|-------------|
| `master` | Widget padre |
| `pattern` | Regex en texto. Si es `None`, todo es válido |
| `**kwargs` | Cualquier opción de `tk.Entry` (`width`, `font`, etc.) |

## Licencia

Libre uso educativo.