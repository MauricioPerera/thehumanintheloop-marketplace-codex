#!/usr/bin/env python3
"""Instrumentos que miden las tres tecnicas contractables del SemVer 2.0.0.

Familia nueva sobre un artefacto distinto al de stripe/entorno: no es HTTP ni
el entorno de ejecucion, es el **string de version** que un proyecto publica.
El SemVer 2.0.0 nombra 11 reglas; de esas, tres miden una propiedad del codigo
que se puede exigir como invariante: el formato `X.Y.Z` (articulo 2), los
identificadores de pre-release (articulo 9) y los de build metadata (articulo
10). Las otras ocho (major cero, inmutabilidad, precedence, etc.) son juicios
de proceso, politica o conocimiento, y por eso quedan en pilas B/C sin
instrumento (ver scripts/knowledge.json).

Las tres reglas miden la prosa exacta de cada articulo:

    formato     El "normal version" es X.Y.Z, con enteros no negativos y sin
                ceros iniciales (articulo 2). Un sufijo de pre-release o de
                build valido NO es una violacion de esta regla en particular
                -el articulo 2 describe el prefijo, los articulos 9 y 10
                describen los sufijos por separado, y por eso hay una regla
                para cada uno-.
    prerelease  Si hay un sufijo `-...`, sus identificadores son no vacios, de
                solo [0-9A-Za-z-], y los numericos sin cero inicial (articulo
                9). Un `-` sin nada detras es un identificador vacio: invalido.
    build       Si hay un sufijo `+...`, sus identificadores son no vacios y de
                solo [0-9A-Za-z-] (articulo 10). A diferencia de pre-release,
                los identificadores numericos de build SI pueden llevar ceros
                iniciales. Un `+` sin nada detras es invalido por el mismo
                motivo que en pre-release.

Las tres reglas comparten un unico parseo de la forma general del SemVer
(`_SEMVER_SHAPE`), asi que un mismo `__version__` se interpreta una sola vez y
cada regla solo mira la parte que le corresponde a su articulo.

**Lo que estas reglas no pueden ver, dicho de entrada.** No hay un parser de
versiones que ejecute nada: se lee el codigo Python via `ast`, y opcionalmente
`pyproject.toml` via `tomllib` (stdlib desde Python 3.11; sin esta libreria el
instrumento devuelve NO-VERIFICABLE para ese archivo en vez de adivinar). Solo
se inspeccionan literales de string -en Python, asignados a `__version__`; en
`pyproject.toml`, la clave `[project].version`-. Una version armada por
concatenacion, f-string, o resuelta dinamicamente (`dynamic = ["version"]` en
pyproject.toml) no la ve nadie: no es un literal, y eso no es un defecto del
instrumento, es el limite de leer el dato en vez de ejecutar el proyecto.

**Que archivo se mide.** Si se pasa un archivo puntual como objetivo (el caso
tipico al usar este skill), se lee *solo ese archivo* -nunca se escanea el
resto del directorio buscando otras declaraciones-. Para auditar un proyecto
entero (varios archivos, cada uno con su propia `__version__`) hay que pedirlo
explicitamente con `--proyecto`.

Exit codes (convencion KDD):
  0  la propiedad se cumple
  1  no se cumple
  2  no se pudo verificar (falta el dato, o no hay que medir)

Uso:
    python semver_checks.py --rule formato <entrada.py o pyproject.toml>
    python semver_checks.py --rule prerelease <entrada.py o pyproject.toml>
    python semver_checks.py --rule build <entrada.py o pyproject.toml>
    python semver_checks.py --rule formato --proyecto <directorio>
    python semver_checks.py --list
"""

__all__ = [
    'NoVerificable',
    'check_formato',
    'check_prerelease',
    'check_build',
    'main',
]

import argparse
import ast
import os
import re
import sys

try:
    import tomllib
except ImportError:
    tomllib = None

# Sobre que mide esta familia: un archivo puntual, o el proyecto entero con
# --proyecto (todo .py y pyproject.toml que no sea prueba).
ARTEFACTO = 'proyecto'

# Un componente numerico sin cero inicial: "0" o "[1-9][0-9]*".
_NUMERO = r'(?:0|[1-9][0-9]*)'
# Un identificador de pre-release o build: ASCII alfanumerico y guion, no vacio.
_IDENT = re.compile(r'\A[0-9A-Za-z-]+\Z')

# La forma general de un SemVer 2.0.0: normal-version ("-" pre-release)?
# ("+" build)? Un solo parseo para las tres reglas -cada una lee solo el
# grupo que le corresponde a su articulo-.
#   - `pre` es None si no hay sufijo "-...", y "" si el sufijo esta vacio
#     ("1.2.3-" sin nada detras: invalido, lo detecta `check_prerelease`).
#   - `build` es el mismo caso para el sufijo "+...".
_SEMVER_SHAPE = re.compile(
    r'\A(?P<major>' + _NUMERO + r')\.(?P<minor>' + _NUMERO + r')\.(?P<patch>' + _NUMERO + r')'
    r'(?:-(?P<pre>[^+]*))?'
    r'(?:\+(?P<build>.*))?\Z'
)


class NoVerificable(Exception):
    """Falta el dato sin el cual la regla no se puede evaluar (exit 2)."""


def _cero_inicial(ident):
    """Si `ident` es un identificador numerico con cero inicial (no "0")."""
    return ident.isdigit() and not re.fullmatch(_NUMERO, ident)


# ---------------------------------------------------------------------------
# Lectura de fuentes: un archivo puntual, o un proyecto entero.
# ---------------------------------------------------------------------------

def _literales_asignados(arbol):
    """(linea, nombre, valor) de cada asignacion de un string literal a un nombre.

    Reconoce tanto asignaciones simples (`__version__ = "1.2.3"`) como anotadas
    (`__version__: str = "1.2.3"`), igual que `entorno_checks`.
    """
    out = []
    for nodo in ast.walk(arbol):
        if not isinstance(nodo, (ast.Assign, ast.AnnAssign)):
            continue
        valor = nodo.value
        if not isinstance(valor, ast.Constant) or not isinstance(valor.value, str):
            continue
        objetivos = nodo.targets if isinstance(nodo, ast.Assign) else [nodo.target]
        for objetivo in objetivos:
            if isinstance(objetivo, ast.Name):
                out.append((nodo.lineno, objetivo.id, valor.value))
            elif isinstance(objetivo, ast.Attribute):
                out.append((nodo.lineno, objetivo.attr, valor.value))
    return out


def _version_de_python(ruta):
    """[(ruta, linea, valor)] de cada __version__ literal en un archivo .py."""
    try:
        with open(ruta, 'r', encoding='utf-8') as fh:
            texto = fh.read()
        arbol = ast.parse(texto)
    except (OSError, SyntaxError, UnicodeDecodeError) as exc:
        raise NoVerificable('no se pudo leer {}: {}'.format(ruta, exc))
    return [(ruta, linea, valor) for linea, nombre, valor in _literales_asignados(arbol)
            if nombre == '__version__']


def _version_de_pyproject(ruta):
    """[(ruta, 1, valor)] si pyproject.toml declara `[project].version` estatico.

    `tomllib` no conserva numero de linea, asi que se reporta como linea 1 -es
    la unica aproximacion posible sin escribir un parser de TOML propio, y se
    declara aca para que el numero de linea no se lea como mas preciso de lo
    que es.
    """
    if tomllib is None:
        raise NoVerificable(
            'tomllib no esta disponible (hace falta Python 3.11+) para leer {}'
            .format(ruta))
    try:
        with open(ruta, 'rb') as fh:
            datos = tomllib.load(fh)
    except tomllib.TOMLDecodeError as exc:
        raise NoVerificable('{} no es TOML valido: {}'.format(ruta, exc))
    proyecto = datos.get('project', {})
    if 'version' in proyecto.get('dynamic', []):
        raise NoVerificable(
            '{} declara version dinamica (dynamic = ["version"]): no hay un '
            'literal que leer, la resuelve el backend de build'.format(ruta))
    version = proyecto.get('version')
    if not isinstance(version, str):
        raise NoVerificable(
            '{} no declara [project].version como string'.format(ruta))
    return [(ruta, 1, version)]


def _versiones_de_archivo(ruta):
    """[(ruta, linea, valor)] de un unico archivo objetivo."""
    nombre = os.path.basename(ruta)
    if nombre == 'pyproject.toml':
        return _version_de_pyproject(ruta)
    if nombre.endswith('.py'):
        return _version_de_python(ruta)
    raise NoVerificable(
        '{} no es un archivo .py ni pyproject.toml: no hay que leer'.format(ruta))


def _versiones_de_proyecto(proyecto):
    """[(ruta, linea, valor)] de todo el proyecto: cada .py y cada pyproject.toml.

    Solo se usa con --proyecto explicito. Se excluyen las pruebas a proposito:
    un string de version de mentira en un fixture es exactamente lo que un
    fixture tiene que tener, y marcarlo pondria el instrumento en rojo por
    hacer bien las cosas.
    """
    out = []
    vistos = False
    for raiz, dirs, archivos in os.walk(proyecto):
        dirs[:] = [d for d in dirs if d not in ('__pycache__', '.git', 'tests')]
        for nombre in sorted(archivos):
            if nombre == 'pyproject.toml':
                vistos = True
                try:
                    out.extend(_version_de_pyproject(os.path.join(raiz, nombre)))
                except NoVerificable:
                    continue
            elif nombre.endswith('.py') and not nombre.startswith('test_'):
                vistos = True
                out.extend(_version_de_python(os.path.join(raiz, nombre)))
    if not vistos:
        raise NoVerificable(
            'el proyecto no tiene ningun .py ni pyproject.toml que leer')
    return out


# ---------------------------------------------------------------------------
# Checks. Cada uno recibe la lista unificada [(ruta, linea, valor)] y opts.
# ---------------------------------------------------------------------------

def check_formato(versiones, opts):
    """El "normal version" es X.Y.Z: enteros no negativos, sin ceros iniciales.

    Articulo 2 del SemVer 2.0.0: "A normal version number MUST take the form
    X.Y.Z where X, Y, and Z are non-negative integers, and MUST NOT contain
    leading zeroes." Esta regla mide solo esa forma. Un sufijo de pre-release
    o de build -valido o no- no la hace fallar: eso lo miden `check_prerelease`
    y `check_build`. Lo que si hace fallar esta regla es que el "normal
    version" en si mismo tenga menos o mas de tres componentes, un componente
    no numerico, o un cero inicial.
    """
    out = []
    for archivo, linea, valor in versiones:
        if not _SEMVER_SHAPE.match(valor):
            out.append((archivo, linea,
                        '__version__ = {!r} no tiene la forma normal-version '
                        '["-" pre-release]["+" build] de SemVer 2.0.0, o su '
                        'X.Y.Z no son tres enteros no negativos sin ceros '
                        'iniciales'.format(valor)))
    return out


def check_prerelease(versiones, opts):
    """Si hay sufijo de pre-release, sus identificadores son validos.

    Articulo 9: los identificadores deben ser no vacios, de solo
    [0-9A-Za-z-], e identificadores numericos sin cero inicial. Un `-` sin
    nada detras ("1.2.3-") declara un identificador vacio y es invalido; una
    version SIN el sufijo "-..." no tiene nada que este articulo pida medir,
    y sale verde.
    """
    out = []
    for archivo, linea, valor in versiones:
        m = _SEMVER_SHAPE.match(valor)
        if not m or m.group('pre') is None:
            continue
        pre = m.group('pre')
        if pre == '':
            out.append((archivo, linea,
                        '__version__ = {!r} declara un sufijo de pre-release '
                        'vacio ("-" sin identificadores detras)'.format(valor)))
            continue
        for ident in pre.split('.'):
            if ident == '':
                out.append((archivo, linea,
                            '__version__ = {!r} tiene un identificador de '
                            'pre-release vacio'.format(valor)))
                break
            if not _IDENT.match(ident):
                out.append((archivo, linea,
                            '__version__ = {!r} tiene el identificador de '
                            'pre-release {!r} con caracteres fuera de '
                            '[0-9A-Za-z-]'.format(valor, ident)))
                break
            if _cero_inicial(ident):
                out.append((archivo, linea,
                            '__version__ = {!r} tiene el identificador numerico '
                            'de pre-release {!r} con cero inicial'.format(
                                valor, ident)))
                break
    return out


def check_build(versiones, opts):
    """Si hay sufijo de build metadata, sus identificadores son validos.

    Articulo 10: los identificadores deben ser no vacios y de solo
    [0-9A-Za-z-]. A diferencia del pre-release, los identificadores numericos
    de build SI pueden llevar ceros iniciales (el spec lo permite
    explicitamente). Un `+` sin nada detras ("1.2.3+") declara build metadata
    vacio y es invalido; una version SIN el sufijo "+..." no tiene nada que
    este articulo pida medir, y sale verde.
    """
    out = []
    for archivo, linea, valor in versiones:
        m = _SEMVER_SHAPE.match(valor)
        if not m or m.group('build') is None:
            continue
        build = m.group('build')
        if build == '':
            out.append((archivo, linea,
                        '__version__ = {!r} declara build metadata vacio '
                        '("+" sin identificadores detras)'.format(valor)))
            continue
        for ident in build.split('.'):
            if ident == '' or not _IDENT.match(ident):
                out.append((archivo, linea,
                            '__version__ = {!r} tiene el identificador de '
                            'build {!r} invalido: debe ser no vacio y de solo '
                            '[0-9A-Za-z-]'.format(valor, ident)))
                break
    return out


RULES = {
    'formato': (check_formato,
                'Formato: normal-version X.Y.Z sin ceros iniciales (sufijos aparte)'),
    'prerelease': (check_prerelease,
                   'Pre-release: identificadores no vacios, [0-9A-Za-z-], sin '
                   'ceros iniciales en los numericos'),
    'build': (check_build,
              'Build metadata: identificadores no vacios y de solo [0-9A-Za-z-]'),
}


def main(argv=None):
    """Corre la regla pedida sobre el archivo o proyecto dado y devuelve el exit code."""
    parser = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    parser.add_argument('--rule')
    parser.add_argument('--list', action='store_true')
    parser.add_argument('--proyecto',
                        help='audita todo un directorio en vez de un solo archivo')
    parser.add_argument('target', nargs='?',
                        help='archivo .py o pyproject.toml puntual a leer')
    args = parser.parse_args(argv)

    if args.list:
        for nombre in sorted(RULES):
            print('{:24} {}'.format(nombre, RULES[nombre][1]))
        return 0

    if args.rule not in RULES:
        print('NO-VERIFICABLE: regla desconocida: {!r} (ver --list)'.format(args.rule))
        return 2
    if not args.target and not args.proyecto:
        print('NO-VERIFICABLE: falta el archivo objetivo o --proyecto')
        return 2

    try:
        if args.proyecto:
            versiones = _versiones_de_proyecto(os.path.abspath(args.proyecto))
        else:
            objetivo = os.path.abspath(args.target)
            if not os.path.isfile(objetivo):
                print('NO-VERIFICABLE: no existe el archivo {}'.format(objetivo))
                return 2
            versiones = _versiones_de_archivo(objetivo)
    except NoVerificable as exc:
        print('NO-VERIFICABLE: {}'.format(exc))
        return 2

    if not versiones:
        print('NO-VERIFICABLE: no se encontro ningun __version__ ni '
              '[project].version que medir')
        return 2

    func, etiqueta = RULES[args.rule]
    try:
        violaciones = func(versiones, args)
    except NoVerificable as exc:
        print('NO-VERIFICABLE: {}: {}'.format(etiqueta, exc))
        return 2

    if violaciones:
        print('INSTRUMENTO ROJO: {}'.format(etiqueta))
        for ruta, linea, detalle in violaciones:
            print('  {}:{}: {}'.format(os.path.basename(ruta), linea, detalle))
        return 1

    print('OK: {}'.format(etiqueta))
    return 0


if __name__ == '__main__':
    sys.exit(main())
