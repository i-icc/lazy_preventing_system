sudo apt-get update
sudo apt-get upgrade
sudo pip3 install --upgrade pip
sudo apt-get install libavutil56 libcairo-gobject2 libgtk-3-0 libqtgui4 libpango-1.0-0 libqtcore4 libavcodec58 libcairo2 libswscale5 libtiff5 libqt4-test libatk1.0-0 libavformat58 libgdk-pixbuf2.0-0 libilmbase23 libjasper1 libopenexr23 libpangocairo-1.0-0 libwebp6
sudo pip3 install opencv-python==4.2.0.32 lxml tqdm
curl -sc /tmp/cookie "https://drive.google.com/uc?export=download&id=1bbr5x_0bQ1e-yIe0F4F-47G859NzYhvz" > /dev/null
CODE="$(awk '/_warning_/ {print $NF}' /tmp/cookie)"
curl -Lb /tmp/cookie "https://drive.google.com/uc?export=download&confirm=${CODE}&id=1bbr5x_0bQ1e-yIe0F4F-47G859NzYhvz" -o tensorflow-2.7.0-cp39-none-linux_aarch64.whl
echo Download finished.
sudo pip3 install tensorflow-2.7.0-cp39-none-linux_aarch64.wh
