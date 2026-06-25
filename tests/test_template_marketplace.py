import pytest
from template_marketplace import Template, TemplateMarketplace, load_templates_from_json

def test_template_marketplace_get_templates():
    templates = [
        Template(1, "Template 1", "thumbnail1", "description1", ["tag1"], "SaaS", {"schema": "schema1"}),
        Template(2, "Template 2", "thumbnail2", "description2", ["tag2"], "Marketplace", {"schema": "schema2"}),
        Template(3, "Template 3", "thumbnail3", "description3", ["tag3"], "SaaS", {"schema": "schema3"}),
    ]
    marketplace = TemplateMarketplace(templates)
    saas_templates = marketplace.get_templates("SaaS")
    assert len(saas_templates) == 2
    assert saas_templates[0].name == "Template 1"
    assert saas_templates[1].name == "Template 3"

def test_template_marketplace_import_template():
    templates = [
        Template(1, "Template 1", "thumbnail1", "description1", ["tag1"], "SaaS", {"schema": "schema1"}),
        Template(2, "Template 2", "thumbnail2", "description2", ["tag2"], "Marketplace", {"schema": "schema2"}),
    ]
    marketplace = TemplateMarketplace(templates)
    imported_schema = marketplace.import_template(1)
    assert imported_schema == {"schema": "schema1"}
    with pytest.raises(ValueError):
        marketplace.import_template(3)

def test_template_marketplace_load_templates():
    templates = [
        Template(1, "Template 1", "thumbnail1", "description1", ["tag1"], "SaaS", {"schema": "schema1"}),
        Template(2, "Template 2", "thumbnail2", "description2", ["tag2"], "Marketplace", {"schema": "schema2"}),
    ]
    marketplace = TemplateMarketplace(templates)
    loaded_templates = marketplace.load_templates()
    assert len(loaded_templates) == 2
    assert loaded_templates[0].name == "Template 1"
    assert loaded_templates[1].name == "Template 2"

def test_load_templates_from_json():
    json_data = """
    [
        {
            "id": 1,
            "name": "Template 1",
            "thumbnail": "thumbnail1",
            "description": "description1",
            "tags": ["tag1"],
            "category": "SaaS",
            "schema": {"schema": "schema1"}
        },
        {
            "id": 2,
            "name": "Template 2",
            "thumbnail": "thumbnail2",
            "description": "description2",
            "tags": ["tag2"],
            "category": "Marketplace",
            "schema": {"schema": "schema2"}
        }
    ]
    """
    templates = load_templates_from_json(json_data)
    assert len(templates) == 2
    assert templates[0].name == "Template 1"
    assert templates[1].name == "Template 2"
