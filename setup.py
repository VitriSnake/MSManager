from setuptools import setup, find_packages
import shutil

setup(name = 'MSManager',
      version = 0.1,
      author = 'VitriSnake',
      author_email = 'vitrisnake@celtiumc.fr',
      maintainer = 'CeltiumC',
      maintainer_email = 'contact@celtiumc.fr',
      description = 'Simply create your Minecraft server on Dedicated Server or VPS',
      license = 'GPLv3.0',
      packages = find_packages(),
      include_package_data=True, 
      scripts=[
          'bin/msmanager',
      ],
      zip_safe=False,
      url='https://github.com/VitriSnake/MSManager',
      keywords='Minecraft',
      install_requires=[],
      long_description=open('README.md', 'r').read(),
      long_description_content_type='text/markdown'
     )