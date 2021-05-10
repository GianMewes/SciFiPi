import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
  name = 'SciFiPi',
  version = '0.0.1', 				
  license='MIT',
  description = 'SciFiPi - The scientific filtering pipeline to clean your machine learning datasets',
  long_description = long_description,
  long_description_content_type="text/markdown",
  author = 'HSU Institute of Automation',
  #author_email = 'your.email@domain.com',
  url = 'https://github.com/GianMewes/KEEN',
  download_url = 'https://github.com/GianMewes/KEEN/archive/refs/tags/v0.0.1-beta.tar.gz',
  keywords = ['Data Preprocessing', 'Data Filtering', 'Machine Learning', 'AI', 'Data Science', 'python'],
  install_requires=[
    'argparse',
	'ipykernel',
	'ipython',
	'ipython-genutils',
	'numpy',
	'pandas',
	'scikit-learn',
	'fastdtw',
	'dtwalign',
	'tzlocal',
	],
  classifiers=[
    'Development Status :: 3 - Alpha',      # "3 - Alpha", "4 - Beta" or "5 - Production/Stable" -> current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
	'Programming Language :: Python :: 3.7',
	'Programming Language :: Python :: 3.8',
	'Programming Language :: Python :: 3.9',
  ],
  package_dir={"": "src"},
  packages=setuptools.find_packages(where="src"),
)