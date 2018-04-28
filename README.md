# Remote File Converter

A utility for those using slow or metered connections. This simple utility allows the user to
download and shrink image files on a remote server with a better connection before downloading them to their local system. The general workflow is:

  - User supplies an image url and conversion parameters to the client program (e.g. desired file format, size, bit depth)
  - Client sends commands to remote server to download the image and perform the conversion
  - Client downloads the smaller, post-conversion file to your local system

### Requirements
  - Local machine: python3, 
  - Remote server: python3, imagemagick

### Installation
  - On remote server:
```
git clone https://github.com/bmoyer/remote_file_converter
```

  - On local machine:
```
git clone https://github.com/bmoyer/remote_file_converter
cd remote_file_converter
./make_config.py 
```

### Usage
The following would remotely download a png file, convert it to a jpg scaled to 50% of the original size, and download it to the local system.
```
./client.py --url http://somelarge.image/file.png --format jpg --scale 50 
```

