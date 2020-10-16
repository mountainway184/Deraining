{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Untitled19.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyPY9FM3dpukgutjWM5SKwbl",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/mountainway184/Deraining/blob/master/Untitled20.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "X0RpJiuOh0VK"
      },
      "source": [
        "def FReLU(inputs,num_channels):\n",
        "  x = DepthwiseConv2D(kernel_size=3, strides=1, padding='same')(inputs)\n",
        "  return K.maximum(x,inputs)\n",
        "\n",
        "def Generator(input_size = (batch_size,None,None,img_channels)):\n",
        "    inputs = Input(batch_shape = (None,None,None,img_channels))\n",
        "\n",
        "    conv1 = Conv2D(64, (3, 3), padding='same')(inputs)\n",
        "    conv1 = FReLU(conv1,64)\n",
        "    conv1 = Conv2D(64, (3, 3), padding='same')(conv1)\n",
        "    conv1 = FReLU(conv1,64)\n",
        "    pool1 = MaxPooling2D(pool_size=(2, 2))(conv1)\n",
        "\n",
        "    conv2 = Conv2D(128, (3, 3),padding='same')(pool1)\n",
        "    conv2 = FReLU(conv2,128)\n",
        "    conv2 = Conv2D(128, (3, 3),padding='same')(conv2)\n",
        "    conv2 = FReLU(conv2,128)\n",
        "    pool2 = MaxPooling2D(pool_size=(2, 2))(conv2)\n",
        "\n",
        "    conv3 = Conv2D(256, (3, 3),padding='same')(pool2)\n",
        "    conv3 = FReLU(conv3,256)\n",
        "    conv3 = Conv2D(256, (3, 3),padding='same')(conv3)\n",
        "    conv3 = FReLU(conv3,256)\n",
        "    pool3 = MaxPooling2D(pool_size=(2, 2))(conv3)\n",
        "\n",
        "    conv4 = Conv2D(512, (3, 3),padding='same')(pool3)\n",
        "    conv4 = FReLU(conv4,512)\n",
        "    conv4 = Conv2D(512, (3, 3),padding='same')(conv4)\n",
        "    conv4 = FReLU(conv4,512)\n",
        "\n",
        "    up5 = Conv2DTranspose(256, (2, 2), strides=(2, 2), padding='same')(conv4)\n",
        "    up5 = FReLU(up5,256)\n",
        "    up5 = concatenate([up5, conv3], axis=3)\n",
        "    \n",
        "    conv6 = Conv2D(256, (3, 3), padding='same')(up5)\n",
        "    conv6 = FReLU(conv6,256)\n",
        "    conv6 = Conv2D(256, (3, 3),padding='same')(conv6)\n",
        "    conv6 = FReLU(conv6,256)\n",
        "\n",
        "    up7 = Conv2DTranspose(128, (2, 2), strides=(2, 2), padding='same')(conv6)\n",
        "    up7 = FReLU(up7,128)\n",
        "    up7 = concatenate([up7, conv2], axis=3) \n",
        "\n",
        "    conv8 = Conv2D(128, (3, 3), padding='same')(up7)\n",
        "    conv8 = FReLU(conv8,128)\n",
        "    conv8 = Conv2D(128, (3, 3),padding='same')(conv8)\n",
        "    conv8 = FReLU(conv8,128)       \n",
        "\n",
        "    up9 = Conv2DTranspose(64, (2, 2), strides=(2, 2), padding='same')(conv8)\n",
        "    up9 = FReLU(up9,64)\n",
        "    up9 = concatenate([up9, conv1], axis=3)     \n",
        "\n",
        "    conv10 = Conv2D(64, (3, 3), padding='same')(up9)\n",
        "    conv10 = FReLU(conv10,64)\n",
        "    conv10 = Conv2D(64, (3, 3),padding='same')(conv10)\n",
        "    conv10 = FReLU(conv10,64)     \n",
        "\n",
        "    conv11 = Conv2D(3,(3, 3),activation = 'sigmoid', padding='same')(conv10)\n",
        "\n",
        "    model = Model(inputs=[inputs], outputs=[conv11])\n",
        "    return model"
      ],
      "execution_count": null,
      "outputs": []
    }
  ]
}