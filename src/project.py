import json
from dataclasses import dataclass
from typing import List

@dataclass
class ProjectTemplate:
    name: str
    description: str

@dataclass
class Project:
    name: str
    template: str = None

class ProjectManager:
    def __init__(self):
        self.templates = [
            ProjectTemplate("Web App", "A basic web application template"),
            ProjectTemplate("Mobile App", "A basic mobile application template"),
        ]
        self.projects = []

    def get_templates(self) -> List[ProjectTemplate]:
        return self.templates

    def create_project_from_template(self, template_name: str, project_name: str) -> Project:
        template = next((t for t in self.templates if t.name == template_name), None)
        if template:
            project = Project(project_name, template_name)
            self.projects.append(project)
            return project
        else:
            raise ValueError("Template not found")

    def create_project_from_scratch(self, project_name: str) -> Project:
        project = Project(project_name)
        self.projects.append(project)
        return project

    def get_project(self, project_name: str) -> Project:
        return next((p for p in self.projects if p.name == project_name), None)
