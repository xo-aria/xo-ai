from setuptools import setup, find_packages

setup(
    name="xo-ai",
    version="1.0.0",
    author="XO Aria",
    author_email="hf18950@email.com",
    description="XO — Minimal Conversational Intelligence Framework",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[],
    entry_points={
        "console_scripts": [
            "xo=xo.cli:run_cli",
        ]
    },
    python_requires=">=3.8",
)
