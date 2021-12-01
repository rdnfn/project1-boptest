import pathlib
import setuptools


here = pathlib.Path(__file__).parent.resolve()
long_description = (here / 'README.md').read_text(encoding='utf-8')

setuptools.setup(
    name="boptest",
    version="0.1.0",
    description="Building Optimization Performance Tests",
    long_description=long_description,
    long_description_content_type="text/markdown",
    package_dir={"boptest": ""},
    packages= ["boptest." + package for package in setuptools.find_packages()],
    python_requires=">=3.6",
)
