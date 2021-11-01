from setuptools import setup, find_packages

with open('README.md') as f:
    long_description = f.read()

def read_requirements():
    with open('requirements.txt', 'r') as req:
        content = req.read()
        requirements = content.split('\n')

    return requirements


#####################################
VERSION = "0.4.3"
#####################################

setup(
    name='whitehat',
    version=VERSION,
    author='LyQuid',
    author_email='lyquidpersonal@gmail.com',
    description = 'Python Library For Ethical Hacker',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='Apache License 2.0',
    url='https://github.com/EterNomm/Whitehat',
    packages=find_packages(),
    include_package_data=True,
    install_requires=read_requirements(),
    keywords=["python", "hacker", "whitehat", "hacker tool", "ethical hacker"]
)
