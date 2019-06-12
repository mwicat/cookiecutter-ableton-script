from _Framework.ControlSurface import ControlSurface


class {{ cookiecutter.application_title }}(ControlSurface):

    def __init__(self, c_instance):
        super({{ cookiecutter.application_title }}, self).__init__(c_instance)
        self.log_message('Initializing {{ cookiecutter.application_title }}...')

        with self.component_guard():
            pass

        self.log_message('Initialized {{ cookiecutter.application_title }}.')
