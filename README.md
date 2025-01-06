# Overview

This simple library is a `pydantic` + `pydantic-xml` data model for Adobe Audition `.sesx` project files.

It strives to offer full read/write compatibility with the full SESX file format, enabling easier automation and scripting around project files without risking breaking those project files.

## Installation

```bash
pip install pydantic_adobe_audition
```

## Usage

```python
from pathlib import Path
from pydantic_adobe_audition import Sesx

# Read data
sesx_content = Path("to/project.sesx").read_text()
project = Sesx.from_xml(sesx_content)

# Write data
sesx_content = project.to_xml()
Path("to/project.output.sesx").write_text(sesx_content)
```
