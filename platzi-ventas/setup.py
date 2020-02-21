from setuptools import setup
#Este archivo sirve para poder instalar nuestra aplicacion en el sistema, es 
# una receta ya escrita, solo la usamos como dogma :-()
setup(
    name='pv',
    version='0.1',
    py_modules=['pv'],
    install_requires=[
        'click',
    ],
    entry_points='''
        [console_scripts]
        pv=pv:cli
    ''',
)