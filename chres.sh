#!/bin/bash

sudo sed /boot/config.txt -i.org -e "/^dtoverlay=vc4-kms/s/^/#/" -e "/^#dtoverlay=vc4-kms/a dtoverlay=vc4-kms-v3d,nocomposite"
