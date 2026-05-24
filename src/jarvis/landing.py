"""Generate the standalone HTML landing page."""

from pathlib import Path

from jinja2 import Environment, FileSystemLoader, select_autoescape


class LandingWriter:
    def __init__(
        self,
        output_dir: Path,
        templates_dir: Path | None = None,
    ) -> None:
        self.output_dir = output_dir
        self.templates_dir = templates_dir or Path(__file__).parent / "templates" / "landing"

    def write(self) -> None:
        self.output_dir.mkdir(parents=True, exist_ok=True)

        env = Environment(
            loader=FileSystemLoader([str(self.templates_dir), str(self.templates_dir.parent)]),
            autoescape=select_autoescape(["html"]),
        )

        tmpl = env.get_template("index.html.j2")
        html = tmpl.render()
        (self.output_dir / "index.html").write_text(html, encoding="utf-8")
