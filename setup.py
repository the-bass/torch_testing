import setuptools


README_LOCATION = 'README.md'


with open(README_LOCATION, 'r') as readme_file:
    long_description = readme_file.read()

setuptools.setup(
    name='torch_testing',
    version="0.0.1",
    author="The Bass",
    author_email="the-bass@posteo.co",
    description="A collection of assertion methods to compare PyTorch Tensors in tests",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/the-bass/torch_testing",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
