"""

import sys
import os

sys.path.append(os.path.abspath('waf/waflib/extras')) # for boost

def options(opt):
    opt.load('cxx boost')
    opt.load('ogre3d', tooldir='.')
    
def configure(conf):
    conf.load('cxx boost')
    conf.load('ogre3d', tooldir='.')

def build(bld):
    tg = bld.program(
       features='cxx',
       source='src/BaseApplication.cpp src/TutorialApplication.cpp',
       target='TutorialApplication',
       use='BOOST OGRE'
    )
    
waf\waf configure^
  --boost-include=D:\boost_1_57_0^
  --boost-lib=D:\boost_1_57_0\lib32-msvc-11.0^
  --boost-mt^
  --ogre-lib=%CD%\OgreSDK\lib\Release^
  --ogre-include=%CD%\OgreSDK\include
        
"""

import os

OGRE_LIBS = [
    "cg",
    "FreeImage",
    "freetype",
    "OgreMain",
    "OgreOverlay",
    "OgrePaging",
    "OgreProperty",
    "OgreRTShaderSystem",
    "OgreTerrain",
    "OgreVolume",
    "OIS",
    "zlib",
    "zziplib"
]

OGRE_LIBS_DEBUG = ["%s_d" % l for l in OGRE_LIBS]

OGRE_INCLUDE = [
    "Cg",
    "freetype",
    "OGRE",
    "OIS",
    "zzip",
    "freetype/config",
    "freetype/internal",
    "freetype/internal/services",
    "OGRE/Overlay",
    "OGRE/Paging",
    "OGRE/Plugins",
    "OGRE/Property",
    "OGRE/RenderSystems",
    "OGRE/RTShaderSystem",
    "OGRE/Terrain",
    "OGRE/Threading",
    "OGRE/Volume",
    "OGRE/WIN32",
    "OGRE/Plugins/BSPSceneManager",
    "OGRE/Plugins/CgProgramManager",
    "OGRE/Plugins/OctreeSceneManager",
    "OGRE/Plugins/OctreeZone",
    "OGRE/Plugins/ParticleFX",
    "OGRE/Plugins/PCZSceneManager",
    "OGRE/RenderSystems/Direct3D11",
    "OGRE/RenderSystems/Direct3D9",
    "OGRE/RenderSystems/GL",
    "OGRE/RenderSystems/GL/GL",
    "OIS/win32"
]

def options(opt):
    opt.add_option('--ogre-lib', dest='ogre_lib', action='store',
        default=False, help='Path to ogre libs')
    opt.add_option('--ogre-include', dest='ogre_include', action='store',
        default=False, help='Path to ogre includes')
                        
def configure(conf):
    conf.env.LIB_OGRE = OGRE_LIBS
    conf.env.LIBPATH_OGRE = conf.options.ogre_lib
    conf.env.INCLUDES_OGRE = [os.path.join(conf.options.ogre_include, i) for i in OGRE_INCLUDE]
    
    OGRE_RESOURCEPATH = (os.sep*2).join(conf.options.ogre_lib.split(os.sep)[:-2]+['bin', 'Release'])+(os.sep*2)
    
    resources = conf.path.make_node('build/resources.cfg')
    with open('%sresources.cfg' % OGRE_RESOURCEPATH, 'r') as f:
        out = ""
        for l in f.read().splitlines():
            out = out + l.replace('../../', '../OgreSDK/')+'\n'
        resources.write(out)
        
    plugins = conf.path.make_node('build/plugins.cfg')
    with open('%splugins.cfg' % OGRE_RESOURCEPATH, 'r') as f:
        out = ""
        for l in f.read().splitlines():
            out = out + l.replace('PluginFolder=.', 'PluginFolder=../OgreSDK/bin/Release')+'\n'
        plugins.write(out)