from setuptools import setup, find_packages

setup(
    name='rezine_rst',
    version='0.1dev',
    url='https://github.com/rockyburt/rezine_rst',
    license='BSD',
    author='Rocky Burt',
    author_email='rocky@serverzen.com',
    description='A reStructuredText parser plugin for Rezine',
    long_description=open('README').read() + '\n\n' + open('CHANGES').read(),
    zip_safe=False,
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
    ],
    packages=find_packages(),
    install_requires=[
        'Pygments',
        'docutils',
        ],
    entry_points={
        'rezine_plugins': [
            'rezine_rst = rezine_rst'
            ],
        },
    platforms='any',
    include_package_data=True,
)
