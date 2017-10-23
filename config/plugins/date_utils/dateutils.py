
from pelican import signals

def register():
    signals.generator_init.connect(add_filter)

def add_filter(pelican):
    pelican.env.filters.update({'relativeDate': relativeDate})




from delorean import Delorean

def relativeDate(date):
    return Delorean(date).humanize()
