#! /usr/bin/python
# -*- coding: euc-jp -*-

import os
import pickle

basedir = '/home/ftp/pub/Plamo-5.x/'
archdir = ('x86', 'x86_64')

'''
 __blockpkgs: updatepkg �ǥ��åץǡ��ȤǤ��ʤ��ѥå������ϡ��ǥե���ȤǤ�ɽ�����ʤ��褦�ˤ���
�Ȥꤢ�����оݤϼ���6�� ('aaa_base, hdsetup, etc, sysvinit, shadow, network_configs)
get_pkginfo.py �� -b ���ץ�������ꤹ��С��������碌��ɽ������롥
'''
blockpkgs = ('aaa_base', 'hdsetup', 'etc', 'sysvinit', 'shadow', 'network_configs')

'''
 __replaces: ��̾��ʬ�䡤���󤵤줿�ѥå����������פ��뤿��ˡ���ѥå�����̾�򿷥ѥå�����̾�˥ޥåפ��롥
ex:  'tamago' -> 'tamago_tsunagi', 'python' -> 'Python2', 'Python3' -> 'Python'
'''
replace_list = {'tamago':'tamago_tsunagi', 
                'Python3':'Python',
                'python':'Python2',
                'pycups2':'py2cups',
                'pycurl2':'py2curl'
                }


for arch in archdir:
    allpkgs= {}
    allpkgs['__blockpkgs'] = blockpkgs
    allpkgs['__replaces'] = replace_list
    pkg_path = basedir + arch  + "/plamo/"
    print(pkg_path)
    for root, dirs, files in os.walk(pkg_path):
        if 'old' in dirs:
            dirs.remove('old') 
        if 'NG' in dirs:
            dirs.remove('NG')  
        if '11_mate.old' in dirs:
            dirs.remove('11_mate.old')

        for j in files:
            if j.find(".txz") > 0 or j.find(".tgz") > 0:
               
                (base, vers, p_arch, tmp) = j.split("-")
                (build, ext) = tmp.split(".") 
                r_path = root.replace(basedir, "")
                data_t = (vers, p_arch, build, ext, r_path)
                allpkgs[base] = data_t

    pickle_name = "allpkgs_" + arch + ".pickle"
    with open(pickle_name, 'wb') as f:
        pickle.dump(allpkgs, f)
