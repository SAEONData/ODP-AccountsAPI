from setuptools import setup, find_packages

version = '1.0.0'

setup(
    name='ODP-AccountsAPI',
    version=version,
    description='The ODP Accounts API',
    url='https://github.com/SAEONData/ODP-AccountsAPI',
    author='Mark Jacobson',
    author_email='mark@saeon.ac.za',
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
    python_requires='~=3.7',
    install_requires=[
        'fastapi',
        'sqlalchemy',
        'python-dotenv',
    ],
    extras_require={
        'test': ['pytest', 'coverage']
    },
    dependency_links=[
        'git+https://github.com/SAEONData/Hydra-Admin-Client.git#egg=Hydra_Admin_Client',
        'git+https://github.com/SAEONData/ODP-AccountsLib.git#egg=ODP_AccountsLib',
    ],
)
