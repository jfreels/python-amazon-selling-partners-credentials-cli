from setuptools import setup

setup(
    name="Amazon Selling Partners API Credentials CLI",
    version="0.1",
    py_modules=["cli"],
    install_requires=[
        "click",
        "python-dotenv",
        "requests"
    ],
    entry_points="""
        [console_scripts]
        cli=cli:cli
    """
)
