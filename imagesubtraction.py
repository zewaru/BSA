import math
import pyfits
import astropy
from astropy.io.fits import getheader
from astropy import wcs
from matplotlib import pyplot as plt
import numpy
import scipy
from scipy import misc


class Fitsfile:

    def __init__(self, inputfilename):
        self.inputfilename = inputfilename
        self.filein = pyfits.open(self.inputfilename)
        self.datain = self.filein[0].data
        self.header = getheader(self.inputfilename)
        self.w = wcs.WCS(self.header)

    def get_header(self):
        return self.header

    def get_data(self):
        return self.datain

    def get_wcs(self):
        return self.w

    def save_image(self, outputfilename):
        scipy.misc.imsave(outputfilename, self.datain)
        print "OK"
        return

firstfile = Fitsfile("test.fits")

firstfile.save_image("test_out.jpg")




#
#
#
#
# def trunc(item,n):
#     if type(item) is float:
#         slen = len('%.*f' %(n, item)) #rounds coordinate to n decimals, measures length
#         stritem = str(item)[:slen] # truncates coordinate so that n decimals are included
#         return float(stritem)
#     elif type(item) is str:
#         return str(item)[:n] # truncates coord to length n
#
# def angulardistance(x, y, a, b):
#     return math.sin(math.radians(y)) * math.sin(math.radians(b)) + math.cos(math.radians(y)) * math.cos(math.radians(b)) * math.cos(math.radians(a-x))
#
#
#
#
#
#
#
#
#
# filein1 = pyfits.open("test.fits")
# filein2 = pyfits.open("test2.fits")
#
# header1 = getheader("test1.fits")
# header2 = getheader("test2.fits")
#
# datain1 = filein1[0].data
# datain2 = filein2[0].data
#
# w1 = wcs.WCS(header1)
# w2 = wcs.WCS(header2)
#
# countsarray1 = numpy.reshape(datain1, 16646400)
#
# countslist1 = countsarray1.tolist()
#
#
# countsarray2 = numpy.reshape(datain2, 16646400)
#
# countslist2 = countsarray2.tolist()
#
# for i in range(0, datain1):
#     for j in range(0, datain1[i]):
#         pixel2world1 = [w1.wcs_pix2world(i,j)]
#
# for i in range(0, datain2):
#     for j in range(0, datain2[i]):
#         pixel2world2 = [w2.wcs_pix2world(i,j)]
#
#
#
