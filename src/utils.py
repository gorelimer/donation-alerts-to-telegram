from pathlib import Path

import jinja2


async def form_render(path: str, **kwargs) -> str:
    text = Path(path).read_text('utf-8')
    template = jinja2.Template(text, trim_blocks=True, lstrip_blocks=True, enable_async=True)
    return await template.render_async(**kwargs)
