from openapi_python_client.templates.types import UNSET

{% macro construct(property, source) %}
{% if property.required %}
{{ property.python_name }} = {{ property.reference.class_name }}({{ source }})
{% else %}
{{ property.python_name }} = None
if {{ source }} is not None:
    {{ property.python_name }} = {{ property.reference.class_name }}({{ source }})
{% endif %}
{% endmacro %}

{% macro transform(property, source, destination) %}
{% if property.required %}
{{ destination }} = {{ source }}.value
{% else %}
if {{ source }} is UNSET:
    {{ destination }} = UNSET
else:
    {{ destination }} = {{ source }}.value if {{ source }} else None
{% endif %}
{% endmacro %}
