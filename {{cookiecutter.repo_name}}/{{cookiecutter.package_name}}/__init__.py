from {{ cookiecutter.application_name }} import {{ cookiecutter.application_title }}


def create_instance(c_instance):
    return {{ cookiecutter.application_title }}(c_instance)
