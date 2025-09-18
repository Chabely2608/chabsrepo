from setuptools import find_packages, setup

package_name = 'create3_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/create3_pkg/launch', ['launch/slam.launch.py']),
        ('share/create3_pkg/config', ['config/slam_params.yaml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='chabelypecina',
    maintainer_email='chabelypecina@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "linear_mov = create3_pkg.ej1:main",
            "teleop_keyboard = create3_pkg.keyboard_teleop:main"
        ],
    },
)
