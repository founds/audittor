from setuptools import setup, find_packages
import pathlib

setup(
    name='audittor',
    version='0.3',
    package_dir={"": "audittor"},
    packages=find_packages(where="audittor"),
    url='https://www.altsys.es',
    license='GNU GPLv3',
    author='altsys',
    author_email='info@altsys.es',
    description='Audita el sistema en busqueda de fallos de configuración',
    long_description='Audita el sistema en busqueda de fallos de configuración',
    scripts=['audittor.py'],
    data_files   = [(['Audittor.desktop'])],
)
