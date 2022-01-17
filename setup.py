from setuptools import setup, find_packages

setup(
    name='department_app',
    version='1.0',
    author='Yehor Romaniuk',
    author_email='krasheg@gmail.com',
    url='https://github.com/krasheg/final_project_python_epam',
    install_requires=[
        'Flask==2.0.2',
        'Flask-Migrate==3.1.0',
        'Flask-RESTful==0.3.9',
        'Flask-SQLAlchemy==2.5.1',
    ],
    include_package_data=True,
    zip_safe=False,
    packages=find_packages()
)
