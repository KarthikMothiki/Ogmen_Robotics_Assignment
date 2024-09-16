from setuptools import find_packages, setup

package_name = 'bot_control'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='km',
    maintainer_email='62557178+KarthikMothiki@users.noreply.github.com',
    description='TODO: Package description',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'laser_filter = bot_control.reading_laser:main',
            'move_robot = bot_control.move:main',
        ],
    },
)
