# wpm

Fork de [cslarsen/wpm](https://github.com/cslarsen/wpm) (v1.51.5) para medir la velocidad de escritura en la consola.

## Cambios

- `--spanish`: usa citas en español e ignora los acentos (`á` = `a`, `ü` = `u`); la `ñ` sigue siendo distinta.
- `ignore_accents = true` en la sección `[wpm]` de `~/.wpmrc` activa la misma comparación con cualquier base de citas.

## Instalación

```bash
pip install --user .
wpm --spanish
```
