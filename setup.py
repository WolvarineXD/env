from setuptools import setup, find_packages

setup(
    name="env",
    version="0.1.0",
    packages=find_packages(),
    install_requires=["click"],
    entry_points={
        "console_scripts": [
            "env=env.cli:cli",
        ],
    },
    author="WolvarineXD",
    description="A simple environment management tool",
    url="https://github.com/WolvarineXD/env",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
