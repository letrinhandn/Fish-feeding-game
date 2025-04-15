from setuptools import setup, find_packages

setup(
    name="feedmyfish",
    version="1.0.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "pygame",
        "windows-curses;platform_system=='Windows'",
    ],
    entry_points={
        'console_scripts': [
            'feedmyfish=koi_game.run:main',
        ],
    },
    python_requires='>=3.6',
    author="Nhan",
    description="A terminal-based koi fish game with interactive feeding system",
    keywords="game, terminal, ascii-art, koi, fish",
    url="https://github.com/yourusername/koi-game",  # Thay thế bằng URL GitHub của bạn
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Games/Entertainment",
    ],
)