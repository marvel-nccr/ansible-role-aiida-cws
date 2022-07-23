# https://ipython.readthedocs.io/en/stable/config/intro.html#python-configuration-files
c = get_config()
c.InteractiveShellApp.extensions = [
  # this allows the use of the %aiida magic in aiida v1.x
  'aiida.tools.ipython.ipython_magics'
]
