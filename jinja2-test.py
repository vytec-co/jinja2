import jinja2

# assume it is an unittest function
context = {  # your variables to pass to template
    'test_var': 'test_value'
}
path = 'path/to/template/dir'
filename = 'tempalte_to_test.tpl'

rendered = jinja2.Environment(
    loader=jinja2.FileSystemLoader(path)
).get_template(filename).render(context)

# `rendered` is now a string with rendered template
# do some asserts on `rendered` string 
# i.e.
assert 'test_value' in rendered
