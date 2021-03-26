# Chaotic Encryption
This repository contains the code for encrypting an image using various techniques written completely in python.

## Chaotic systems used
### 1. Logistic map equation
### 2. Lorenz system of differential equations

## Encryption methods used
### 1. Only substitution (Confusion method)
Here, the code substitutes every pixel of the image with another pixel (which is obtained be XORing the initial pixel's value with a pseudo-random number (different for every pixel) generated using one of the above mentioned PRNG) thus making the encryption very secure.
### 2. Shuffling and then Substitution (Diffusion then Confusion method)
Here the code first shuffles the pixels of an image using random numbers (one for every pixel) generated using one of the PRNG and then it performs the above described substitution method with another set of keys. Thus this encryption approach is very secure.
