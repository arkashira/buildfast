import json
from dataclasses import dataclass
from typing import List, Dict

@dataclass
class Template:
    id: int
    name: str
    thumbnail: str
    description: str
    tags: List[str]
    category: str
    schema: Dict

class TemplateMarketplace:
    def __init__(self, templates: List[Template]):
        self.templates = templates

    def get_templates(self, category: str = None) -> List[Template]:
        if category:
            return [t for t in self.templates if t.category == category]
        return self.templates

    def import_template(self, template_id: int) -> Dict:
        for template in self.templates:
            if template.id == template_id:
                return template.schema
        raise ValueError("Template not found")

    def load_templates(self) -> List[Template]:
        # Simulate loading templates from a database or file
        return self.templates

def load_templates_from_json(json_data: str) -> List[Template]:
    data = json.loads(json_data)
    templates = []
    for template_data in data:
        template = Template(
            id=template_data["id"],
            name=template_data["name"],
            thumbnail=template_data["thumbnail"],
            description=template_data["description"],
            tags=template_data["tags"],
            category=template_data["category"],
            schema=template_data["schema"],
        )
        templates.append(template)
    return templates
