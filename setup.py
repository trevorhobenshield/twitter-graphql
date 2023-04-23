from textwrap import dedent

from setuptools import find_packages, setup

install_requires = [
    "httpx",
    "nest_asyncio",
    'uvloop; platform_system != "Windows"',
    "orjson",
    "tqdm",
]

setup(
    name="twitter-graphql",
    version="0.0.0",
    python_requires=">=3.11.0",
    description="Unofficial Twitter GraphQL API",
    long_description=dedent('''
    
    Unofficial Twitter GraphQL API
    
    '''),
    long_description_content_type='text/markdown',
    author="Trevor Hobenshield",
    author_email="trevorhobenshield@gmail.com",
    url="https://github.com/trevorhobenshield/twitter-graphql",
    install_requires=install_requires,
    keywords="twitter api graphql client",
    packages=find_packages(),
    include_package_data=True,
)
