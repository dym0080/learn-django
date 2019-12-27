from django import template

# [自定义模板标签]不懂，这块文档还没学习过。
# 文档地址： https://docs.djangoproject.com/zh-hans/2.2/howto/custom-template-tags/

register = template.Library()

@register.filter
def field_type(bound_field):
    return bound_field.field.widget.__class__.__name__

@register.filter
def input_class(bound_field):
    css_class = ''
    if bound_field.form.is_bound:
        if bound_field.errors:
            css_class = 'is-invalid'
        elif field_type(bound_field) != 'PasswordInput':
            css_class = 'is-valid'
    return 'form-control {}'.format(css_class)