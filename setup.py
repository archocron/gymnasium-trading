from setuptools import setup

setup(
    name="gymnasium_trading",
    version="0.0.1",
    install_requires=["gymnasium==0.26.0", "pygame==2.1.3"],
    author='Alejandro Rioja Chocrón',
    author_email='archocron@gmail.com',
    url='https://github.com/archocron/gymnasium-trading',
    packages=['gymnasium_trading'],
    license='gpl-3.0',
    description='Gimnasium environment focus on trading strategies',
    # I explain this later on
    download_url='https://github.com/archocron/gymnasium-trading/archive/refs/tags/0.0.1.tar.gz',

)
