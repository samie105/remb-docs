---
title: "GPU - Web documentation"
source: "https://docs.deno.com/api/web/gpu"
canonical_url: "https://docs.deno.com/api/web/gpu"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T17:13:25.628Z"
content_hash: "27d865f61f51d235ec9aa85bec8920470c682807616c8b0d8b19d61445ae6a01"
menu_path: ["GPU - Web documentation"]
section_path: []
nav_prev: {"path": "deno/deno/api/web/file/index.md", "title": "File - Web documentation"}
nav_next: {"path": "deno/deno/api/web/intl/index.md", "title": "Intl - Web documentation"}
---

### Classes [#](#Classes)

c

[GPU](./././~/GPU "GPU")

The entry point to WebGPU in Deno, accessed via the global navigator.gpu property.

*   [getPreferredCanvasFormat](./././~/GPU#method_getpreferredcanvasformat_0)
*   [requestAdapter](./././~/GPU#method_requestadapter_0)

c

[GPUAdapter](./././~/GPUAdapter "GPUAdapter")

Represents a physical GPU device that can be used to create a logical GPU device.

*   [features](./././~/GPUAdapter#property_features)
*   [info](./././~/GPUAdapter#property_info)
*   [limits](./././~/GPUAdapter#property_limits)
*   [requestDevice](./././~/GPUAdapter#method_requestdevice_0)

c

[GPUAdapterInfo](./././~/GPUAdapterInfo "GPUAdapterInfo")

No documentation available

*   [architecture](./././~/GPUAdapterInfo#property_architecture)
*   [description](./././~/GPUAdapterInfo#property_description)
*   [device](./././~/GPUAdapterInfo#property_device)
*   [isFallbackAdapter](./././~/GPUAdapterInfo#property_isfallbackadapter)
*   [subgroupMaxSize](./././~/GPUAdapterInfo#property_subgroupmaxsize)
*   [subgroupMinSize](./././~/GPUAdapterInfo#property_subgroupminsize)
*   [vendor](./././~/GPUAdapterInfo#property_vendor)

c

[GPUBindGroup](./././~/GPUBindGroup "GPUBindGroup")

No documentation available

*   [label](./././~/GPUBindGroup#property_label)

c

[GPUBindGroupLayout](./././~/GPUBindGroupLayout "GPUBindGroupLayout")

No documentation available

*   [label](./././~/GPUBindGroupLayout#property_label)

c

[GPUBuffer](./././~/GPUBuffer "GPUBuffer")

Represents a block of memory allocated on the GPU.

*   [destroy](./././~/GPUBuffer#method_destroy_0)
*   [getMappedRange](./././~/GPUBuffer#method_getmappedrange_0)
*   [label](./././~/GPUBuffer#property_label)
*   [mapAsync](./././~/GPUBuffer#method_mapasync_0)
*   [mapState](./././~/GPUBuffer#property_mapstate)
*   [size](./././~/GPUBuffer#property_size)
*   [unmap](./././~/GPUBuffer#method_unmap_0)
*   [usage](./././~/GPUBuffer#property_usage)

c

[GPUBufferUsage](./././~/GPUBufferUsage "GPUBufferUsage")

No documentation available

*   [COPY\_DST](./././~/GPUBufferUsage#property_copy_dst)
*   [COPY\_SRC](./././~/GPUBufferUsage#property_copy_src)
*   [INDEX](./././~/GPUBufferUsage#property_index)
*   [INDIRECT](./././~/GPUBufferUsage#property_indirect)
*   [MAP\_READ](./././~/GPUBufferUsage#property_map_read)
*   [MAP\_WRITE](./././~/GPUBufferUsage#property_map_write)
*   [QUERY\_RESOLVE](./././~/GPUBufferUsage#property_query_resolve)
*   [STORAGE](./././~/GPUBufferUsage#property_storage)
*   [UNIFORM](./././~/GPUBufferUsage#property_uniform)
*   [VERTEX](./././~/GPUBufferUsage#property_vertex)

c

[GPUColorWrite](./././~/GPUColorWrite "GPUColorWrite")

No documentation available

*   [ALL](./././~/GPUColorWrite#property_all)
*   [ALPHA](./././~/GPUColorWrite#property_alpha)
*   [BLUE](./././~/GPUColorWrite#property_blue)
*   [GREEN](./././~/GPUColorWrite#property_green)
*   [RED](./././~/GPUColorWrite#property_red)

c

[GPUCommandBuffer](./././~/GPUCommandBuffer "GPUCommandBuffer")

No documentation available

*   [label](./././~/GPUCommandBuffer#property_label)

c

[GPUCommandEncoder](./././~/GPUCommandEncoder "GPUCommandEncoder")

Used to record GPU commands for later execution by the GPU.

*   [beginComputePass](./././~/GPUCommandEncoder#method_begincomputepass_0)
*   [beginRenderPass](./././~/GPUCommandEncoder#method_beginrenderpass_0)
*   [clearBuffer](./././~/GPUCommandEncoder#method_clearbuffer_0)
*   [copyBufferToBuffer](./././~/GPUCommandEncoder#method_copybuffertobuffer_0)
*   [copyBufferToTexture](./././~/GPUCommandEncoder#method_copybuffertotexture_0)
*   [copyTextureToBuffer](./././~/GPUCommandEncoder#method_copytexturetobuffer_0)
*   [copyTextureToTexture](./././~/GPUCommandEncoder#method_copytexturetotexture_0)
*   [finish](./././~/GPUCommandEncoder#method_finish_0)
*   [insertDebugMarker](./././~/GPUCommandEncoder#method_insertdebugmarker_0)
*   [label](./././~/GPUCommandEncoder#property_label)
*   [popDebugGroup](./././~/GPUCommandEncoder#method_popdebuggroup_0)
*   [pushDebugGroup](./././~/GPUCommandEncoder#method_pushdebuggroup_0)
*   [resolveQuerySet](./././~/GPUCommandEncoder#method_resolvequeryset_0)
*   [writeTimestamp](./././~/GPUCommandEncoder#method_writetimestamp_0)

c

[GPUCompilationInfo](./././~/GPUCompilationInfo "GPUCompilationInfo")

No documentation available

*   [messages](./././~/GPUCompilationInfo#property_messages)

c

[GPUCompilationMessage](./././~/GPUCompilationMessage "GPUCompilationMessage")

No documentation available

*   [length](./././~/GPUCompilationMessage#property_length)
*   [lineNum](./././~/GPUCompilationMessage#property_linenum)
*   [linePos](./././~/GPUCompilationMessage#property_linepos)
*   [message](./././~/GPUCompilationMessage#property_message)
*   [offset](./././~/GPUCompilationMessage#property_offset)
*   [type](./././~/GPUCompilationMessage#property_type)

c

[GPUComputePassEncoder](./././~/GPUComputePassEncoder "GPUComputePassEncoder")

No documentation available

*   [dispatchWorkgroups](./././~/GPUComputePassEncoder#method_dispatchworkgroups_0)
*   [dispatchWorkgroupsIndirect](./././~/GPUComputePassEncoder#method_dispatchworkgroupsindirect_0)
*   [end](./././~/GPUComputePassEncoder#method_end_0)
*   [insertDebugMarker](./././~/GPUComputePassEncoder#method_insertdebugmarker_0)
*   [label](./././~/GPUComputePassEncoder#property_label)
*   [popDebugGroup](./././~/GPUComputePassEncoder#method_popdebuggroup_0)
*   [pushDebugGroup](./././~/GPUComputePassEncoder#method_pushdebuggroup_0)
*   [setBindGroup](./././~/GPUComputePassEncoder#method_setbindgroup_0)
*   [setPipeline](./././~/GPUComputePassEncoder#method_setpipeline_0)

c

[GPUComputePipeline](./././~/GPUComputePipeline "GPUComputePipeline")

No documentation available

*   [getBindGroupLayout](./././~/GPUComputePipeline#method_getbindgrouplayout_0)
*   [label](./././~/GPUComputePipeline#property_label)

c

[GPUDevice](./././~/GPUDevice "GPUDevice")

The primary interface for interacting with a WebGPU device.

*   [adapterInfo](./././~/GPUDevice#property_adapterinfo)
*   [createBindGroup](./././~/GPUDevice#method_createbindgroup_0)
*   [createBindGroupLayout](./././~/GPUDevice#method_createbindgrouplayout_0)
*   [createBuffer](./././~/GPUDevice#method_createbuffer_0)
*   [createCommandEncoder](./././~/GPUDevice#method_createcommandencoder_0)
*   [createComputePipeline](./././~/GPUDevice#method_createcomputepipeline_0)
*   [createComputePipelineAsync](./././~/GPUDevice#method_createcomputepipelineasync_0)
*   [createPipelineLayout](./././~/GPUDevice#method_createpipelinelayout_0)
*   [createQuerySet](./././~/GPUDevice#method_createqueryset_0)
*   [createRenderBundleEncoder](./././~/GPUDevice#method_createrenderbundleencoder_0)
*   [createRenderPipeline](./././~/GPUDevice#method_createrenderpipeline_0)
*   [createRenderPipelineAsync](./././~/GPUDevice#method_createrenderpipelineasync_0)
*   [createSampler](./././~/GPUDevice#method_createsampler_0)
*   [createShaderModule](./././~/GPUDevice#method_createshadermodule_0)
*   [createTexture](./././~/GPUDevice#method_createtexture_0)
*   [destroy](./././~/GPUDevice#method_destroy_0)
*   [features](./././~/GPUDevice#property_features)
*   [label](./././~/GPUDevice#property_label)
*   [limits](./././~/GPUDevice#property_limits)
*   [lost](./././~/GPUDevice#property_lost)
*   [popErrorScope](./././~/GPUDevice#method_poperrorscope_0)
*   [pushErrorScope](./././~/GPUDevice#method_pusherrorscope_0)
*   [queue](./././~/GPUDevice#property_queue)

c

[GPUMapMode](./././~/GPUMapMode "GPUMapMode")

No documentation available

*   [READ](./././~/GPUMapMode#property_read)
*   [WRITE](./././~/GPUMapMode#property_write)

c

[GPUPipelineLayout](./././~/GPUPipelineLayout "GPUPipelineLayout")

No documentation available

*   [label](./././~/GPUPipelineLayout#property_label)

c

[GPUQuerySet](./././~/GPUQuerySet "GPUQuerySet")

No documentation available

*   [count](./././~/GPUQuerySet#property_count)
*   [destroy](./././~/GPUQuerySet#method_destroy_0)
*   [label](./././~/GPUQuerySet#property_label)
*   [type](./././~/GPUQuerySet#property_type)

c

[GPUQueue](./././~/GPUQueue "GPUQueue")

Represents a queue to submit commands to the GPU.

*   [label](./././~/GPUQueue#property_label)
*   [onSubmittedWorkDone](./././~/GPUQueue#method_onsubmittedworkdone_0)
*   [submit](./././~/GPUQueue#method_submit_0)
*   [writeBuffer](./././~/GPUQueue#method_writebuffer_0)
*   [writeTexture](./././~/GPUQueue#method_writetexture_0)

c

[GPURenderBundle](./././~/GPURenderBundle "GPURenderBundle")

No documentation available

*   [label](./././~/GPURenderBundle#property_label)

c

[GPURenderBundleEncoder](./././~/GPURenderBundleEncoder "GPURenderBundleEncoder")

No documentation available

*   [draw](./././~/GPURenderBundleEncoder#method_draw_0)
*   [drawIndexed](./././~/GPURenderBundleEncoder#method_drawindexed_0)
*   [drawIndexedIndirect](./././~/GPURenderBundleEncoder#method_drawindexedindirect_0)
*   [drawIndirect](./././~/GPURenderBundleEncoder#method_drawindirect_0)
*   [finish](./././~/GPURenderBundleEncoder#method_finish_0)
*   [insertDebugMarker](./././~/GPURenderBundleEncoder#method_insertdebugmarker_0)
*   [label](./././~/GPURenderBundleEncoder#property_label)
*   [popDebugGroup](./././~/GPURenderBundleEncoder#method_popdebuggroup_0)
*   [pushDebugGroup](./././~/GPURenderBundleEncoder#method_pushdebuggroup_0)
*   [setBindGroup](./././~/GPURenderBundleEncoder#method_setbindgroup_0)
*   [setIndexBuffer](./././~/GPURenderBundleEncoder#method_setindexbuffer_0)
*   [setPipeline](./././~/GPURenderBundleEncoder#method_setpipeline_0)
*   [setVertexBuffer](./././~/GPURenderBundleEncoder#method_setvertexbuffer_0)

c

[GPURenderPassEncoder](./././~/GPURenderPassEncoder "GPURenderPassEncoder")

No documentation available

*   [beginOcclusionQuery](./././~/GPURenderPassEncoder#method_beginocclusionquery_0)
*   [draw](./././~/GPURenderPassEncoder#method_draw_0)
*   [drawIndexed](./././~/GPURenderPassEncoder#method_drawindexed_0)
*   [drawIndexedIndirect](./././~/GPURenderPassEncoder#method_drawindexedindirect_0)
*   [drawIndirect](./././~/GPURenderPassEncoder#method_drawindirect_0)
*   [end](./././~/GPURenderPassEncoder#method_end_0)
*   [endOcclusionQuery](./././~/GPURenderPassEncoder#method_endocclusionquery_0)
*   [executeBundles](./././~/GPURenderPassEncoder#method_executebundles_0)
*   [insertDebugMarker](./././~/GPURenderPassEncoder#method_insertdebugmarker_0)
*   [label](./././~/GPURenderPassEncoder#property_label)
*   [popDebugGroup](./././~/GPURenderPassEncoder#method_popdebuggroup_0)
*   [pushDebugGroup](./././~/GPURenderPassEncoder#method_pushdebuggroup_0)
*   [setBindGroup](./././~/GPURenderPassEncoder#method_setbindgroup_0)
*   [setBlendConstant](./././~/GPURenderPassEncoder#method_setblendconstant_0)
*   [setIndexBuffer](./././~/GPURenderPassEncoder#method_setindexbuffer_0)
*   [setPipeline](./././~/GPURenderPassEncoder#method_setpipeline_0)
*   [setScissorRect](./././~/GPURenderPassEncoder#method_setscissorrect_0)
*   [setStencilReference](./././~/GPURenderPassEncoder#method_setstencilreference_0)
*   [setVertexBuffer](./././~/GPURenderPassEncoder#method_setvertexbuffer_0)
*   [setViewport](./././~/GPURenderPassEncoder#method_setviewport_0)

c

[GPURenderPipeline](./././~/GPURenderPipeline "GPURenderPipeline")

No documentation available

*   [getBindGroupLayout](./././~/GPURenderPipeline#method_getbindgrouplayout_0)
*   [label](./././~/GPURenderPipeline#property_label)

c

[GPUSampler](./././~/GPUSampler "GPUSampler")

No documentation available

*   [label](./././~/GPUSampler#property_label)

c

[GPUShaderModule](./././~/GPUShaderModule "GPUShaderModule")

Represents a compiled shader module that can be used to create graphics or compute pipelines.

*   [getCompilationInfo](./././~/GPUShaderModule#method_getcompilationinfo_0)
*   [label](./././~/GPUShaderModule#property_label)

c

[GPUShaderStage](./././~/GPUShaderStage "GPUShaderStage")

No documentation available

*   [COMPUTE](./././~/GPUShaderStage#property_compute)
*   [FRAGMENT](./././~/GPUShaderStage#property_fragment)
*   [VERTEX](./././~/GPUShaderStage#property_vertex)

c

[GPUSupportedFeatures](./././~/GPUSupportedFeatures "GPUSupportedFeatures")

No documentation available

*   [entries](./././~/GPUSupportedFeatures#method_entries_0)
*   [forEach](./././~/GPUSupportedFeatures#method_foreach_0)
*   [has](./././~/GPUSupportedFeatures#method_has_0)
*   [keys](./././~/GPUSupportedFeatures#method_keys_0)
*   [size](./././~/GPUSupportedFeatures#property_size)
*   [values](./././~/GPUSupportedFeatures#method_values_0)

c

[GPUSupportedLimits](./././~/GPUSupportedLimits "GPUSupportedLimits")

No documentation available

*   [maxBindGroups](./././~/GPUSupportedLimits#property_maxbindgroups)
*   [maxBindGroupsPlusVertexBuffers](./././~/GPUSupportedLimits#property_maxbindgroupsplusvertexbuffers)
*   [maxBindingsPerBindGroup](./././~/GPUSupportedLimits#property_maxbindingsperbindgroup)
*   [maxBufferSize](./././~/GPUSupportedLimits#property_maxbuffersize)
*   [maxColorAttachmentBytesPerSample](./././~/GPUSupportedLimits#property_maxcolorattachmentbytespersample)
*   [maxColorAttachments](./././~/GPUSupportedLimits#property_maxcolorattachments)
*   [maxComputeInvocationsPerWorkgroup](./././~/GPUSupportedLimits#property_maxcomputeinvocationsperworkgroup)
*   [maxComputeWorkgroupSizeX](./././~/GPUSupportedLimits#property_maxcomputeworkgroupsizex)
*   [maxComputeWorkgroupSizeY](./././~/GPUSupportedLimits#property_maxcomputeworkgroupsizey)
*   [maxComputeWorkgroupSizeZ](./././~/GPUSupportedLimits#property_maxcomputeworkgroupsizez)
*   [maxComputeWorkgroupStorageSize](./././~/GPUSupportedLimits#property_maxcomputeworkgroupstoragesize)
*   [maxComputeWorkgroupsPerDimension](./././~/GPUSupportedLimits#property_maxcomputeworkgroupsperdimension)
*   [maxDynamicStorageBuffersPerPipelineLayout](./././~/GPUSupportedLimits#property_maxdynamicstoragebuffersperpipelinelayout)
*   [maxDynamicUniformBuffersPerPipelineLayout](./././~/GPUSupportedLimits#property_maxdynamicuniformbuffersperpipelinelayout)
*   [maxInterStageShaderVariables](./././~/GPUSupportedLimits#property_maxinterstageshadervariables)
*   [maxSampledTexturesPerShaderStage](./././~/GPUSupportedLimits#property_maxsampledtexturespershaderstage)
*   [maxSamplersPerShaderStage](./././~/GPUSupportedLimits#property_maxsamplerspershaderstage)
*   [maxStorageBufferBindingSize](./././~/GPUSupportedLimits#property_maxstoragebufferbindingsize)
*   [maxStorageBuffersPerShaderStage](./././~/GPUSupportedLimits#property_maxstoragebufferspershaderstage)
*   [maxStorageTexturesPerShaderStage](./././~/GPUSupportedLimits#property_maxstoragetexturespershaderstage)
*   [maxTextureArrayLayers](./././~/GPUSupportedLimits#property_maxtexturearraylayers)
*   [maxTextureDimension1D](./././~/GPUSupportedLimits#property_maxtexturedimension1d)
*   [maxTextureDimension2D](./././~/GPUSupportedLimits#property_maxtexturedimension2d)
*   [maxTextureDimension3D](./././~/GPUSupportedLimits#property_maxtexturedimension3d)
*   [maxUniformBufferBindingSize](./././~/GPUSupportedLimits#property_maxuniformbufferbindingsize)
*   [maxUniformBuffersPerShaderStage](./././~/GPUSupportedLimits#property_maxuniformbufferspershaderstage)
*   [maxVertexAttributes](./././~/GPUSupportedLimits#property_maxvertexattributes)
*   [maxVertexBufferArrayStride](./././~/GPUSupportedLimits#property_maxvertexbufferarraystride)
*   [maxVertexBuffers](./././~/GPUSupportedLimits#property_maxvertexbuffers)
*   [minStorageBufferOffsetAlignment](./././~/GPUSupportedLimits#property_minstoragebufferoffsetalignment)
*   [minUniformBufferOffsetAlignment](./././~/GPUSupportedLimits#property_minuniformbufferoffsetalignment)

c

[GPUTexture](./././~/GPUTexture "GPUTexture")

Represents a texture (image) in GPU memory.

*   [createView](./././~/GPUTexture#method_createview_0)
*   [depthOrArrayLayers](./././~/GPUTexture#property_depthorarraylayers)
*   [destroy](./././~/GPUTexture#method_destroy_0)
*   [dimension](./././~/GPUTexture#property_dimension)
*   [format](./././~/GPUTexture#property_format)
*   [height](./././~/GPUTexture#property_height)
*   [label](./././~/GPUTexture#property_label)
*   [mipLevelCount](./././~/GPUTexture#property_miplevelcount)
*   [sampleCount](./././~/GPUTexture#property_samplecount)
*   [usage](./././~/GPUTexture#property_usage)
*   [width](./././~/GPUTexture#property_width)

c

[GPUTextureUsage](./././~/GPUTextureUsage "GPUTextureUsage")

No documentation available

*   [COPY\_DST](./././~/GPUTextureUsage#property_copy_dst)
*   [COPY\_SRC](./././~/GPUTextureUsage#property_copy_src)
*   [RENDER\_ATTACHMENT](./././~/GPUTextureUsage#property_render_attachment)
*   [STORAGE\_BINDING](./././~/GPUTextureUsage#property_storage_binding)
*   [TEXTURE\_BINDING](./././~/GPUTextureUsage#property_texture_binding)

c

[GPUTextureView](./././~/GPUTextureView "GPUTextureView")

No documentation available

*   [label](./././~/GPUTextureView#property_label)

c

[GPUUncapturedErrorEvent](./././~/GPUUncapturedErrorEvent "GPUUncapturedErrorEvent")

No documentation available

*   [error](./././~/GPUUncapturedErrorEvent#property_error)

### Interfaces [#](#Interfaces)

I

[GPUBindGroupDescriptor](./././~/GPUBindGroupDescriptor "GPUBindGroupDescriptor")

No documentation available

*   [entries](./././~/GPUBindGroupDescriptor#property_entries)
*   [layout](./././~/GPUBindGroupDescriptor#property_layout)

I

[GPUBindGroupEntry](./././~/GPUBindGroupEntry "GPUBindGroupEntry")

No documentation available

*   [binding](./././~/GPUBindGroupEntry#property_binding)
*   [resource](./././~/GPUBindGroupEntry#property_resource)

I

[GPUBindGroupLayoutDescriptor](./././~/GPUBindGroupLayoutDescriptor "GPUBindGroupLayoutDescriptor")

No documentation available

*   [entries](./././~/GPUBindGroupLayoutDescriptor#property_entries)

I

[GPUBindGroupLayoutEntry](./././~/GPUBindGroupLayoutEntry "GPUBindGroupLayoutEntry")

No documentation available

*   [binding](./././~/GPUBindGroupLayoutEntry#property_binding)
*   [buffer](./././~/GPUBindGroupLayoutEntry#property_buffer)
*   [sampler](./././~/GPUBindGroupLayoutEntry#property_sampler)
*   [storageTexture](./././~/GPUBindGroupLayoutEntry#property_storagetexture)
*   [texture](./././~/GPUBindGroupLayoutEntry#property_texture)
*   [visibility](./././~/GPUBindGroupLayoutEntry#property_visibility)

I

[GPUBlendComponent](./././~/GPUBlendComponent "GPUBlendComponent")

No documentation available

*   [dstFactor](./././~/GPUBlendComponent#property_dstfactor)
*   [operation](./././~/GPUBlendComponent#property_operation)
*   [srcFactor](./././~/GPUBlendComponent#property_srcfactor)

I

[GPUBlendState](./././~/GPUBlendState "GPUBlendState")

No documentation available

*   [alpha](./././~/GPUBlendState#property_alpha)
*   [color](./././~/GPUBlendState#property_color)

I

[GPUBufferBinding](./././~/GPUBufferBinding "GPUBufferBinding")

No documentation available

*   [buffer](./././~/GPUBufferBinding#property_buffer)
*   [offset](./././~/GPUBufferBinding#property_offset)
*   [size](./././~/GPUBufferBinding#property_size)

I

[GPUBufferBindingLayout](./././~/GPUBufferBindingLayout "GPUBufferBindingLayout")

No documentation available

*   [hasDynamicOffset](./././~/GPUBufferBindingLayout#property_hasdynamicoffset)
*   [minBindingSize](./././~/GPUBufferBindingLayout#property_minbindingsize)
*   [type](./././~/GPUBufferBindingLayout#property_type)

I

[GPUBufferDescriptor](./././~/GPUBufferDescriptor "GPUBufferDescriptor")

No documentation available

*   [mappedAtCreation](./././~/GPUBufferDescriptor#property_mappedatcreation)
*   [size](./././~/GPUBufferDescriptor#property_size)
*   [usage](./././~/GPUBufferDescriptor#property_usage)

I

[GPUCanvasConfiguration](./././~/GPUCanvasConfiguration "GPUCanvasConfiguration")

No documentation available

*   [alphaMode](./././~/GPUCanvasConfiguration#property_alphamode)
*   [colorSpace](./././~/GPUCanvasConfiguration#property_colorspace)
*   [device](./././~/GPUCanvasConfiguration#property_device)
*   [format](./././~/GPUCanvasConfiguration#property_format)
*   [usage](./././~/GPUCanvasConfiguration#property_usage)
*   [viewFormats](./././~/GPUCanvasConfiguration#property_viewformats)

I

[GPUCanvasContext](./././~/GPUCanvasContext "GPUCanvasContext")

No documentation available

*   [configure](./././~/GPUCanvasContext#method_configure_0)
*   [getCurrentTexture](./././~/GPUCanvasContext#method_getcurrenttexture_0)
*   [unconfigure](./././~/GPUCanvasContext#method_unconfigure_0)

I

[GPUColorDict](./././~/GPUColorDict "GPUColorDict")

No documentation available

*   [a](./././~/GPUColorDict#property_a)
*   [b](./././~/GPUColorDict#property_b)
*   [g](./././~/GPUColorDict#property_g)
*   [r](./././~/GPUColorDict#property_r)

I

[GPUColorTargetState](./././~/GPUColorTargetState "GPUColorTargetState")

No documentation available

*   [blend](./././~/GPUColorTargetState#property_blend)
*   [format](./././~/GPUColorTargetState#property_format)
*   [writeMask](./././~/GPUColorTargetState#property_writemask)

I

[GPUCommandBufferDescriptor](./././~/GPUCommandBufferDescriptor "GPUCommandBufferDescriptor")

No documentation available

I

[GPUCommandEncoderDescriptor](./././~/GPUCommandEncoderDescriptor "GPUCommandEncoderDescriptor")

No documentation available

I

[GPUComputePassDescriptor](./././~/GPUComputePassDescriptor "GPUComputePassDescriptor")

No documentation available

*   [timestampWrites](./././~/GPUComputePassDescriptor#property_timestampwrites)

I

[GPUComputePassTimestampWrites](./././~/GPUComputePassTimestampWrites "GPUComputePassTimestampWrites")

No documentation available

*   [beginningOfPassWriteIndex](./././~/GPUComputePassTimestampWrites#property_beginningofpasswriteindex)
*   [endOfPassWriteIndex](./././~/GPUComputePassTimestampWrites#property_endofpasswriteindex)
*   [querySet](./././~/GPUComputePassTimestampWrites#property_queryset)

I

[GPUComputePipelineDescriptor](./././~/GPUComputePipelineDescriptor "GPUComputePipelineDescriptor")

No documentation available

*   [compute](./././~/GPUComputePipelineDescriptor#property_compute)

I

[GPUDepthStencilState](./././~/GPUDepthStencilState "GPUDepthStencilState")

No documentation available

*   [depthBias](./././~/GPUDepthStencilState#property_depthbias)
*   [depthBiasClamp](./././~/GPUDepthStencilState#property_depthbiasclamp)
*   [depthBiasSlopeScale](./././~/GPUDepthStencilState#property_depthbiasslopescale)
*   [depthCompare](./././~/GPUDepthStencilState#property_depthcompare)
*   [depthWriteEnabled](./././~/GPUDepthStencilState#property_depthwriteenabled)
*   [format](./././~/GPUDepthStencilState#property_format)
*   [stencilBack](./././~/GPUDepthStencilState#property_stencilback)
*   [stencilFront](./././~/GPUDepthStencilState#property_stencilfront)
*   [stencilReadMask](./././~/GPUDepthStencilState#property_stencilreadmask)
*   [stencilWriteMask](./././~/GPUDepthStencilState#property_stencilwritemask)

I

[GPUDeviceDescriptor](./././~/GPUDeviceDescriptor "GPUDeviceDescriptor")

No documentation available

*   [requiredFeatures](./././~/GPUDeviceDescriptor#property_requiredfeatures)
*   [requiredLimits](./././~/GPUDeviceDescriptor#property_requiredlimits)

I

[GPUDeviceLostInfo](./././~/GPUDeviceLostInfo "GPUDeviceLostInfo")

No documentation available

*   [message](./././~/GPUDeviceLostInfo#property_message)
*   [reason](./././~/GPUDeviceLostInfo#property_reason)

I

v

[GPUError](./././~/GPUError "GPUError")

The **`GPUError`** interface of the WebGPU API is the base interface for errors surfaced by GPUDevice.popErrorScope and the GPUDevice.uncapturederror\_event event. Available only in secure contexts.

*   [message](./././~/GPUError#property_message)
*   [prototype](./././~/GPUError#property_prototype)

I

[GPUExtent3DDict](./././~/GPUExtent3DDict "GPUExtent3DDict")

No documentation available

*   [depthOrArrayLayers](./././~/GPUExtent3DDict#property_depthorarraylayers)
*   [height](./././~/GPUExtent3DDict#property_height)
*   [width](./././~/GPUExtent3DDict#property_width)

I

[GPUFragmentState](./././~/GPUFragmentState "GPUFragmentState")

No documentation available

*   [targets](./././~/GPUFragmentState#property_targets)

I

v

[GPUInternalError](./././~/GPUInternalError "GPUInternalError")

No documentation available

*   [prototype](./././~/GPUInternalError#property_prototype)

I

[GPUMultisampleState](./././~/GPUMultisampleState "GPUMultisampleState")

No documentation available

*   [alphaToCoverageEnabled](./././~/GPUMultisampleState#property_alphatocoverageenabled)
*   [count](./././~/GPUMultisampleState#property_count)
*   [mask](./././~/GPUMultisampleState#property_mask)

I

[GPUObjectBase](./././~/GPUObjectBase "GPUObjectBase")

No documentation available

*   [label](./././~/GPUObjectBase#property_label)

I

[GPUObjectDescriptorBase](./././~/GPUObjectDescriptorBase "GPUObjectDescriptorBase")

No documentation available

*   [label](./././~/GPUObjectDescriptorBase#property_label)

I

[GPUOrigin3DDict](./././~/GPUOrigin3DDict "GPUOrigin3DDict")

No documentation available

*   [x](./././~/GPUOrigin3DDict#property_x)
*   [y](./././~/GPUOrigin3DDict#property_y)
*   [z](./././~/GPUOrigin3DDict#property_z)

I

v

[GPUOutOfMemoryError](./././~/GPUOutOfMemoryError "GPUOutOfMemoryError")

No documentation available

*   [prototype](./././~/GPUOutOfMemoryError#property_prototype)

I

[GPUPipelineBase](./././~/GPUPipelineBase "GPUPipelineBase")

No documentation available

*   [getBindGroupLayout](./././~/GPUPipelineBase#method_getbindgrouplayout_0)

I

[GPUPipelineDescriptorBase](./././~/GPUPipelineDescriptorBase "GPUPipelineDescriptorBase")

No documentation available

*   [layout](./././~/GPUPipelineDescriptorBase#property_layout)

I

v

[GPUPipelineError](./././~/GPUPipelineError "GPUPipelineError")

The **`GPUPipelineError`** interface of the WebGPU API describes a pipeline failure. Available only in secure contexts.

*   [prototype](./././~/GPUPipelineError#property_prototype)
*   [reason](./././~/GPUPipelineError#property_reason)

I

[GPUPipelineErrorInit](./././~/GPUPipelineErrorInit "GPUPipelineErrorInit")

No documentation available

*   [reason](./././~/GPUPipelineErrorInit#property_reason)

I

[GPUPipelineLayoutDescriptor](./././~/GPUPipelineLayoutDescriptor "GPUPipelineLayoutDescriptor")

No documentation available

*   [bindGroupLayouts](./././~/GPUPipelineLayoutDescriptor#property_bindgrouplayouts)

I

[GPUPrimitiveState](./././~/GPUPrimitiveState "GPUPrimitiveState")

No documentation available

*   [cullMode](./././~/GPUPrimitiveState#property_cullmode)
*   [frontFace](./././~/GPUPrimitiveState#property_frontface)
*   [stripIndexFormat](./././~/GPUPrimitiveState#property_stripindexformat)
*   [topology](./././~/GPUPrimitiveState#property_topology)
*   [unclippedDepth](./././~/GPUPrimitiveState#property_unclippeddepth)

I

[GPUProgrammablePassEncoder](./././~/GPUProgrammablePassEncoder "GPUProgrammablePassEncoder")

No documentation available

*   [insertDebugMarker](./././~/GPUProgrammablePassEncoder#method_insertdebugmarker_0)
*   [popDebugGroup](./././~/GPUProgrammablePassEncoder#method_popdebuggroup_0)
*   [pushDebugGroup](./././~/GPUProgrammablePassEncoder#method_pushdebuggroup_0)
*   [setBindGroup](./././~/GPUProgrammablePassEncoder#method_setbindgroup_0)

I

[GPUProgrammableStage](./././~/GPUProgrammableStage "GPUProgrammableStage")

No documentation available

*   [constants](./././~/GPUProgrammableStage#property_constants)
*   [entryPoint](./././~/GPUProgrammableStage#property_entrypoint)
*   [module](./././~/GPUProgrammableStage#property_module)

I

[GPUQuerySetDescriptor](./././~/GPUQuerySetDescriptor "GPUQuerySetDescriptor")

No documentation available

*   [count](./././~/GPUQuerySetDescriptor#property_count)
*   [type](./././~/GPUQuerySetDescriptor#property_type)

I

[GPURenderBundleDescriptor](./././~/GPURenderBundleDescriptor "GPURenderBundleDescriptor")

No documentation available

I

[GPURenderBundleEncoderDescriptor](./././~/GPURenderBundleEncoderDescriptor "GPURenderBundleEncoderDescriptor")

No documentation available

*   [depthReadOnly](./././~/GPURenderBundleEncoderDescriptor#property_depthreadonly)
*   [stencilReadOnly](./././~/GPURenderBundleEncoderDescriptor#property_stencilreadonly)

I

[GPURenderEncoderBase](./././~/GPURenderEncoderBase "GPURenderEncoderBase")

No documentation available

*   [draw](./././~/GPURenderEncoderBase#method_draw_0)
*   [drawIndexed](./././~/GPURenderEncoderBase#method_drawindexed_0)
*   [drawIndexedIndirect](./././~/GPURenderEncoderBase#method_drawindexedindirect_0)
*   [drawIndirect](./././~/GPURenderEncoderBase#method_drawindirect_0)
*   [setIndexBuffer](./././~/GPURenderEncoderBase#method_setindexbuffer_0)
*   [setPipeline](./././~/GPURenderEncoderBase#method_setpipeline_0)
*   [setVertexBuffer](./././~/GPURenderEncoderBase#method_setvertexbuffer_0)

I

[GPURenderPassColorAttachment](./././~/GPURenderPassColorAttachment "GPURenderPassColorAttachment")

No documentation available

*   [clearValue](./././~/GPURenderPassColorAttachment#property_clearvalue)
*   [loadOp](./././~/GPURenderPassColorAttachment#property_loadop)
*   [resolveTarget](./././~/GPURenderPassColorAttachment#property_resolvetarget)
*   [storeOp](./././~/GPURenderPassColorAttachment#property_storeop)
*   [view](./././~/GPURenderPassColorAttachment#property_view)

I

[GPURenderPassDepthStencilAttachment](./././~/GPURenderPassDepthStencilAttachment "GPURenderPassDepthStencilAttachment")

No documentation available

*   [depthClearValue](./././~/GPURenderPassDepthStencilAttachment#property_depthclearvalue)
*   [depthLoadOp](./././~/GPURenderPassDepthStencilAttachment#property_depthloadop)
*   [depthReadOnly](./././~/GPURenderPassDepthStencilAttachment#property_depthreadonly)
*   [depthStoreOp](./././~/GPURenderPassDepthStencilAttachment#property_depthstoreop)
*   [stencilClearValue](./././~/GPURenderPassDepthStencilAttachment#property_stencilclearvalue)
*   [stencilLoadOp](./././~/GPURenderPassDepthStencilAttachment#property_stencilloadop)
*   [stencilReadOnly](./././~/GPURenderPassDepthStencilAttachment#property_stencilreadonly)
*   [stencilStoreOp](./././~/GPURenderPassDepthStencilAttachment#property_stencilstoreop)
*   [view](./././~/GPURenderPassDepthStencilAttachment#property_view)

I

[GPURenderPassDescriptor](./././~/GPURenderPassDescriptor "GPURenderPassDescriptor")

No documentation available

*   [colorAttachments](./././~/GPURenderPassDescriptor#property_colorattachments)
*   [depthStencilAttachment](./././~/GPURenderPassDescriptor#property_depthstencilattachment)
*   [occlusionQuerySet](./././~/GPURenderPassDescriptor#property_occlusionqueryset)
*   [timestampWrites](./././~/GPURenderPassDescriptor#property_timestampwrites)

I

[GPURenderPassLayout](./././~/GPURenderPassLayout "GPURenderPassLayout")

No documentation available

*   [colorFormats](./././~/GPURenderPassLayout#property_colorformats)
*   [depthStencilFormat](./././~/GPURenderPassLayout#property_depthstencilformat)
*   [sampleCount](./././~/GPURenderPassLayout#property_samplecount)

I

[GPURenderPassTimestampWrites](./././~/GPURenderPassTimestampWrites "GPURenderPassTimestampWrites")

No documentation available

*   [beginningOfPassWriteIndex](./././~/GPURenderPassTimestampWrites#property_beginningofpasswriteindex)
*   [endOfPassWriteIndex](./././~/GPURenderPassTimestampWrites#property_endofpasswriteindex)
*   [querySet](./././~/GPURenderPassTimestampWrites#property_queryset)

I

[GPURenderPipelineDescriptor](./././~/GPURenderPipelineDescriptor "GPURenderPipelineDescriptor")

No documentation available

*   [depthStencil](./././~/GPURenderPipelineDescriptor#property_depthstencil)
*   [fragment](./././~/GPURenderPipelineDescriptor#property_fragment)
*   [multisample](./././~/GPURenderPipelineDescriptor#property_multisample)
*   [primitive](./././~/GPURenderPipelineDescriptor#property_primitive)
*   [vertex](./././~/GPURenderPipelineDescriptor#property_vertex)

I

[GPURequestAdapterOptions](./././~/GPURequestAdapterOptions "GPURequestAdapterOptions")

No documentation available

*   [forceFallbackAdapter](./././~/GPURequestAdapterOptions#property_forcefallbackadapter)
*   [powerPreference](./././~/GPURequestAdapterOptions#property_powerpreference)

I

[GPUSamplerBindingLayout](./././~/GPUSamplerBindingLayout "GPUSamplerBindingLayout")

No documentation available

*   [type](./././~/GPUSamplerBindingLayout#property_type)

I

[GPUSamplerDescriptor](./././~/GPUSamplerDescriptor "GPUSamplerDescriptor")

No documentation available

*   [addressModeU](./././~/GPUSamplerDescriptor#property_addressmodeu)
*   [addressModeV](./././~/GPUSamplerDescriptor#property_addressmodev)
*   [addressModeW](./././~/GPUSamplerDescriptor#property_addressmodew)
*   [compare](./././~/GPUSamplerDescriptor#property_compare)
*   [lodMaxClamp](./././~/GPUSamplerDescriptor#property_lodmaxclamp)
*   [lodMinClamp](./././~/GPUSamplerDescriptor#property_lodminclamp)
*   [magFilter](./././~/GPUSamplerDescriptor#property_magfilter)
*   [maxAnisotropy](./././~/GPUSamplerDescriptor#property_maxanisotropy)
*   [minFilter](./././~/GPUSamplerDescriptor#property_minfilter)
*   [mipmapFilter](./././~/GPUSamplerDescriptor#property_mipmapfilter)

I

[GPUShaderModuleDescriptor](./././~/GPUShaderModuleDescriptor "GPUShaderModuleDescriptor")

No documentation available

*   [code](./././~/GPUShaderModuleDescriptor#property_code)
*   [sourceMap](./././~/GPUShaderModuleDescriptor#property_sourcemap)

I

[GPUStencilFaceState](./././~/GPUStencilFaceState "GPUStencilFaceState")

No documentation available

*   [compare](./././~/GPUStencilFaceState#property_compare)
*   [depthFailOp](./././~/GPUStencilFaceState#property_depthfailop)
*   [failOp](./././~/GPUStencilFaceState#property_failop)
*   [passOp](./././~/GPUStencilFaceState#property_passop)

I

[GPUStorageTextureBindingLayout](./././~/GPUStorageTextureBindingLayout "GPUStorageTextureBindingLayout")

No documentation available

*   [access](./././~/GPUStorageTextureBindingLayout#property_access)
*   [format](./././~/GPUStorageTextureBindingLayout#property_format)
*   [viewDimension](./././~/GPUStorageTextureBindingLayout#property_viewdimension)

I

[GPUTexelCopyBufferInfo](./././~/GPUTexelCopyBufferInfo "GPUTexelCopyBufferInfo")

No documentation available

*   [buffer](./././~/GPUTexelCopyBufferInfo#property_buffer)

I

[GPUTexelCopyBufferLayout](./././~/GPUTexelCopyBufferLayout "GPUTexelCopyBufferLayout")

No documentation available

*   [bytesPerRow](./././~/GPUTexelCopyBufferLayout#property_bytesperrow)
*   [offset](./././~/GPUTexelCopyBufferLayout#property_offset)
*   [rowsPerImage](./././~/GPUTexelCopyBufferLayout#property_rowsperimage)

I

[GPUTexelCopyTextureInfo](./././~/GPUTexelCopyTextureInfo "GPUTexelCopyTextureInfo")

No documentation available

*   [aspect](./././~/GPUTexelCopyTextureInfo#property_aspect)
*   [mipLevel](./././~/GPUTexelCopyTextureInfo#property_miplevel)
*   [origin](./././~/GPUTexelCopyTextureInfo#property_origin)
*   [texture](./././~/GPUTexelCopyTextureInfo#property_texture)

I

[GPUTextureBindingLayout](./././~/GPUTextureBindingLayout "GPUTextureBindingLayout")

No documentation available

*   [multisampled](./././~/GPUTextureBindingLayout#property_multisampled)
*   [sampleType](./././~/GPUTextureBindingLayout#property_sampletype)
*   [viewDimension](./././~/GPUTextureBindingLayout#property_viewdimension)

I

[GPUTextureDescriptor](./././~/GPUTextureDescriptor "GPUTextureDescriptor")

No documentation available

*   [dimension](./././~/GPUTextureDescriptor#property_dimension)
*   [format](./././~/GPUTextureDescriptor#property_format)
*   [mipLevelCount](./././~/GPUTextureDescriptor#property_miplevelcount)
*   [sampleCount](./././~/GPUTextureDescriptor#property_samplecount)
*   [size](./././~/GPUTextureDescriptor#property_size)
*   [usage](./././~/GPUTextureDescriptor#property_usage)
*   [viewFormats](./././~/GPUTextureDescriptor#property_viewformats)

I

[GPUTextureViewDescriptor](./././~/GPUTextureViewDescriptor "GPUTextureViewDescriptor")

No documentation available

*   [arrayLayerCount](./././~/GPUTextureViewDescriptor#property_arraylayercount)
*   [aspect](./././~/GPUTextureViewDescriptor#property_aspect)
*   [baseArrayLayer](./././~/GPUTextureViewDescriptor#property_basearraylayer)
*   [baseMipLevel](./././~/GPUTextureViewDescriptor#property_basemiplevel)
*   [dimension](./././~/GPUTextureViewDescriptor#property_dimension)
*   [format](./././~/GPUTextureViewDescriptor#property_format)
*   [mipLevelCount](./././~/GPUTextureViewDescriptor#property_miplevelcount)
*   [usage](./././~/GPUTextureViewDescriptor#property_usage)

I

[GPUUncapturedErrorEventInit](./././~/GPUUncapturedErrorEventInit "GPUUncapturedErrorEventInit")

No documentation available

*   [error](./././~/GPUUncapturedErrorEventInit#property_error)

I

v

[GPUValidationError](./././~/GPUValidationError "GPUValidationError")

No documentation available

*   [prototype](./././~/GPUValidationError#property_prototype)

I

[GPUVertexAttribute](./././~/GPUVertexAttribute "GPUVertexAttribute")

No documentation available

*   [format](./././~/GPUVertexAttribute#property_format)
*   [offset](./././~/GPUVertexAttribute#property_offset)
*   [shaderLocation](./././~/GPUVertexAttribute#property_shaderlocation)

I

[GPUVertexBufferLayout](./././~/GPUVertexBufferLayout "GPUVertexBufferLayout")

No documentation available

*   [arrayStride](./././~/GPUVertexBufferLayout#property_arraystride)
*   [attributes](./././~/GPUVertexBufferLayout#property_attributes)
*   [stepMode](./././~/GPUVertexBufferLayout#property_stepmode)

I

[GPUVertexState](./././~/GPUVertexState "GPUVertexState")

No documentation available

*   [buffers](./././~/GPUVertexState#property_buffers)

### Type Aliases [#](<#Type Aliases>)

T

[GPUAddressMode](./././~/GPUAddressMode "GPUAddressMode")

No documentation available

T

[GPUAutoLayoutMode](./././~/GPUAutoLayoutMode "GPUAutoLayoutMode")

No documentation available

T

[GPUBindingResource](./././~/GPUBindingResource "GPUBindingResource")

No documentation available

T

[GPUBlendFactor](./././~/GPUBlendFactor "GPUBlendFactor")

No documentation available

T

[GPUBlendOperation](./././~/GPUBlendOperation "GPUBlendOperation")

No documentation available

T

[GPUBufferBindingType](./././~/GPUBufferBindingType "GPUBufferBindingType")

No documentation available

T

[GPUBufferMapState](./././~/GPUBufferMapState "GPUBufferMapState")

No documentation available

T

[GPUBufferUsageFlags](./././~/GPUBufferUsageFlags "GPUBufferUsageFlags")

No documentation available

T

[GPUCanvasAlphaMode](./././~/GPUCanvasAlphaMode "GPUCanvasAlphaMode")

No documentation available

T

[GPUColor](./././~/GPUColor "GPUColor")

No documentation available

T

[GPUColorWriteFlags](./././~/GPUColorWriteFlags "GPUColorWriteFlags")

No documentation available

T

[GPUCompareFunction](./././~/GPUCompareFunction "GPUCompareFunction")

No documentation available

T

[GPUCompilationMessageType](./././~/GPUCompilationMessageType "GPUCompilationMessageType")

No documentation available

T

[GPUCullMode](./././~/GPUCullMode "GPUCullMode")

No documentation available

T

[GPUDeviceLostReason](./././~/GPUDeviceLostReason "GPUDeviceLostReason")

No documentation available

T

[GPUErrorFilter](./././~/GPUErrorFilter "GPUErrorFilter")

No documentation available

T

[GPUExtent3D](./././~/GPUExtent3D "GPUExtent3D")

No documentation available

T

[GPUFeatureName](./././~/GPUFeatureName "GPUFeatureName")

No documentation available

T

[GPUFilterMode](./././~/GPUFilterMode "GPUFilterMode")

No documentation available

T

[GPUFlagsConstant](./././~/GPUFlagsConstant "GPUFlagsConstant")

No documentation available

T

[GPUFrontFace](./././~/GPUFrontFace "GPUFrontFace")

No documentation available

T

[GPUIndexFormat](./././~/GPUIndexFormat "GPUIndexFormat")

No documentation available

T

[GPULoadOp](./././~/GPULoadOp "GPULoadOp")

No documentation available

T

[GPUMapModeFlags](./././~/GPUMapModeFlags "GPUMapModeFlags")

No documentation available

T

[GPUMipmapFilterMode](./././~/GPUMipmapFilterMode "GPUMipmapFilterMode")

No documentation available

T

[GPUOrigin3D](./././~/GPUOrigin3D "GPUOrigin3D")

No documentation available

T

[GPUPowerPreference](./././~/GPUPowerPreference "GPUPowerPreference")

No documentation available

T

[GPUPrimitiveTopology](./././~/GPUPrimitiveTopology "GPUPrimitiveTopology")

No documentation available

T

[GPUQueryType](./././~/GPUQueryType "GPUQueryType")

No documentation available

T

[GPUSamplerBindingType](./././~/GPUSamplerBindingType "GPUSamplerBindingType")

No documentation available

T

[GPUShaderStageFlags](./././~/GPUShaderStageFlags "GPUShaderStageFlags")

No documentation available

T

[GPUStencilOperation](./././~/GPUStencilOperation "GPUStencilOperation")

No documentation available

T

[GPUStorageTextureAccess](./././~/GPUStorageTextureAccess "GPUStorageTextureAccess")

No documentation available

T

[GPUStoreOp](./././~/GPUStoreOp "GPUStoreOp")

No documentation available

T

[GPUTextureAspect](./././~/GPUTextureAspect "GPUTextureAspect")

No documentation available

T

[GPUTextureDimension](./././~/GPUTextureDimension "GPUTextureDimension")

No documentation available

T

[GPUTextureFormat](./././~/GPUTextureFormat "GPUTextureFormat")

No documentation available

T

[GPUTextureSampleType](./././~/GPUTextureSampleType "GPUTextureSampleType")

No documentation available

T

[GPUTextureUsageFlags](./././~/GPUTextureUsageFlags "GPUTextureUsageFlags")

No documentation available

T

[GPUTextureViewDimension](./././~/GPUTextureViewDimension "GPUTextureViewDimension")

No documentation available

T

[GPUVertexFormat](./././~/GPUVertexFormat "GPUVertexFormat")

No documentation available

T

[GPUVertexStepMode](./././~/GPUVertexStepMode "GPUVertexStepMode")

No documentation available
