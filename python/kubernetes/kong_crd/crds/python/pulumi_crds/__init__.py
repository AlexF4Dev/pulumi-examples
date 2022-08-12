# coding=utf-8
# *** WARNING: this file was generated by crd2pulumi. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from . import _utilities
import typing
# Export this package's modules as members:
from .provider import *

# Make subpackages available:
if typing.TYPE_CHECKING:
    import pulumi_crds.configuration as __configuration
    configuration = __configuration
    import pulumi_crds.meta as __meta
    meta = __meta
else:
    configuration = _utilities.lazy_import('pulumi_crds.configuration')
    meta = _utilities.lazy_import('pulumi_crds.meta')

_utilities.register(
    resource_modules="""
[
 {
  "pkg": "crds",
  "mod": "configuration.konghq.com/v1",
  "fqn": "pulumi_crds.configuration.v1",
  "classes": {
   "kubernetes:configuration.konghq.com/v1:KongClusterPlugin": "KongClusterPlugin"
  }
 }
]
""",
    resource_packages="""
[
 {
  "pkg": "crds",
  "token": "pulumi:providers:crds",
  "fqn": "pulumi_crds",
  "class": "Provider"
 }
]
"""
)
