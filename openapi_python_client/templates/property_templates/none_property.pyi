{% macro construct(property, source) %}
{{ property.python_name }} = None
{% endmacro %}

{% macro transform(property, source, destination, declare_type=True) %}
{{ destination }} =  None
{% endmacro %}
