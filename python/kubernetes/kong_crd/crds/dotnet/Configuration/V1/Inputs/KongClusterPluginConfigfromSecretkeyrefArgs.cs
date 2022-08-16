// *** WARNING: this file was generated by crd2pulumi. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Kubernetes.Types.Inputs.Configuration.V1
{

    /// <summary>
    /// NamespacedSecretValueFromSource represents the source of a secret value specifying the secret namespace
    /// </summary>
    public class KongClusterPluginConfigfromSecretkeyrefArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// the key containing the value
        /// </summary>
        [Input("key", required: true)]
        public Input<string> Key { get; set; } = null!;

        /// <summary>
        /// the secret containing the key
        /// </summary>
        [Input("name", required: true)]
        public Input<string> Name { get; set; } = null!;

        /// <summary>
        /// The namespace containing the secret
        /// </summary>
        [Input("namespace", required: true)]
        public Input<string> Namespace { get; set; } = null!;

        public KongClusterPluginConfigfromSecretkeyrefArgs()
        {
        }
    }
}