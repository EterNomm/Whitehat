from setuptools import setup, find_packages
import re

with open('README.md') as f:
    long_description = f.read()

version = ''
with open('whitehat/__init__.py') as f:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE).group(1)

if not version:
    raise RuntimeError('Version is not set')

def read_requirements():
    with open('requirements.txt', 'r') as req:
        content = req.read()
        requirements = content.split('\n')

    return requirements


setup(
    name='whitehat',
    version=version,
    author='LyQuid',
    author_email='lyquidpersonal@gmail.com',
    description = 'Python Packages For Ethical Hacking',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='Apache License 2.0',
    url='https://github.com/EterNomm/Whitehat',
    project_urls={
        "Source Code": "https://github.com/EterNomm/Whitehat",
        "Discord": "https://discord.gg/qpT2AeYZRN",
        "Issue tracker": "https://github.com/EterNomm/Whitehat/issues"
    },
    packages=find_packages(),
    include_package_data=True,
    install_requires=read_requirements(),
    keywords=["python", "hacking", "whitehat", "hacking tool", "ethical hacking"],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Science/Research',
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: Android',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: MacOS',
        'Operating System :: POSIX :: Linux'
    ]
)
