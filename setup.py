from setuptools import setup

setup(
    name="gymnasium_trading",
    version="0.0.3",
    install_requires=["gymnasium==0.28.1", "pygame==2.5.0"],
    author='Alejandro Rioja Chocrón',
    author_email='archocron@gmail.com',
    url='https://github.com/archocron/gymnasium-trading',
    packages=['gymnasium_trading'],
    license='gpl-3.0',
    description='Gimnasium environment focus on trading strategies',
    # I explain this later on
    download_url='https://github.com/archocron/gymnasium-trading/archive/refs/tags/0.0.3.tar.gz',

)
