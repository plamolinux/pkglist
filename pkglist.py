#! /usr/bin/python
# -*- coding: euc-jp -*-

import os
import pickle

basedir = '/home/ftp/pub/Plamo-5.x/'
archdir = ('x86', 'x86_64')

'''
 __blockpkgs: updatepkg でアップデートできないパッケージは，デフォルトでは表示しないようにする
とりあえず対象は次の6つ ('aaa_base, hdsetup, etc, sysvinit, shadow, network_configs)
get_pkginfo.py で -b オプションを指定すれば，これらも合わせて表示される．
'''
blockpkgs = ('aaa_base', 'hdsetup', 'etc', 'sysvinit', 'shadow', 'network_configs')

'''
 __replaces: 改名，分割，集約されたパッケージを追跡するために，旧パッケージ名を新パッケージ名にマップする．
ex:  'tamago' -> 'tamago_tsunagi', 'python' -> 'Python2', 'Python3' -> 'Python'
分割されたパッケージを追跡するために、新パッケージ名はタプルにして一対多の対応を可能にしたが、
カテゴリごとに新パッケージを表示する機能を追加したので一対多のマッピングは不要になったものの、
新パッケージ名のリストはタプルのままなので，要素が一つだけでも末尾に","を付ける必要あり．

旧仕様:
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
