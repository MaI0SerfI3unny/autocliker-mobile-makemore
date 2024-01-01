# AutoCliker For Mobile Game "Make More"

![ScreenIntro](https://github.com/MaI0SerfI3unny/autocliker-mobile-makemore/blob/main/readme/img/Autoclicker.png)

# Installation

```sh
git clone https://github.com/MaI0SerfI3unny/autocliker-mobile-makemore.git
cd autocliker-mobile-makemore
pip3 install -r requirements.txt
python3 main.py --path=./make_more.png 
```

# Configuration

To use the program, you will need two devices - a computer on which this script is run, as well as a mobile phone, in which the "Make More!" program must be running. Also, you need to install remote access software on both devices - TeamViewer or Anydesk, the choice is yours.

# Example configuration on TeamViewer

1. Install TeamViewer on your computer.
2. Install TeamViewer QuickSupport on your phone.
3. Launch TeamViewer on both devices and make a remote connection through your computer to your phone. As soon as the phone picture is visible, you need to go through the phone to the game “Make More!” Finally, run the python script program according to the instructions above.

```sh
python3 main.py --path=./make_more.png 
```

The --path argument is responsible for the path to the picture that needs to be searched on the screen and automatically clicked. This argument is important and the script will not run without the path. The script itself can work on other games where you only need to click. To do this, you can take a photo of the selected area and enter in the --path argument the path to the photo you want to auto-click on.

