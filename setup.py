import setuptools
from pathlib import Path


README = (Path(__file__).parent/"README.md").read_text()

setuptools.setup(
    name="streamlit-disqus",
    version="0.1.0",
    author="okld",
    author_email="",
    description="A streamlit component to integrate Disqus in your applications.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/okld/streamlit-disqus",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[],
    python_requires=">=3.6",
    install_requires=[
        "streamlit >= 0.63",  # TODO Change to 0.73?
    ],
)
