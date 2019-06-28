import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sim-cli",
    version="0.0.1",
    author="Benjamin Fox",
    author_email="foxbenjaminfox@gmail.com",
    description="CLI for semantic string similarity",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/foxbenjaminfox/string-similarity-cli",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Affero General Public License v3",
    ],
    install_requires=[
        "rpyc",
        "spacy",
        "en_vectors_web_lg @ https://github.com/explosion/spacy-models/releases/download/en_vectors_web_lg-2.1.0/en_vectors_web_lg-2.1.0.tar.gz#egg=en_vectors_web_lg-2.1.0",
    ],
    entry_points={"console_scripts": ["sim=sim_cli:main"]},
)
