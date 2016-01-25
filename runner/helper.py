import subprocess
import re

class SuperSecureInterpreter:
    # Reconsider the Nameing here
    templates = {
        'javascript': {
            'base': "{code}",
            'test': "{code}"
        },
        'python': {
            'base': "{code}",
            'test': "def print(*args,**kwargs):pass;\n{code}\nif __name__=='__main__':unittest.main();"
        }
    }
    interpreters = {
        'javascript': 'node -e', 
        'python': 'python3 -c'
    }
    # test_result = {
    #     'javascript': r', 0 failures\n', 
    #     'python': r'OK$'
    # }
    def __init__(self, code_string, language='python', template_type='base'):
        self.code_string = code_string
        self.language = language
        self.interpreter = self.interpreters[language]
        self.template_set = self.templates[language]
        self.template_type = template_type 
        self.result = None

    def open(self):
        code_template = self.template_set.get(self.template_type, self.template_set['base'])
        code_to_run = code_template.format(code=self.code_string)
        self.result = subprocess.getoutput('{} "{}"'.format(
                self.interpreter,
                code_to_run.replace('"','\\"')
            )
        )

    def analyze(self):
        if self.language == 'python':
            if re.search(r'OK$', self.result):
                return True
        elif self.language == 'javascript':
            if re.search(r', 0 failures\n', self.result):
                return True
        return False