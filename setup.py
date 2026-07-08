import setuptools 

with open("Readme.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()



__version__ = "0.0.0"

PROJECT_NAME = "End-to-End Text Summarization"
REPO_NAME = "Text-Summarization"
AUTHOR = "SriDevi Marlothu"
AUTHOR_EMAIL = "uniquesridevi0629@gmail.com"
GITHUB_USER_NAME = "SriDevi1806"

SRC_REPO = "src"

setuptools.setup(
    name=PROJECT_NAME,
    version=__version__,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    description="End-to-End Text Summarization using NLP",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{GITHUB_USER_NAME}/{REPO_NAME}",
    package_dir={"": SRC_REPO},
    packages=setuptools.find_packages(where=SRC_REPO),
    include_package_data=True,
    python_requires=">=3.11",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

