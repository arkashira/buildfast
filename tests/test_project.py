from project import ProjectManager, ProjectTemplate, Project

def test_get_templates():
    manager = ProjectManager()
    templates = manager.get_templates()
    assert len(templates) == 2
    assert templates[0].name == "Web App"
    assert templates[1].name == "Mobile App"

def test_create_project_from_template():
    manager = ProjectManager()
    project = manager.create_project_from_template("Web App", "My Web App")
    assert project.name == "My Web App"
    assert project.template == "Web App"

def test_create_project_from_template_not_found():
    manager = ProjectManager()
    try:
        manager.create_project_from_template("Unknown Template", "My Project")
        assert False
    except ValueError as e:
        assert str(e) == "Template not found"

def test_create_project_from_scratch():
    manager = ProjectManager()
    project = manager.create_project_from_scratch("My Project")
    assert project.name == "My Project"
    assert project.template is None

def test_get_project():
    manager = ProjectManager()
    project = manager.create_project_from_template("Web App", "My Web App")
    retrieved_project = manager.get_project("My Web App")
    assert retrieved_project == project
