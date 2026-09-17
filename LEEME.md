# INMEDIC — Prototipo navegable (módulo 01 · Registro)

Las pantallas del prototipo programadas como páginas web, para revisarlas en el navegador
sin abrir Figma. Cada pantalla tiene su propia dirección, así que se puede mandar el enlace
de una sola: *"checa la 1.4.04"*.

## El link para mostrarlo al cliente

**https://claude.ai/artifact/M5bLJSNi5Jw8ArzNMLfqMU**

Es la version de un solo archivo, ya publicada. **Nace privada**: para que Jairo la pueda
abrir hay que compartirla desde el menu Share de esa misma pagina. Mientras no se comparta,
solo la ve Fernando.

Para actualizarla despues de cambiar pantallas:

```bash
python construir-una-sola-pagina.py
```

y se vuelve a publicar ese `inmedic-prototipo.html` sobre el mismo link.

## Dos versiones del mismo prototipo

| | Para que sirve |
|---|---|
| `index.html` + `01-registro/` | **Para trabajar.** Una pantalla por archivo, facil de editar y de pasarle al programador. |
| `inmedic-prototipo.html` | **Para compartir.** Todo en un solo archivo, navegacion por ancla (`#1.4.05`). Se genera con el script, no se edita a mano. |

La version de un solo archivo se arma leyendo las 12 pantallas sueltas, asi que la fuente de
verdad siempre son los archivos de `01-registro/`.

## Cómo abrirlo

**La forma fácil:** doble clic en `index.html`. No necesita servidor ni internet
(salvo para la tipografía Montserrat, que se carga de Google Fonts).

**Con servidor local**, si prefieres:

```bash
python -m http.server 8031 --directory jairo-inmedic/prototipo-web
```

Y abres `http://localhost:8031`.

## Qué trae

| Código | Pantalla |
|---|---|
| 1.1.01 | Log in |
| 1.1.02 | Restablecer contraseña |
| 1.2.01 | Paso 2 · Datos fiscales — Persona Moral |
| 1.2.02 | Paso 2 · Datos fiscales — Persona Física |
| 1.3.01 | Paso 3 · Registro de Cede |
| 1.4.01 | Paso 4 · Sucursales — aún no hay ninguna |
| 1.4.02 | Paso 4 · Sucursales — agregar otra |
| 1.4.03 | Paso 4 · Sucursales — editar una |
| 1.4.04 | Paso 4 · Sucursales — falta un campo |
| 1.4.05 | Paso 4 · Modal "¿Terminar?" |
| 1.4.06 | Paso 4 · Modal "¿Cancelar?" |
| 1.5.01 | Paso 5 · Finalización — **pantalla nueva, no existía en Figma** |

## Cómo se recorre

- **Los botones de las pantallas están conectados.** "Iniciar Sesión", "Continuar",
  "Editar", "Terminar" y las pestañas Persona Moral / Persona Física llevan a donde deben.
- **La barra negra de arriba** es del prototipo, no del producto. Muestra el código,
  el nombre y en cuál vas, y tiene Anterior / Siguiente / Índice.
- **Las flechas ← y → del teclado** avanzan y retroceden. Sirve para ir rápido en una junta.
- Al pie de cada pantalla hay una nota amarilla con lo que falta decidir en esa pantalla.

## Cómo está armado

```
prototipo-web/
  index.html              Índice: lista de pantallas y puntos a decidir
  assets/
    estilos.css           Todos los estilos. Los colores y tipografías salieron
                          del propio archivo de Figma.
    app.js                La lista de pantallas y la barra de revisión
  01-registro/            Una pantalla, un archivo
```

Es HTML y CSS planos, sin frameworks ni dependencias. La idea es que el programador
de Jairo pueda tomar estas pantallas como referencia directa, o de plano reusar el CSS.

### Los colores y tipografías no son inventados

Se sacaron del archivo de Figma `INMEDIC v2 (copia)` leyendo los rellenos y estilos
de texto de las pantallas reales:

| Token | Valor | Dónde se usa |
|---|---|---|
| `--amarillo` | `#fdc034` | Botón principal, paso actual, acentos |
| `--teal` / `--teal-900` | `#04404d` / `#001c26` | Fondos oscuros, barra de revisión |
| `--verde` | `#1ba69c` | Pasos ya completados, confirmaciones |
| `--rojo` | `#fa5252` | Errores de validación |
| Grises | `#f8f9fa` `#adb5bd` `#495057` | Fondos, bordes, texto |
| Tipografía | Montserrat 400/500/600/700 | Todo |

## Publicarlo para que Jairo lo vea en línea

⚠️ **Esta carpeta está dentro de OneDrive y OneDrive rompe los repos de git.**
Para subirlo a GitHub Pages, cópiala primero fuera de OneDrive:

```bash
cp -r "C:/Users/makin/OneDrive/Documentos/Vonoa web/jairo-inmedic/prototipo-web" "C:/Users/makin/inmedic-prototipo"
```

Y desde ahí inicializas el repo y lo publicas.

## Lo que falta

Los módulos 02 a 08. Se van programando conforme se vayan cerrando en la revisión
con Jairo, para no programar dos veces lo mismo.
