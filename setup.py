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
    maintainer='user',
    maintainer_email='junha308@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'radar_visualizer_node = radar_visualizer.radar_visualizer_node:main',
        ],
    },
)
