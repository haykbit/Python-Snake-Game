from setuptools import setup

with open("README", 'r') as f:
    long_description = f.read()

setup(
    name='snake-game',
    version='1.0',
    description='A snake game programed with python',
    license="HaykPetrosyanElmayan",
    long_description=long_description,
    author='Hayk Petrosyan',
    author_email='hpetrosyan.projects@gmail.com',
    packages=['snake-game'],  # same as name
)
