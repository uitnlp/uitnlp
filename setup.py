import setuptools

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

__version__ = 'v0.1.2'

setuptools.setup(
    name='uitnlp',
    packages=setuptools.find_packages(),
    version=__version__,
    author='The UIT Natural Language Processing Group',
    author_email='vund@uit.edu.vn',
    description='UITNLP: A Python NLP Library for Vietnamese',
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords='natural-language-processing nlp natural-language-understanding uit-nlp vietnamese-word-segmentation',
    url='https://github.com/uitnlp/uitnlp.git',
	license='Apache License 2.0',
    classifiers=[
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Programming Language :: Python :: 3.6',
		'Programming Language :: Python :: 3.7',
		'Programming Language :: Python :: 3.8',
    ],
    include_package_data=True,
    python_requires='>=3.6',
    install_requires=[
        'sklearn',
        'numpy',
        'pandas',
        'nltk',
        'gdown',
    ]
)