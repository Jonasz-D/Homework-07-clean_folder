from setuptools import setup

setup(name = 'clean_folder',
      version='1',
      url='d',
      author='JD',
      license='MIT',
      packages=['clean_folder'],
      entry_points = {'console_scripts': ['clean-folder = clean_folder.clean:sort']}
      )