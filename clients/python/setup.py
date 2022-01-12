import pathlib
from setuptools import setup
import pkg_resources

with pathlib.Path('requirements.txt').open() as f:
    install_requires = [str(r) for r in pkg_resources.parse_requirements(f)]

setup(name='sust-api-clients',
      version='0.0.1',
      description='Sust Global API Clients',
      packages=[
        'sust.api.climate_explorer',
        'sust.api.climate_explorer.clientgen',
        'sust.api.climate_explorer.clientgen.api',
        'sust.api.climate_explorer.clientgen.apis',
        'sust.api.climate_explorer.clientgen.model',
        'sust.api.climate_explorer.clientgen.models',
      ],
      install_requires=[install_requires],
     )
