from setuptools import setup

setup(
    name='cv-aid',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    install_requires=[
        'deepstack_sdk==0.2.1',
        'filetype==1.0.9',
        'numpy==1.19.5',
        'opencv_python_inference_engine==2021.10.10',
        'setuptools==45.2.0',
    ],
)