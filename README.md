<h1 align="center">
    <a href="https://runshaw.hackclub.com/christmastree">
    <img src="./image.png">
    </a>
</h1>

<p align="center">
    <i align="center">A Runshaw Hack Club project to have your code run on real hardware!</i>
</p>

## 📝 Introduction

Welcome to the Runshaw Hack Club Christmas Tree project! Ever wanted to write your own LED light show? Now you can! We've created a simple python API that allows you to control the lights on our Christmas tree. If you submit an effect, it will be run on the tree for everyone to see!

## 🛠️ Getting Started

To get started, you'll need to install our custom python library. You can find our more at the [github repository](https://github.com/Runshaw-Hack-Club/Christmas-Tree-API). Once you've installed the library, you can start writing your own effects! See the [examples](./examples) folder for some inspiration.


## ⚙️ Hardware

We've created two trees for your code to be run on. The first tree is made up of 200 WS2812B LED pixels, and controlled by a Raspberry Pi 4B with 4GB of RAM. The second tree is made up of 50 WS2812B LED pixels, and controlled by a Raspberry Pi Zero W. Both trees are running the same code, so you can be sure that your effect will run on both trees.

## 💡 Submitting an Effect

To submit an effect, simply create a pull request to this repository with your effect in the [effects](./effects) folder. Your effect should be a python file which uses our custom library to control the lights. Please ensure that you have set debug to False in your effect, as this will be run on the real hardware.

When writing an effect, please try to avoid:
- Dark colours, as they are hard to see on the tree
- Fast flashing

Any questions? Email me [here](mailto:hi@danieldb.uk). 

## 🎄 Creating your own tree

Are you a Hack Club leader wanting to run your own tree program? We've made it easy for you to set up your own tree! Feel free to use our code and hardware setup to create your own tree. You can fork this repository and modify the code to suit your needs. On you raspberry pi, you'll want to run the file `pi/cycle_effects.py` as a systemd service. This will allow the tree to run your effects on boot.