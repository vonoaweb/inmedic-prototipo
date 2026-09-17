# -*- coding: utf-8 -*-
"""
Toma las 12 pantallas sueltas y arma un solo archivo HTML con todo dentro.
Sirve para compartirlo por link: no necesita servidor ni carpetas.

    python construir-una-sola-pagina.py

Genera: inmedic-prototipo.html
"""

import io
import os
import re

AQUI = os.path.dirname(os.path.abspath(__file__))

PANTALLAS = [
    ("1.1.01", "Log in",                                     "1.1.01-log-in.html"),
    ("1.1.02", "Restablecer contraseña",                     "1.1.02-restablecer-contrasena.html"),
    ("1.2.01", "Paso 2 · Datos fiscales — Persona Moral",    "1.2.01-datos-fiscales-moral.html"),
    ("1.2.02", "Paso 2 · Datos fiscales — Persona Física",   "1.2.02-datos-fiscales-fisica.html"),
    ("1.3.01", "Paso 3 · Registro de Cede (sede principal)", "1.3.01-registro-de-cede.html"),
    ("1.4.01", "Paso 4 · Sucursales — aún no hay ninguna",   "1.4.01-sucursales-vacio.html"),
    ("1.4.02", "Paso 4 · Sucursales — agregar otra",         "1.4.02-sucursales-agregar.html"),
    ("1.4.03", "Paso 4 · Sucursales — editar una",           "1.4.03-sucursales-editar.html"),
    ("1.4.04", "Paso 4 · Sucursales — falta un campo",       "1.4.04-sucursales-error.html"),
    ("1.4.05", 'Paso 4 · Modal "¿Terminar?"',                "1.4.05-modal-terminar.html"),
    ("1.4.06", 'Paso 4 · Modal "¿Cancelar?"',                "1.4.06-modal-cancelar.html"),
    ("1.5.01", "Paso 5 · Finalización",                      "1.5.01-finalizacion.html"),
]

ARCHIVO_A_CODIGO = {archivo: cod for cod, _, archivo in PANTALLAS}

DECISIONES = [
    ("1.1.02", "Qué pasa si las dos contraseñas no coinciden, y el mínimo de caracteres"),
    ("1.2.02", "¿El logotipo es obligatorio también para persona física?"),
    ("1.3.01", "¿“Cede” se queda con C o se corrige a “Sede”?"),
    ("1.4.01", "¿Se puede terminar el registro sin ninguna sucursal?"),
    ("1.4.02", "¿La Cede aparece dentro de la tabla de sucursales o aparte?"),
    ("1.4.04", "Cuáles campos son realmente obligatorios"),
    ("1.4.06", "Al cancelar, ¿se pierde también la Cede? ¿A dónde va el usuario?"),
    ("1.5.01", "Pantalla nueva: ¿los tres botones del final están bien?"),
]


def leer(ruta):
    with io.open(ruta, encoding="utf-8") as f:
        return f.read()


def reescribir_enlaces(html):
    """Los enlaces entre archivos se vuelven anclas: 1.2.01-....html -> #1.2.01"""
    for archivo, cod in ARCHIVO_A_CODIGO.items():
        html = html.replace('href="%s"' % archivo, 'href="#%s"' % cod)
        html = html.replace('href="01-registro/%s"' % archivo, 'href="#%s"' % cod)
    html = html.replace('href="../index.html"', 'href="#indice"')
    html = html.replace('href="index.html"', 'href="#indice"')
    return html


def cuerpo_de(archivo):
    """Lo que va entre la barra de revisión y el <script> final."""
    html = leer(os.path.join(AQUI, "01-registro", archivo))
    ini = html.index('<div id="barra"></div>') + len('<div id="barra"></div>')
    fin = html.index("<script")
    return reescribir_enlaces(html[ini:fin].strip())


def construir():
    css = leer(os.path.join(AQUI, "assets", "estilos.css"))

    filas_indice = "\n".join(
        '<a href="#%s"%s><span class="cod">%s</span><span class="nom">%s%s</span><span class="flecha">&rarr;</span></a>'
        % (cod, ' class="es-pendiente"' if cod == "1.5.01" else "", cod, titulo,
           " · pantalla nueva, no existía" if cod == "1.5.01" else "")
        for cod, titulo, _ in PANTALLAS
    )

    filas_decisiones = "\n".join(
        '<a href="#%s"><span class="cod">%s</span><span class="nom">%s</span><span class="flecha">&rarr;</span></a>'
        % (cod, cod, texto)
        for cod, texto in DECISIONES
    )

    secciones = "\n".join(
        '<section class="pantalla" data-codigo="%s">\n%s\n</section>' % (cod, cuerpo_de(archivo))
        for cod, _, archivo in PANTALLAS
    )

    datos_js = ",\n    ".join(
        '{ cod: "%s", nom: %s }' % (cod, '"%s"' % titulo.replace('"', '\\"'))
        for cod, titulo, _ in PANTALLAS
    )

    plantilla = leer(os.path.join(AQUI, "plantilla-una-sola-pagina.html"))
    salida = (plantilla
              .replace("/*CSS*/", css)
              .replace("<!--INDICE-->", filas_indice)
              .replace("<!--DECISIONES-->", filas_decisiones)
              .replace("<!--PANTALLAS-->", secciones)
              .replace("/*DATOS*/", datos_js))

    destino = os.path.join(AQUI, "inmedic-prototipo.html")
    with io.open(destino, "w", encoding="utf-8") as f:
        f.write(salida)
    print("Listo: %s (%.0f KB)" % (destino, os.path.getsize(destino) / 1024.0))


if __name__ == "__main__":
    construir()
