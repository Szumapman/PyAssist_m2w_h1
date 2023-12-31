from setuptools import setup, find_namespace_packages

packages = [package for package in 
            find_namespace_packages(
                where='./pyassist', 
                include='package_cheat_sheet.*'
)]

setup(
    name='pyassist',
    version='2.1',
    description='The program allows the user to manage data in an address book, including tasks such as adding, deleting, exporting, and importing records. It also features the capability to export and import data in CSV format. Additionally, the program facilitates file sorting on the computer. It provides error handling and a user-friendly command-line interface for easy of use.',
    url='https://github.com/Szumapman/PyAssist_m2w_h1',
    author=('Paweł Szumański',),
    author_email='',
    packages=packages,
    package_dir={"": "pyassist"},
    install_requires=[
        # 'SpeechRecognition', # Modules used for speech recognition
        # 'pyttsx3',           # and changing text to speech.
        # 'pyaudio',           # Currently disabled.
        'pyfiglet',
        'cowsay',
        'prompt_toolkit',
        'validator-collection',
    ],
    entry_points={'console_scripts': ['pyassist = cli_pyassist:main']}
)