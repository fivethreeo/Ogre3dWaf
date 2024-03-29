import sys
import os
sys.path.append(os.path.abspath('waf/waflib/extras'))

def options(opt):
    opt.load('cxx msvc boost')
    opt.load('ogre3d', tooldir='.')
    
def configure(conf):
    conf.load('cxx msvc boost')
    conf.load('ogre3d', tooldir='.')
    
    conf.env['MSVC_TARGETS'] = ['x86']
    
    LIB_MSVC = 'kernel32 user32 gdi32 oleaut32 ole32 comctl32 vfw32 ws2_32 advapi32'
    conf.env.LIB_MSVC = LIB_MSVC.split(" ")
    conf.check_libs_msvc(LIB_MSVC)
    
    conf.check_boost(stlib='thread system filesystem')

    conf.env.INCLUDES += [os.path.abspath('include')]
    
    conf.env.CXXFLAGS = '/EHsc'
    
def build(bld):

    tg = bld.program(
       features='cxx',
       source='src/BaseApplication.cpp src/TutorialApplication.cpp',
       target='TutorialApplication',
       use='MSVC BOOST OGRE'
    )