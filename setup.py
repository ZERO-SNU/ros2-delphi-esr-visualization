from setuptools import setup
from glob import glob
import os

package_name = 'radar_visualizer'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.xml')),
        (os.path.join('share', package_name, 'config'), glob('config/*'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Hwang Dongha',
    maintainer_email='depth221@gmail.com',
    description='Driver codes for visualization of objects from the Delphi ESR 2.5 RADAR',
    license='MIT Licence',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'radar_visualizer_node = radar_visualizer.radar_visualizer_node:main',
        ],
    },
)
