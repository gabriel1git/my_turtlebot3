import os
from glob import glob
from setuptools import setup

package_name = 'my_turtlebot3'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
  	    (os.path.join('share', package_name,'meshes'), glob('meshes/*')),
  	    (os.path.join('share', package_name,'urdf'), glob('urdf/*')),
  	    (os.path.join('share', package_name, 'config'), glob('config/*')),
  	    (os.path.join('share', package_name,'sdf'), glob('sdf/*')),
  	    (os.path.join('share', package_name), glob('launch/*.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='gabriel',
    maintainer_email='ggabriel9925@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            #'trajectory_msg = icrane2.controller:main'
            'sdf_spawn = my_turtlebot3.spawn_entity:main',
            'occupancy_grid = my_turtlebot3.occupancy_grid_pub:main',
            'listener = my_turtlebot3.subscriber_lidar:main',
        ],
    },
)
