import os
import re
import setuptools


def read(fname, version=False):
    text = open(os.path.join(os.path.dirname(__file__), fname), encoding="utf8").read()
    if version:
        text = re.search(r'__version__ = "(.*?)"', text).group(1)
    return text


setuptools.setup(
    name="SafoneAPI",
    packages=setuptools.find_packages(),
    version=read("SafoneAPI/__init__.py", version=True),
    license="MIT",
    description="Asynchronous Python Wrapper For SafoneAPI",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="AsmSafone",
    author_email="asmsafone@gmail.com",
    url="https://github.com/AsmSafone/SafoneAPI",
    project_urls={
        "Homepage": "https://api.safone.co",
        "Documentation": "https://api.safone.co/docs",
        "Issue Tracker": "https://github.com/AsmSafone/SafoneAPI/issues",
    },
    keywords=["API", "SafoneAPI", "Safone-API", "Safone_API"],
    install_requires=["aiohttp", "aiofiles", "pyrogram"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Natural Language :: English",
    ],
    python_requires="~=3.7",
)
