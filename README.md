# legoraps

used libs:

https://www.linux-projects.org/uv4l/

1. upgrade to buster
sudo apt dist-upgrade
pip install pigpio


2. 
sudo apt-get install uv4l uv4l-raspicam uv4l-server uv4l-webrtc uv4l-raspicam-extras
sudo apt-get install uv4l uv4l-server uv4l-uvc uv4l-server uv4l-webrtc uv4l-xmpp-bridge
8090 for usb device
8080 for board cam

openssl genrsa -out selfsign.key 2048 && openssl req -new -x509 -key selfsign.key -out selfsign.crt -sha256
enable I2C and cam

https://raspberry-valley.azurewebsites.net/UV4L/

TODO's:
main config file
boot script
installation script