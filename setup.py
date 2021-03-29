from setuptools import setup, find_packages

requirements = [
    "autopep8",
    "pyyaml"
]

setup(
    name="Bento Box",
    version="0.1.0",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "bento = src.__main__:main"
        ]
    },
    install_requires=requirements,
)
