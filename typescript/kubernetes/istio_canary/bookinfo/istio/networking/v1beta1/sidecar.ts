// *** WARNING: this file was generated by crd2pulumi. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs } from "../../types";
import * as utilities from "../../utilities";

import {ObjectMeta} from "../../meta/v1";

export class Sidecar extends pulumi.CustomResource {
    /**
     * Get an existing Sidecar resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): Sidecar {
        return new Sidecar(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'kubernetes:networking.istio.io/v1beta1:Sidecar';

    /**
     * Returns true if the given object is an instance of Sidecar.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Sidecar {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Sidecar.__pulumiType;
    }

    public readonly apiVersion!: pulumi.Output<"networking.istio.io/v1beta1" | undefined>;
    public readonly kind!: pulumi.Output<"Sidecar" | undefined>;
    public readonly metadata!: pulumi.Output<ObjectMeta | undefined>;
    /**
     * Configuration affecting network reachability of a sidecar. See more details at: https://istio.io/docs/reference/config/networking/sidecar.html
     */
    public readonly spec!: pulumi.Output<outputs.networking.v1beta1.SidecarSpec | undefined>;
    public readonly status!: pulumi.Output<{[key: string]: any} | undefined>;

    /**
     * Create a Sidecar resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args?: SidecarArgs, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            inputs["apiVersion"] = "networking.istio.io/v1beta1";
            inputs["kind"] = "Sidecar";
            inputs["metadata"] = args ? args.metadata : undefined;
            inputs["spec"] = args ? args.spec : undefined;
            inputs["status"] = args ? args.status : undefined;
        } else {
            inputs["apiVersion"] = undefined /*out*/;
            inputs["kind"] = undefined /*out*/;
            inputs["metadata"] = undefined /*out*/;
            inputs["spec"] = undefined /*out*/;
            inputs["status"] = undefined /*out*/;
        }
        if (!opts.version) {
            opts = pulumi.mergeOptions(opts, { version: utilities.getVersion()});
        }
        super(Sidecar.__pulumiType, name, inputs, opts);
    }
}

/**
 * The set of arguments for constructing a Sidecar resource.
 */
export interface SidecarArgs {
    readonly apiVersion?: pulumi.Input<"networking.istio.io/v1beta1">;
    readonly kind?: pulumi.Input<"Sidecar">;
    readonly metadata?: pulumi.Input<ObjectMeta>;
    /**
     * Configuration affecting network reachability of a sidecar. See more details at: https://istio.io/docs/reference/config/networking/sidecar.html
     */
    readonly spec?: pulumi.Input<inputs.networking.v1beta1.SidecarSpecArgs>;
    readonly status?: pulumi.Input<{[key: string]: any}>;
}
