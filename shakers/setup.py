import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="shakers",
    version="0.0.1",
    author="Nels Hanson",
    author_email="nelshanson@gmail.com",
    description="The Handshake Game",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nelshanson/shakers",
    packages=setuptools.find_packages(),
    entry_points = {
        'console_scripts': ['shakers=shakers.__main__:_main']
    }
    python_requires='>=3.6',
)