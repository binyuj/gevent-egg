def __bootstrap__():
   global __bootstrap__, __loader__, __file__
   import sys, pkg_resources, imp, platform
   __file__ = pkg_resources.resource_filename(__name__,'_util-py%s-%s-%s-%s.%s' % (sys.version[:3],sys.platform,('ucs2','ucs4')[sys.maxunicode>2**32],('i686','x86_64')[sys.maxint>2**32],imp.get_suffixes()[0][0].split('.')[-1]))
   __loader__ = None; del __bootstrap__, __loader__
   imp.load_dynamic(__name__,__file__)
__bootstrap__()
