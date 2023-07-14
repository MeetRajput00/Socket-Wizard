from setuptools import setup, find_packages
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.read()
setup(
    name = 'ports',
    version = '0.0.1',
    author = 'Meet Rajput',
    author_email = 'rajputmeet10@gmail.com',
    license = 'MIT License',
    description = 'This cli tool is used to create server and listener on your machine.',
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = 'https://github.com/MeetRajput00/Ports',
    py_modules = ['port', 'app'],
    packages = find_packages(),
    install_requires = [requirements],
    python_requires='>=3.7',
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "Operating System :: OS Independent",
    ],
    entry_points = '''
        [console_scripts]
        cooltool=my_tool:cli
    '''
)