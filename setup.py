from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in mdpl_custom/__init__.py
from mdpl_custom import __version__ as version

setup(
	name="mdpl_custom",
	version=version,
	description="Mdpl Custom",
	author="amafhh",
	author_email="infotechamafhh@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
