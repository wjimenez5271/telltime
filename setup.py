from setuptools import setup

setup(
    name='telltime',
    version='0.1',
    packages=['telltime'],
    url='https://github.com/wjimenez5271/coastguard',
    license='Apache 2.0',
    author='William Jimenez',
    author_email='wjimenez5271@gmail.com',
    description='Simple CLI utility for working with epoch timestamps',
    zip_safe=False,
    entry_points={
        'console_scripts': ['epoch=telltime.main:main']},
    install_requires = ['argparse'],
)