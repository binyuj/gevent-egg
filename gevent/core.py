def __bootstrap__():
   global __bootstrap__, __loader__, __file__
   import sys, pkg_resources, imp, platform
   __file__ = pkg_resources.resource_filename(__name__,'core-py%s-%s-%s%s' % (sys.version[:3],sys.platform,platform.machine(),imp.get_suffixes()[0][0]))
   __loader__ = None; del __bootstrap__, __loader__
   imp.load_dynamic(__name__,__file__)
__bootstrap__()
