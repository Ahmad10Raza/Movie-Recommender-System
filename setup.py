from setuptools import setup


#   Setup configuration for the package (metadata)
with open('README.md', encoding='utf-8') as f:
    long_description = f.read()
    
    
REPO_NAME="Movie-Recommender-System",
AUTHOR_USER_NAME="Ahmad10Raza",
SRC_REPO='src'
LIST_OF_REQUIREMENTS=['streamlit']




setup(
    name=SRC_REPO,
    version='0.0.1',
    author=AUTHOR_USER_NAME,
    description='A Movie Recommender System',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    author_email="rjaahmad60@gmail.com",
    packages=[SRC_REPO],
    license='MIT',
    python_requires='>=3.8',
    install_requires=LIST_OF_REQUIREMENTS,
    
)
