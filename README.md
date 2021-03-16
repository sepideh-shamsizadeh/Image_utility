# Image Utility

A library for drawing rectangle on image and geting the rectangle location(x, y, w, h).

### Branches

#### master


## Input requirements
Each time you could pass a path of image.


## How does it work
Mouse for drawing rectangle.
- Esc : stoping.
- z : undo.
- r : reset.
- '+' : zoom-in
- '-' : Get out of zoom.

## Project Setup, Setting up development Environment on Ubuntu:

### Prerequisites


```bash
sudo apt install tesseract-ocr libtesseract-dev libleptonica-dev build-essential libncursesw5-dev libreadline6-dev libssl-dev \
  libgdbm-dev libc6-dev libbz2-dev
```

### Python3.6

```bash
sudo apt update && sudo apt build-dep python3.5
cd /tmp
wget https://www.python.org/ftp/python/3.6.4/Python-3.6.4.tgz
tar -xvf Python-3.6.*.tgz
cd Python-3.6.*
./configure
make -j 8
sudo make altinstall
```

### Preparing the install location

#### Install Virtual environment

```bash
sudo pip3.6 install virtualenvwrapper
```

#### Setup virtual environment
```bash
echo "export VIRTUALENVWRAPPER_PYTHON=`which python3.6`" >> ~/.bashrc
echo "alias v.activate=\"source $(which virtualenvwrapper.sh)\"" >> ~/.bashrc
source ~/.bashrc
v.activate
mkvirtualenv --python=$(which python3.6) --no-site-packages image_utility
```
#### Activating virtual environment

```bash
workon image_utility
```

#### Cloning

```bash
mkdir -p ~/workspace
cd ~/workspace
git clone git@github.com:sepidehshams/image-utility.git
cd image-utility
pip install -e .
```
### Command-line Interface:
```bash
usage: image-utility `path/to/images`
```
