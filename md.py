#!/usr/bin/env python3
from textual.app import App, ComposeResult
from textual.widgets import Footer, Header, Markdown
import sys



def path_md(ruta: str):
    if not ruta.endswith('.md'):
        return "# Try a Markdown file"
    else:
        with open(ruta, 'r') as archivo_md:
            contenido = archivo_md.read()
        return contenido


# markdown = prueba

if len(sys.argv) > 1:
    markdown = path_md(sys.argv[1])
    titulo = sys.argv[1]
else:
    titulo = "Enter the second argument"
    markdown = """\
# Enter the second argument

```shell
python md.py [argv]
# or
md.py [argv]
```
"""

class MarkdownExampleApp(App):


    BINDINGS = [("q", "exit", "Quit"),
                ("d", "toggle_dark", "Dark/light")]

    def compose(self) -> ComposeResult:
        yield Header()
        yield Markdown(markdown)
        yield Footer()

    def action_exit(self):
        return self.exit()

    def action_toggle_dark(self) -> None:
        return super().action_toggle_dark()

    def on_mount(self):
        self.title = str(titulo)


if __name__ == "__main__":
    app = MarkdownExampleApp()
    app.run()
