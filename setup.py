import setuptools

setuptools.setup (
  include_package_data = True, 
  name='TextAnalyzerPy',
  version='0.0.1',
  description='oss-dev my calculator 0002',
  author='jiwoojeong',
  author_email='erase.jeong@gmail.com',
  url = "https://github.com/erase-jeong/TextAnalyzerPy",
  download_url = "https://github.com/erase-jeong/TextAnalyzerPy/archive/refs/tags/v0.0.1.zip",
  install_requires=['pytest'],
  long_description = 'oss-dev calculator python module',
  long_description_content_type = 'text/markdown',
  classifiers=[
      "Programmming Language :: Python :: 3",
      "Operating System :: OS Independent",
  ],
)
