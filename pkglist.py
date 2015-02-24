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
ʬ�䤵�줿�ѥå����������פ��뤿��ˡ����ѥå�����̾�ϥ��ץ�ˤ��ư���¿���б����ǽ�ˤ�������
���ƥ��ꤴ�Ȥ˿��ѥå�������ɽ�����뵡ǽ���ɲä����Τǰ���¿�Υޥåԥ󥰤����פˤʤä���ΤΡ�
���ѥå�����̾�Υꥹ�Ȥϥ��ץ�ΤޤޤʤΤǡ����Ǥ���Ĥ����Ǥ�������","���դ���ɬ�פ��ꡥ

�����:
replace_list = {'tamago':('20110401', ('tamago_tsunagi',)), 
                'emacs':('24.2', ('emacs_mini', 'emacs_bin', 'emacs_lib', 'emacs')), 
                'Python3':('3.3.2', ('Python',)), 
                'python':('2.7.3', ('Python2',)), 
                'pycups2':('1.9.70', ('py2cups',)), 
                'pycurl2':('7.19.5',('py2curl',)),
		'python_setuptools':('0.6c11',('python_setuptools', 'python2_setuptools')),
                'xfwm4_themes':('4.6.0',('xfwm4_themes', 'xfce_theme_albatross', 'xfce_theme_greybird', 'xfce_theme_numix', 'xfce_theme_orion')),
               }
'''
replace_list = {'tamago':'tamago_tsunagi', 
                'Python3':'Python',
                'python':'Python2',
                'pycups2':'py2cups',
                'pycurl2':'py2curl'
                }

#allpkgs['__replaces'] = replace_list

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
                r_path = root.replace("/home/ftp/pub/Plamo-5.x/", "")
                data_t = (vers, p_arch, build, ext, r_path)
                allpkgs[base] = data_t

    pickle_name = "allpkgs_" + arch + ".pickle"
    with open(pickle_name, 'wb') as f:
        pickle.dump(allpkgs, f)
