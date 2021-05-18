from setuptools import setup, find_packages
import pathlib
HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()

setup(
    name = "Physical Quantity calculating",
    version = '0.1.0',
    description=
                '''
                    In arithmetic operations, the corresponding physical quantity is automatically generated 
                    and the corresponding coherent unit is selected
                    ''',
    long_description = README,
    long_description_content_type="text/markdown",
    author='chenmich',
    author_email='403189920@qq.com',
    url='',
    packages=['quantities'],
)