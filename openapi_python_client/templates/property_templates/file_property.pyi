{% macro construct(property, source, initial_value=None) %}
{{ property.python_name }} = File(
     payload = BytesIO({{ source }})
)
{% endmacro %}

{% macro check_type_for_construct(source) %}isinstance({{ source }}, bytes){% endmacro %}

{% macro transform(property, source, destination, declare_type=False, query_parameter=False) %}
{% if property.required %}
{% if property.nullable %}
{{ destination }} = {{ source }}.to_tuple() if {{ source }} else None
{% else %}
{{ destination }} = {{ source }}.to_tuple()
{% endif %}
{% else %}
{{ destination }}{% if declare_type %}: {{ property.get_type_string(query_parameter=query_parameter, json=True) }}{% endif %} = UNSET
if not isinstance({{ source }}, Unset):
{% if property.nullable or query_parameter %}
    {{ destination }} = {{ source }}.to_tuple() if {{ source }} else None
{% else %}
    {{ destination }} = {{ source }}.to_tuple()
{% endif %}
{% endif %}
{% endmacro %}
