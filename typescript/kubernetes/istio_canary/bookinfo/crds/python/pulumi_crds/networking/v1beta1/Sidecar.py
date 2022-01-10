# coding=utf-8
# *** WARNING: this file was generated by crd2pulumi. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from . import outputs
from ._inputs import *
from pulumi_kubernetes import meta_v1 as _meta_v1

__all__ = ['SidecarArgs', 'Sidecar']

@pulumi.input_type
class SidecarArgs:
    def __init__(__self__, *,
                 api_version: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 metadata: Optional[pulumi.Input['_meta_v1.ObjectMetaArgs']] = None,
                 spec: Optional[pulumi.Input['SidecarSpecArgs']] = None,
                 status: Optional[pulumi.Input[Mapping[str, Any]]] = None):
        """
        The set of arguments for constructing a Sidecar resource.
        :param pulumi.Input['SidecarSpecArgs'] spec: Configuration affecting network reachability of a sidecar. See more details at: https://istio.io/docs/reference/config/networking/sidecar.html
        """
        if api_version is not None:
            pulumi.set(__self__, "api_version", 'networking.istio.io/v1beta1')
        if kind is not None:
            pulumi.set(__self__, "kind", 'Sidecar')
        if metadata is not None:
            pulumi.set(__self__, "metadata", metadata)
        if spec is not None:
            pulumi.set(__self__, "spec", spec)
        if status is not None:
            pulumi.set(__self__, "status", status)

    @property
    @pulumi.getter(name="apiVersion")
    def api_version(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "api_version")

    @api_version.setter
    def api_version(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "api_version", value)

    @property
    @pulumi.getter
    def kind(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "kind")

    @kind.setter
    def kind(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "kind", value)

    @property
    @pulumi.getter
    def metadata(self) -> Optional[pulumi.Input['_meta_v1.ObjectMetaArgs']]:
        return pulumi.get(self, "metadata")

    @metadata.setter
    def metadata(self, value: Optional[pulumi.Input['_meta_v1.ObjectMetaArgs']]):
        pulumi.set(self, "metadata", value)

    @property
    @pulumi.getter
    def spec(self) -> Optional[pulumi.Input['SidecarSpecArgs']]:
        """
        Configuration affecting network reachability of a sidecar. See more details at: https://istio.io/docs/reference/config/networking/sidecar.html
        """
        return pulumi.get(self, "spec")

    @spec.setter
    def spec(self, value: Optional[pulumi.Input['SidecarSpecArgs']]):
        pulumi.set(self, "spec", value)

    @property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "status", value)


class Sidecar(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 api_version: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 metadata: Optional[pulumi.Input[pulumi.InputType['_meta_v1.ObjectMetaArgs']]] = None,
                 spec: Optional[pulumi.Input[pulumi.InputType['SidecarSpecArgs']]] = None,
                 status: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 __props__=None):
        """
        Create a Sidecar resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['SidecarSpecArgs']] spec: Configuration affecting network reachability of a sidecar. See more details at: https://istio.io/docs/reference/config/networking/sidecar.html
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[SidecarArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a Sidecar resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param SidecarArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SidecarArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 api_version: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 metadata: Optional[pulumi.Input[pulumi.InputType['_meta_v1.ObjectMetaArgs']]] = None,
                 spec: Optional[pulumi.Input[pulumi.InputType['SidecarSpecArgs']]] = None,
                 status: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 __props__=None):
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = SidecarArgs.__new__(SidecarArgs)

            __props__.__dict__["api_version"] = 'networking.istio.io/v1beta1'
            __props__.__dict__["kind"] = 'Sidecar'
            __props__.__dict__["metadata"] = metadata
            __props__.__dict__["spec"] = spec
            __props__.__dict__["status"] = status
        super(Sidecar, __self__).__init__(
            'kubernetes:networking.istio.io/v1beta1:Sidecar',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Sidecar':
        """
        Get an existing Sidecar resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = SidecarArgs.__new__(SidecarArgs)

        __props__.__dict__["api_version"] = None
        __props__.__dict__["kind"] = None
        __props__.__dict__["metadata"] = None
        __props__.__dict__["spec"] = None
        __props__.__dict__["status"] = None
        return Sidecar(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="apiVersion")
    def api_version(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "api_version")

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def metadata(self) -> pulumi.Output[Optional['_meta_v1.outputs.ObjectMeta']]:
        return pulumi.get(self, "metadata")

    @property
    @pulumi.getter
    def spec(self) -> pulumi.Output[Optional['outputs.SidecarSpec']]:
        """
        Configuration affecting network reachability of a sidecar. See more details at: https://istio.io/docs/reference/config/networking/sidecar.html
        """
        return pulumi.get(self, "spec")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[Optional[Mapping[str, Any]]]:
        return pulumi.get(self, "status")

