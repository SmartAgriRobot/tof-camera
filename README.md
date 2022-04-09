# ToF Camera
a range imaging camera system employing time-of-flight techniques to resolve distance between the camera and the subject for each point of the image, by measuring the round trip time of an artificial light signal provided by a laser or an LED.

## Features
* Live depth image

## Installation
```
sudo apt update
sudo apt install python3-pip python3-gpiozero python3-serial \
	python3-opencv python3-numpy python3-matplotlib python3-sklearn \
	python3-sklearn-lib libx264-dev libjpeg-dev libgstreamer1.0-dev \
	libgstreamer-plugins-base1.0-dev libgstreamer-plugins-bad1.0-dev \
	gstreamer1.0-plugins-ugly gstreamer1.0-tools gstreamer1.0-gl gstreamer1.0-gtk3
```
## Compatibility
### Hardware :
* Raspberry Pi Zero 2 W
* Cygbot CygLiDAR D1

### Software :
* Raspberry Pi OS (Bullseye)
* Python 3

## Usage
```
git clone https://github.com/SmartAgriRobot/tof-camera.git
cd tof-camera
cd sourcecode
python3 main.py
```
## Video Guide
[SmartAgriRobot Channel](https://www.youtube.com/channel/UCOgiOXJ43hnMZIsxGAZKoPQ)

## Folder structure
| ###Folder Name  | ###detail  |
| :------------ |:---------------|
| 3d            | STL file part for 3d printer |
| clip          | Operation video clip       |
| images        | Images of prototype        |
| pdf           | Specification document        |
| sourcecode    | Python source code        |

## License and Credits
The ToF Camera is released under the MIT license.

## Disclaimer
This source and the whole package comes without warranty. It may or may not harm your computer or cell phone. Please use with care. Any damage cannot be related back to the author. The source has been tested on a virtual environment and scanned for viruses and has passed all tests.
