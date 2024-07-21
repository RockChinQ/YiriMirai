from setuptools import find_namespace_packages
from setuptools import setup

setup(
    name="yiri-mirai-rc",
    version="0.2.8.0",
    description="一个轻量级、低耦合的基于 mirai-api-http 的 Python SDK。",
    long_description=open("README.md", "rt", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/RockChinQ/YiriMirai",
    project_urls={
        "Bug Report": "https://github.com/RockChinQ/YiriMirai/issues"
    },
    author="RockChinQ",
    author_email="1010553892@qq.com",
    license="GNU Affero General Public License v3.0",
    packages=find_namespace_packages("src"),
    package_dir={"": "src"},
    py_modules=["mirai"],
    package_data={"": ["*.json"]},
    install_requires=[
        "httpx",
        "pydantic>=2.0.0",
        "websockets>=12.0",
        "typing-extensions",
        "starlette",
        "aiofiles",
    ],
    classifiers=[
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "Natural Language :: English",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
)