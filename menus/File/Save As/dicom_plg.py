# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 03:52:48 2016

@author: yxl
"""

from scipy.misc import imsave
from core.engine import Simple
import wx, IPy

class Plugin(Simple):
    title = 'DICOM'
    note = ['all']
    
    #parameter
    para = {'path':'./'}
    
    def show(self):
        IPy.alert('un implement!')
        return None

    #process
    def run(self, ips, img, para = None):
        imsave(para['path'], ips.get_img())