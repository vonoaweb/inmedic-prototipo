/* ===========================================================
   INMEDIC — Prototipo web
   Barra de revisión: muestra el código de la pantalla y permite
   avanzar y retroceder por el flujo con los botones o con las
   flechas del teclado.
   =========================================================== */

const PANTALLAS = [
  { cod: '1.1.01', nom: 'Log in',                                      url: '01-registro/1.1.01-log-in.html' },
  { cod: '1.1.02', nom: 'Restablecer contraseña',                      url: '01-registro/1.1.02-restablecer-contrasena.html' },
  { cod: '1.2.01', nom: 'Paso 2 · Datos fiscales — Persona Moral',     url: '01-registro/1.2.01-datos-fiscales-moral.html' },
  { cod: '1.2.02', nom: 'Paso 2 · Datos fiscales — Persona Física',    url: '01-registro/1.2.02-datos-fiscales-fisica.html' },
  { cod: '1.3.01', nom: 'Paso 3 · Registro de Cede (sede principal)',  url: '01-registro/1.3.01-registro-de-cede.html' },
  { cod: '1.4.01', nom: 'Paso 4 · Sucursales — aún no hay ninguna',    url: '01-registro/1.4.01-sucursales-vacio.html' },
  { cod: '1.4.02', nom: 'Paso 4 · Sucursales — agregar otra',          url: '01-registro/1.4.02-sucursales-agregar.html' },
  { cod: '1.4.03', nom: 'Paso 4 · Sucursales — editar una',            url: '01-registro/1.4.03-sucursales-editar.html' },
  { cod: '1.4.04', nom: 'Paso 4 · Sucursales — falta un campo',        url: '01-registro/1.4.04-sucursales-error.html' },
  { cod: '1.4.05', nom: 'Paso 4 · Modal "¿Terminar?"',                 url: '01-registro/1.4.05-modal-terminar.html' },
  { cod: '1.4.06', nom: 'Paso 4 · Modal "¿Cancelar?"',                 url: '01-registro/1.4.06-modal-cancelar.html' },
  { cod: '1.5.01', nom: 'Paso 5 · Finalización',                       url: '01-registro/1.5.01-finalizacion.html', nueva: true }
];

function pintarBarra() {
  const host = document.getElementById('barra');
  if (!host) return;

  const cod = document.body.dataset.codigo;
  const i = PANTALLAS.findIndex(p => p.cod === cod);
  if (i === -1) return;

  const actual = PANTALLAS[i];
  const previa = PANTALLAS[i - 1];
  const sig    = PANTALLAS[i + 1];
  const raiz   = '../';

  const href = p => raiz + p.url.replace('01-registro/', '01-registro/');

  host.className = 'barra';
  host.innerHTML = `
    <a class="barra__marca" href="${raiz}index.html">INMEDIC · prototipo</a>
    <span class="barra__codigo">${actual.cod}</span>
    <span class="barra__titulo">${actual.nom}</span>
    <span class="barra__paso">${i + 1} de ${PANTALLAS.length}</span>
    <nav class="barra__nav">
      <a class="barra__btn" ${previa ? `href="${href(previa)}"` : 'aria-disabled="true"'}>← Anterior</a>
      <a class="barra__btn" ${sig ? `href="${href(sig)}"` : 'aria-disabled="true"'}>Siguiente →</a>
      <a class="barra__btn" href="${raiz}index.html">Índice</a>
    </nav>
  `;

  document.addEventListener('keydown', e => {
    if (e.target.matches('input, select, textarea')) return;
    if (e.key === 'ArrowLeft'  && previa) location.href = href(previa);
    if (e.key === 'ArrowRight' && sig)    location.href = href(sig);
  });
}

function pintarIndice() {
  const host = document.getElementById('lista-registro');
  if (!host) return;
  host.innerHTML = PANTALLAS.map(p => `
    <a href="${p.url}" class="${p.nueva ? 'es-pendiente' : ''}">
      <span class="cod">${p.cod}</span>
      <span class="nom">${p.nom}${p.nueva ? ' · pantalla nueva, no existía' : ''}</span>
      <span class="flecha">→</span>
    </a>
  `).join('');
}

document.addEventListener('DOMContentLoaded', () => {
  pintarBarra();
  pintarIndice();

  // Los campos del prototipo no guardan nada: evitamos que un Enter
  // recargue la página y se pierda el recorrido.
  document.querySelectorAll('form').forEach(f => f.addEventListener('submit', e => e.preventDefault()));
});
