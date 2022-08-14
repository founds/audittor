from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / "README.md").read_text(encoding="utf-8")

REQUIREMENTS = [i.strip() for i in open("requirements.txt").readlines()]

setup(
    name='audittor',
    version='0.2',
    package_dir={"": "audittor"},
    packages=find_packages(where="audittor"),
    url='https://www.altsys.es',
    license='GNU GPLv3',
    author='altsys',
    author_email='info@altsys.es',
    description='Audita el sistema en busqueda de fallos de configuración',
    long_description=long_description,
    install_requires=REQUIREMENTS
)
