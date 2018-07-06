#! /usr/bin/env python
from __future__ import print_function

from astropy.io import fits
import numpy as np
import sys
import os

NPIX = 500


def autocorr(x):
    corr = np.correlate(x, x, mode='full')
    half = corr[corr.size/2:]
    normed = half/half[0]
    return normed


def get_pixels(n, cube):
    # TODO learn how to avoid nan pixels
    x = np.random.randint(cube.shape[1],size=n)
    y = np.random.randint(cube.shape[2],size=n)
    pix = cube[:,x,y]
    return pix

def make_acorr_stats(n,cube):
    pix = get_pixels(n,cube)
    acorr = np.array( [ autocorr(pix[:,i]) for i in range(n)])
    mean = np.nanmean(acorr,axis=0)
    std = np.nanstd(acorr,axis=0)
    return mean, std

def get_effective_ndof(cube):
    nsamples = cube.shape[0]
    mean, std = make_acorr_stats(NPIX,cube)
    # detect the first element that has correlation consistent with zero
    print(mean)
    print(std)
    print(mean-std)
    fzero = np.min(np.where(mean-std < 0))
    print(fzero)
    ndof = nsamples - 1 - fzero
    return ndof


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: {0} image_cube.fits".format(__file__))
        sys.exit(1)
    fname = sys.argv[-1]
    print("Reading cube from {0}".format(fname))
    cube = fits.open(fname)[0].data
    if len(cube.shape) != 3:
        print("{0} needs to have 3 axes, but it has {1}".format(fname,len(cube.shape)))
        sys.exit(1)
    print("Cube has shape {0}".format(cube.shape))
    print("Cube has {0} effective degrees of freedom".format(get_effective_ndof(cube)))
