import json
import uuid
from pathlib import Path
from typing import Any, Generator, List, OrderedDict

from markitdown import MarkItDown
from pydantic import BaseModel


class GuideReference(BaseModel):
    url: str = ""
    description: str = ""


class GuideSection(BaseModel):
    title: str = ""
    content: str = ""
    visible: bool = True
    img: List[GuideReference] = []
    video: List[GuideReference] = []


class GuideTab(BaseModel):
    title: str = ""
    sort_order: int = 0
    description: str = ""
    visible: bool = True
    sections: List[GuideSection] = []


class Guide(BaseModel):
    created_at: str = ""
    updated_at: str = ""
    data: OrderedDict[str, OrderedDict[str, GuideTab]] = OrderedDict()


def get_temp_file() -> Generator[Any, Any, Path]:
    file = Path(f"/tmp/{uuid.uuid4().hex}.html")
    try:
        yield file
    finally:
        file.unlink(missing_ok=True)


if __name__ == "__main__":
    with Path("I10n/en.json").open() as f:
        json_obj = json.load(f)
    guide = Guide.model_validate(json_obj)
    print(guide.updated_at)
    md = MarkItDown()
    Path("docs").mkdir(exist_ok=True)
    for header, guide_tabs in guide.data.items():
        with Path(f"docs/{header}.md").open("w") as f:
            f.write(f"# {header}\n")
            for tab_sections, tab in guide_tabs.items():
                f.write(f"## {tab.title}\n")
                for section in tab.sections:
                    if section.title:
                        f.write(f"### {section.title}\n")
                    if section.content:
                        file = next(get_temp_file())
                        with file.open("w") as tmp:
                            tmp.write(section.content)
                        result = md.convert(str(file), extension=".html")
                        f.write(f"{result.text_content}\n\n")
