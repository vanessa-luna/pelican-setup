from subprocess import call
from webassets.filter import Filter

class MythFilter(Filter):
    name = 'myth'

    def output(self, _in, out, **kwargs):

        out.write(_in.read())



        subprocess.Popen("myth _in", shell=True, stdout=subprocess.PIPE).stdout.read()

    def input(self, _in, out, **kwargs):
        myth input.css output.css
        call(["myth", "-l"])


        out.write(_in.read())
