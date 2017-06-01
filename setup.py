from setuptools import setup

setup(name='bmp280_median_logger',
      version='0.1',
      description='Logs 60 sec median values (time shift consistent) to log file.',
      author='Andreas Krietemeyer',
      author_email='andreas.krietemeyer@gmail.com',
      license='MIT',
      install_requires=['numpy', 'pandas'],
      packages=['bmp280_median_logger'],
      )
