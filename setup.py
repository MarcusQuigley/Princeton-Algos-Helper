from setuptools import setup
# setup the package

setup(
    name='algohelpers',
    version='0.2',
    packages=['algohelpers',],
    license='Creative Commons Attribution-Noncommercial-Share Alike license',
    long_description=open('README.txt').read(),
)
# setup(
#     name='evennia',
#     version=get_version(),
#     author="Evennia community",
#     maintainer="Griatch",
#     maintainer_email="griatch AT gmail DOT com",
#     url="http://www.evennia.com",
#     description='A full-featured MUD building toolkit.',
#     packages=find_packages(),
#     scripts=get_scripts(),
#     install_requires=get_requirements(),
#     package_data={'': package_data()},
#     zip_safe=False
# )