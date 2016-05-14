#!/bin/sh

gpioctl dirout 15
gpioctl dirout 17

case "$1" in
    "f" )
        gpioctl clear 15
        gpioctl clear 17 ;;

    "s" )
        gpioctl set 15
        gpioctl clear 17 ;;

    "b" )
        gpioctl set 15
        gpioctl set 17 ;;
esac

