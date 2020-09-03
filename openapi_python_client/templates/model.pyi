from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict

{% for relative in model.relative_imports %}
{{ relative }}
{% endfor %}


@dataclass
{% if model.reference.mixins %}
class {{ model.reference.class_name }}({{ model.reference.mixins | join(', ') }}):
{% else %}
class {{ model.reference.class_name }}:
{% endif %}
    """ {{ model.description }} """
    {% for property in model.required_properties + model.optional_properties %}
    {{ property.to_string() }}
    {% endfor %}

    def to_dict(self) -> Dict[str, Any]:
        {% if model.reference.mixins %}
        obj = super().to_dict()
        {% else %}
        obj = {}
        {% endif %}
        {% for property in model.required_properties + model.optional_properties %}
        {% if property.template %}
        {% from "property_templates/" + property.template import transform %}
        {{ transform(property, "self." + property.python_name, property.python_name) | indent(8) }}
        {% else %}
        {{ property.python_name }} =  self.{{ property.python_name }}
        {% endif %}
        {% endfor %}

        obj.update({
            {% for property in model.required_properties + model.optional_properties %}
            "{{ property.name }}": {{ property.python_name }},
            {% endfor %}
        })
        return obj

    @staticmethod
    def from_dict(d: Dict[str, Any], **kwargs) -> {{ model.reference.class_name }}:
{% for mixin in model.reference.mixins %}
        kwargs.update({{ mixin }}.from_dict(d).to_dict())
{% endfor %}
{% for property in model.required_properties + model.optional_properties %}
    {% if property.nullable or not property.required %}
        {% set property_source = 'd.get("' + property.name + '")' %}
    {% else %}
        {% set property_source = 'd["' + property.name + '"]' %}
    {% endif %}
    {% if property.template %}
        {% from "property_templates/" + property.template import construct %}
        {{ construct(property, property_source) | indent(8) }}
    {% else %}
        {{ property.python_name }} = {{ property_source }}
    {% endif %}

{% endfor %}
        return {{ model.reference.class_name }}(
{% for property in model.required_properties + model.optional_properties %}
            {{ property.python_name }}={{ property.python_name }},
{% endfor %}
            **kwargs
        )
