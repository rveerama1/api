# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mesh/v1alpha1/proxy.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from networking.v1alpha3 import destination_rule_pb2 as networking_dot_v1alpha3_dot_destination__rule__pb2
from networking.v1alpha3 import workload_group_pb2 as networking_dot_v1alpha3_dot_workload__group__pb2
from networking.v1beta1 import proxy_config_pb2 as networking_dot_v1beta1_dot_proxy__config__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19mesh/v1alpha1/proxy.proto\x12\x13istio.mesh.v1alpha1\x1a\x1egoogle/protobuf/duration.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a*networking/v1alpha3/destination_rule.proto\x1a(networking/v1alpha3/workload_group.proto\x1a%networking/v1beta1/proxy_config.proto\"\xa5\x0e\n\x07Tracing\x12=\n\x06zipkin\x18\x01 \x01(\x0b\x32#.istio.mesh.v1alpha1.Tracing.ZipkinH\x00R\x06zipkin\x12\x46\n\tlightstep\x18\x02 \x01(\x0b\x32&.istio.mesh.v1alpha1.Tracing.LightstepH\x00R\tlightstep\x12@\n\x07\x64\x61tadog\x18\x03 \x01(\x0b\x32$.istio.mesh.v1alpha1.Tracing.DatadogH\x00R\x07\x64\x61tadog\x12L\n\x0bstackdriver\x18\x04 \x01(\x0b\x32(.istio.mesh.v1alpha1.Tracing.StackdriverH\x00R\x0bstackdriver\x12Z\n\x11open_census_agent\x18\t \x01(\x0b\x32,.istio.mesh.v1alpha1.Tracing.OpenCensusAgentH\x00R\x0fopenCensusAgent\x12M\n\x0b\x63ustom_tags\x18\x05 \x03(\x0b\x32,.istio.mesh.v1alpha1.Tracing.CustomTagsEntryR\ncustomTags\x12-\n\x13max_path_tag_length\x18\x06 \x01(\rR\x10maxPathTagLength\x12\x1a\n\x08sampling\x18\x07 \x01(\x01R\x08sampling\x12O\n\x0ctls_settings\x18\x08 \x01(\x0b\x32,.istio.networking.v1alpha3.ClientTLSSettingsR\x0btlsSettings\x1a\"\n\x06Zipkin\x12\x18\n\x07\x61\x64\x64ress\x18\x01 \x01(\tR\x07\x61\x64\x64ress\x1aH\n\tLightstep\x12\x18\n\x07\x61\x64\x64ress\x18\x01 \x01(\tR\x07\x61\x64\x64ress\x12!\n\x0c\x61\x63\x63\x65ss_token\x18\x02 \x01(\tR\x0b\x61\x63\x63\x65ssToken\x1a#\n\x07\x44\x61tadog\x12\x18\n\x07\x61\x64\x64ress\x18\x01 \x01(\tR\x07\x61\x64\x64ress\x1a\xae\x02\n\x0bStackdriver\x12\x14\n\x05\x64\x65\x62ug\x18\x01 \x01(\x08R\x05\x64\x65\x62ug\x12T\n\x18max_number_of_attributes\x18\x02 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueR\x15maxNumberOfAttributes\x12V\n\x19max_number_of_annotations\x18\x03 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueR\x16maxNumberOfAnnotations\x12[\n\x1cmax_number_of_message_events\x18\x04 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueR\x18maxNumberOfMessageEvents\x1a\xe7\x01\n\x0fOpenCensusAgent\x12\x18\n\x07\x61\x64\x64ress\x18\x01 \x01(\tR\x07\x61\x64\x64ress\x12S\n\x07\x63ontext\x18\x02 \x03(\x0e\x32\x39.istio.mesh.v1alpha1.Tracing.OpenCensusAgent.TraceContextR\x07\x63ontext\"e\n\x0cTraceContext\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x15\n\x11W3C_TRACE_CONTEXT\x10\x01\x12\x0c\n\x08GRPC_BIN\x10\x02\x12\x17\n\x13\x43LOUD_TRACE_CONTEXT\x10\x03\x12\x06\n\x02\x42\x33\x10\x04\x1a\xe9\x01\n\tCustomTag\x12@\n\x07literal\x18\x01 \x01(\x0b\x32$.istio.mesh.v1alpha1.Tracing.LiteralH\x00R\x07literal\x12L\n\x0b\x65nvironment\x18\x02 \x01(\x0b\x32(.istio.mesh.v1alpha1.Tracing.EnvironmentH\x00R\x0b\x65nvironment\x12\x44\n\x06header\x18\x03 \x01(\x0b\x32*.istio.mesh.v1alpha1.Tracing.RequestHeaderH\x00R\x06headerB\x06\n\x04type\x1a\x1f\n\x07Literal\x12\x14\n\x05value\x18\x01 \x01(\tR\x05value\x1a\x46\n\x0b\x45nvironment\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12#\n\rdefault_value\x18\x02 \x01(\tR\x0c\x64\x65\x66\x61ultValue\x1aH\n\rRequestHeader\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12#\n\rdefault_value\x18\x02 \x01(\tR\x0c\x64\x65\x66\x61ultValue\x1a\x65\n\x0f\x43ustomTagsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12<\n\x05value\x18\x02 \x01(\x0b\x32&.istio.mesh.v1alpha1.Tracing.CustomTagR\x05value:\x02\x38\x01\x42\x08\n\x06tracer\"F\n\x03SDS\x12\x18\n\x07\x65nabled\x18\x01 \x01(\x08R\x07\x65nabled\x12%\n\x0fk8s_sa_jwt_path\x18\x02 \x01(\tR\x0ck8sSaJwtPath\"\xbc\x02\n\x08Topology\x12.\n\x13num_trusted_proxies\x18\x01 \x01(\rR\x11numTrustedProxies\x12u\n\x1b\x66orward_client_cert_details\x18\x02 \x01(\x0e\x32\x36.istio.mesh.v1alpha1.Topology.ForwardClientCertDetailsR\x18\x66orwardClientCertDetails\"\x88\x01\n\x18\x46orwardClientCertDetails\x12\r\n\tUNDEFINED\x10\x00\x12\x0c\n\x08SANITIZE\x10\x01\x12\x10\n\x0c\x46ORWARD_ONLY\x10\x02\x12\x12\n\x0e\x41PPEND_FORWARD\x10\x03\x12\x10\n\x0cSANITIZE_SET\x10\x04\x12\x17\n\x13\x41LWAYS_FORWARD_ONLY\x10\x05\"\xb6\x01\n\x12PrivateKeyProvider\x12N\n\x08\x63ryptomb\x18\x02 \x01(\x0b\x32\x30.istio.mesh.v1alpha1.PrivateKeyProvider.CryptoMbH\x00R\x08\x63ryptomb\x1a\x44\n\x08\x43ryptoMb\x12\x38\n\npoll_delay\x18\x01 \x01(\x0b\x32\x19.google.protobuf.DurationR\tpollDelayB\n\n\x08provider\"\xd8\x16\n\x0bProxyConfig\x12\x1f\n\x0b\x63onfig_path\x18\x01 \x01(\tR\nconfigPath\x12\x1f\n\x0b\x62inary_path\x18\x02 \x01(\tR\nbinaryPath\x12)\n\x0fservice_cluster\x18\x03 \x01(\tH\x00R\x0eserviceCluster\x12g\n\x14tracing_service_name\x18$ \x01(\x0e\x32\x33.istio.mesh.v1alpha1.ProxyConfig.TracingServiceNameH\x00R\x12tracingServiceName\x12@\n\x0e\x64rain_duration\x18\x04 \x01(\x0b\x32\x19.google.protobuf.DurationR\rdrainDuration\x12S\n\x18parent_shutdown_duration\x18\x05 \x01(\x0b\x32\x19.google.protobuf.DurationR\x16parentShutdownDuration\x12+\n\x11\x64iscovery_address\x18\x06 \x01(\tR\x10\x64iscoveryAddress\x12U\n\x17\x64iscovery_refresh_delay\x18\x07 \x01(\x0b\x32\x19.google.protobuf.DurationB\x02\x18\x01R\x15\x64iscoveryRefreshDelay\x12)\n\x0ezipkin_address\x18\x08 \x01(\tB\x02\x18\x01R\rzipkinAddress\x12,\n\x12statsd_udp_address\x18\n \x01(\tR\x10statsdUdpAddress\x12\x45\n\x1d\x65nvoy_metrics_service_address\x18\x14 \x01(\tB\x02\x18\x01R\x1a\x65nvoyMetricsServiceAddress\x12(\n\x10proxy_admin_port\x18\x0b \x01(\x05R\x0eproxyAdminPort\x12/\n\x11\x61vailability_zone\x18\x0c \x01(\tB\x02\x18\x01R\x10\x61vailabilityZone\x12\x64\n\x19\x63ontrol_plane_auth_policy\x18\r \x01(\x0e\x32).istio.mesh.v1alpha1.AuthenticationPolicyR\x16\x63ontrolPlaneAuthPolicy\x12,\n\x12\x63ustom_config_file\x18\x0e \x01(\tR\x10\x63ustomConfigFile\x12(\n\x10stat_name_length\x18\x0f \x01(\x05R\x0estatNameLength\x12=\n\x0b\x63oncurrency\x18\x10 \x01(\x0b\x32\x1b.google.protobuf.Int32ValueR\x0b\x63oncurrency\x12\x41\n\x1dproxy_bootstrap_template_path\x18\x11 \x01(\tR\x1aproxyBootstrapTemplatePath\x12\x65\n\x11interception_mode\x18\x12 \x01(\x0e\x32\x38.istio.mesh.v1alpha1.ProxyConfig.InboundInterceptionModeR\x10interceptionMode\x12\x36\n\x07tracing\x18\x13 \x01(\x0b\x32\x1c.istio.mesh.v1alpha1.TracingR\x07tracing\x12*\n\x03sds\x18\x15 \x01(\x0b\x32\x18.istio.mesh.v1alpha1.SDSR\x03sds\x12[\n\x18\x65nvoy_access_log_service\x18\x16 \x01(\x0b\x32\".istio.mesh.v1alpha1.RemoteServiceR\x15\x65nvoyAccessLogService\x12V\n\x15\x65nvoy_metrics_service\x18\x17 \x01(\x0b\x32\".istio.mesh.v1alpha1.RemoteServiceR\x13\x65nvoyMetricsService\x12Z\n\x0eproxy_metadata\x18\x18 \x03(\x0b\x32\x33.istio.mesh.v1alpha1.ProxyConfig.ProxyMetadataEntryR\rproxyMetadata\x12Z\n\x0eruntime_values\x18% \x03(\x0b\x32\x33.istio.mesh.v1alpha1.ProxyConfig.RuntimeValuesEntryR\rruntimeValues\x12\x1f\n\x0bstatus_port\x18\x1a \x01(\x05R\nstatusPort\x12&\n\x0f\x65xtra_stat_tags\x18\x1b \x03(\tR\rextraStatTags\x12H\n\x10gateway_topology\x18\x1c \x01(\x0b\x32\x1d.istio.mesh.v1alpha1.TopologyR\x0fgatewayTopology\x12W\n\x1atermination_drain_duration\x18\x1d \x01(\x0b\x32\x19.google.protobuf.DurationR\x18terminationDrainDuration\x12\x17\n\x07mesh_id\x18\x1e \x01(\tR\x06meshId\x12R\n\x0freadiness_probe\x18\x1f \x01(\x0b\x32).istio.networking.v1alpha3.ReadinessProbeR\x0ereadinessProbe\x12\x62\n\x13proxy_stats_matcher\x18  \x01(\x0b\x32\x32.istio.mesh.v1alpha1.ProxyConfig.ProxyStatsMatcherR\x11proxyStatsMatcher\x12h\n#hold_application_until_proxy_starts\x18! \x01(\x0b\x32\x1a.google.protobuf.BoolValueR\x1fholdApplicationUntilProxyStarts\x12.\n\x13\x63\x61_certificates_pem\x18\" \x03(\tR\x11\x63\x61\x43\x65rtificatesPem\x12:\n\x05image\x18# \x01(\x0b\x32$.istio.networking.v1beta1.ProxyImageR\x05image\x12Y\n\x14private_key_provider\x18& \x01(\x0b\x32\'.istio.mesh.v1alpha1.PrivateKeyProviderR\x12privateKeyProvider\x1a@\n\x12ProxyMetadataEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01\x1a@\n\x12RuntimeValuesEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01\x1a\x9e\x01\n\x11ProxyStatsMatcher\x12-\n\x12inclusion_prefixes\x18\x01 \x03(\tR\x11inclusionPrefixes\x12-\n\x12inclusion_suffixes\x18\x02 \x03(\tR\x11inclusionSuffixes\x12+\n\x11inclusion_regexps\x18\x03 \x03(\tR\x10inclusionRegexps\"l\n\x12TracingServiceName\x12\x1b\n\x17\x41PP_LABEL_AND_NAMESPACE\x10\x00\x12\x17\n\x13\x43\x41NONICAL_NAME_ONLY\x10\x01\x12 \n\x1c\x43\x41NONICAL_NAME_AND_NAMESPACE\x10\x02\"=\n\x17InboundInterceptionMode\x12\x0c\n\x08REDIRECT\x10\x00\x12\n\n\x06TPROXY\x10\x01\x12\x08\n\x04NONE\x10\x02\x42\x0e\n\x0c\x63luster_nameJ\x04\x08\t\x10\nR\x0f\x63onnect_timeout\"\xeb\x01\n\rRemoteService\x12\x18\n\x07\x61\x64\x64ress\x18\x01 \x01(\tR\x07\x61\x64\x64ress\x12O\n\x0ctls_settings\x18\x02 \x01(\x0b\x32,.istio.networking.v1alpha3.ClientTLSSettingsR\x0btlsSettings\x12o\n\rtcp_keepalive\x18\x03 \x01(\x0b\x32J.istio.networking.v1alpha3.ConnectionPoolSettings.TCPSettings.TcpKeepaliveR\x0ctcpKeepalive*>\n\x14\x41uthenticationPolicy\x12\x08\n\x04NONE\x10\x00\x12\x0e\n\nMUTUAL_TLS\x10\x01\x12\x0c\n\x07INHERIT\x10\xe8\x07\x42\x1cZ\x1aistio.io/api/mesh/v1alpha1b\x06proto3')

_AUTHENTICATIONPOLICY = DESCRIPTOR.enum_types_by_name['AuthenticationPolicy']
AuthenticationPolicy = enum_type_wrapper.EnumTypeWrapper(_AUTHENTICATIONPOLICY)
NONE = 0
MUTUAL_TLS = 1
INHERIT = 1000


_TRACING = DESCRIPTOR.message_types_by_name['Tracing']
_TRACING_ZIPKIN = _TRACING.nested_types_by_name['Zipkin']
_TRACING_LIGHTSTEP = _TRACING.nested_types_by_name['Lightstep']
_TRACING_DATADOG = _TRACING.nested_types_by_name['Datadog']
_TRACING_STACKDRIVER = _TRACING.nested_types_by_name['Stackdriver']
_TRACING_OPENCENSUSAGENT = _TRACING.nested_types_by_name['OpenCensusAgent']
_TRACING_CUSTOMTAG = _TRACING.nested_types_by_name['CustomTag']
_TRACING_LITERAL = _TRACING.nested_types_by_name['Literal']
_TRACING_ENVIRONMENT = _TRACING.nested_types_by_name['Environment']
_TRACING_REQUESTHEADER = _TRACING.nested_types_by_name['RequestHeader']
_TRACING_CUSTOMTAGSENTRY = _TRACING.nested_types_by_name['CustomTagsEntry']
_SDS = DESCRIPTOR.message_types_by_name['SDS']
_TOPOLOGY = DESCRIPTOR.message_types_by_name['Topology']
_PRIVATEKEYPROVIDER = DESCRIPTOR.message_types_by_name['PrivateKeyProvider']
_PRIVATEKEYPROVIDER_CRYPTOMB = _PRIVATEKEYPROVIDER.nested_types_by_name['CryptoMb']
_PROXYCONFIG = DESCRIPTOR.message_types_by_name['ProxyConfig']
_PROXYCONFIG_PROXYMETADATAENTRY = _PROXYCONFIG.nested_types_by_name['ProxyMetadataEntry']
_PROXYCONFIG_RUNTIMEVALUESENTRY = _PROXYCONFIG.nested_types_by_name['RuntimeValuesEntry']
_PROXYCONFIG_PROXYSTATSMATCHER = _PROXYCONFIG.nested_types_by_name['ProxyStatsMatcher']
_REMOTESERVICE = DESCRIPTOR.message_types_by_name['RemoteService']
_TRACING_OPENCENSUSAGENT_TRACECONTEXT = _TRACING_OPENCENSUSAGENT.enum_types_by_name['TraceContext']
_TOPOLOGY_FORWARDCLIENTCERTDETAILS = _TOPOLOGY.enum_types_by_name['ForwardClientCertDetails']
_PROXYCONFIG_TRACINGSERVICENAME = _PROXYCONFIG.enum_types_by_name['TracingServiceName']
_PROXYCONFIG_INBOUNDINTERCEPTIONMODE = _PROXYCONFIG.enum_types_by_name['InboundInterceptionMode']
Tracing = _reflection.GeneratedProtocolMessageType('Tracing', (_message.Message,), {

  'Zipkin' : _reflection.GeneratedProtocolMessageType('Zipkin', (_message.Message,), {
    'DESCRIPTOR' : _TRACING_ZIPKIN,
    '__module__' : 'mesh.v1alpha1.proxy_pb2'
    # @@protoc_insertion_point(class_scope:istio.mesh.v1alpha1.Tracing.Zipkin)
    })
  ,

  'Lightstep' : _reflection.GeneratedProtocolMessageType('Lightstep', (_message.Message,), {
    'DESCRIPTOR' : _TRACING_LIGHTSTEP,
    '__module__' : 'mesh.v1alpha1.proxy_pb2'
    # @@protoc_insertion_point(class_scope:istio.mesh.v1alpha1.Tracing.Lightstep)
    })
  ,

  'Datadog' : _reflection.GeneratedProtocolMessageType('Datadog', (_message.Message,), {
    'DESCRIPTOR' : _TRACING_DATADOG,
    '__module__' : 'mesh.v1alpha1.proxy_pb2'
    # @@protoc_insertion_point(class_scope:istio.mesh.v1alpha1.Tracing.Datadog)
    })
  ,

  'Stackdriver' : _reflection.GeneratedProtocolMessageType('Stackdriver', (_message.Message,), {
    'DESCRIPTOR' : _TRACING_STACKDRIVER,
    '__module__' : 'mesh.v1alpha1.proxy_pb2'
    # @@protoc_insertion_point(class_scope:istio.mesh.v1alpha1.Tracing.Stackdriver)
    })
  ,

  'OpenCensusAgent' : _reflection.GeneratedProtocolMessageType('OpenCensusAgent', (_message.Message,), {
    'DESCRIPTOR' : _TRACING_OPENCENSUSAGENT,
    '__module__' : 'mesh.v1alpha1.proxy_pb2'
    # @@protoc_insertion_point(class_scope:istio.mesh.v1alpha1.Tracing.OpenCensusAgent)
    })
  ,

  'CustomTag' : _reflection.GeneratedProtocolMessageType('CustomTag', (_message.Message,), {
    'DESCRIPTOR' : _TRACING_CUSTOMTAG,
    '__module__' : 'mesh.v1alpha1.proxy_pb2'
    # @@protoc_insertion_point(class_scope:istio.mesh.v1alpha1.Tracing.CustomTag)
    })
  ,

  'Literal' : _reflection.GeneratedProtocolMessageType('Literal', (_message.Message,), {
    'DESCRIPTOR' : _TRACING_LITERAL,
    '__module__' : 'mesh.v1alpha1.proxy_pb2'
    # @@protoc_insertion_point(class_scope:istio.mesh.v1alpha1.Tracing.Literal)
    })
  ,

  'Environment' : _reflection.GeneratedProtocolMessageType('Environment', (_message.Message,), {
    'DESCRIPTOR' : _TRACING_ENVIRONMENT,
    '__module__' : 'mesh.v1alpha1.proxy_pb2'
    # @@protoc_insertion_point(class_scope:istio.mesh.v1alpha1.Tracing.Environment)
    })
  ,

  'RequestHeader' : _reflection.GeneratedProtocolMessageType('RequestHeader', (_message.Message,), {
    'DESCRIPTOR' : _TRACING_REQUESTHEADER,
    '__module__' : 'mesh.v1alpha1.proxy_pb2'
    # @@protoc_insertion_point(class_scope:istio.mesh.v1alpha1.Tracing.RequestHeader)
    })
  ,

  'CustomTagsEntry' : _reflection.GeneratedProtocolMessageType('CustomTagsEntry', (_message.Message,), {
    'DESCRIPTOR' : _TRACING_CUSTOMTAGSENTRY,
    '__module__' : 'mesh.v1alpha1.proxy_pb2'
    # @@protoc_insertion_point(class_scope:istio.mesh.v1alpha1.Tracing.CustomTagsEntry)
    })
  ,
  'DESCRIPTOR' : _TRACING,
  '__module__' : 'mesh.v1alpha1.proxy_pb2'
  # @@protoc_insertion_point(class_scope:istio.mesh.v1alpha1.Tracing)
  })
_sym_db.RegisterMessage(Tracing)
_sym_db.RegisterMessage(Tracing.Zipkin)
_sym_db.RegisterMessage(Tracing.Lightstep)
_sym_db.RegisterMessage(Tracing.Datadog)
_sym_db.RegisterMessage(Tracing.Stackdriver)
_sym_db.RegisterMessage(Tracing.OpenCensusAgent)
_sym_db.RegisterMessage(Tracing.CustomTag)
_sym_db.RegisterMessage(Tracing.Literal)
_sym_db.RegisterMessage(Tracing.Environment)
_sym_db.RegisterMessage(Tracing.RequestHeader)
_sym_db.RegisterMessage(Tracing.CustomTagsEntry)

SDS = _reflection.GeneratedProtocolMessageType('SDS', (_message.Message,), {
  'DESCRIPTOR' : _SDS,
  '__module__' : 'mesh.v1alpha1.proxy_pb2'
  # @@protoc_insertion_point(class_scope:istio.mesh.v1alpha1.SDS)
  })
_sym_db.RegisterMessage(SDS)

Topology = _reflection.GeneratedProtocolMessageType('Topology', (_message.Message,), {
  'DESCRIPTOR' : _TOPOLOGY,
  '__module__' : 'mesh.v1alpha1.proxy_pb2'
  # @@protoc_insertion_point(class_scope:istio.mesh.v1alpha1.Topology)
  })
_sym_db.RegisterMessage(Topology)

PrivateKeyProvider = _reflection.GeneratedProtocolMessageType('PrivateKeyProvider', (_message.Message,), {

  'CryptoMb' : _reflection.GeneratedProtocolMessageType('CryptoMb', (_message.Message,), {
    'DESCRIPTOR' : _PRIVATEKEYPROVIDER_CRYPTOMB,
    '__module__' : 'mesh.v1alpha1.proxy_pb2'
    # @@protoc_insertion_point(class_scope:istio.mesh.v1alpha1.PrivateKeyProvider.CryptoMb)
    })
  ,
  'DESCRIPTOR' : _PRIVATEKEYPROVIDER,
  '__module__' : 'mesh.v1alpha1.proxy_pb2'
  # @@protoc_insertion_point(class_scope:istio.mesh.v1alpha1.PrivateKeyProvider)
  })
_sym_db.RegisterMessage(PrivateKeyProvider)
_sym_db.RegisterMessage(PrivateKeyProvider.CryptoMb)

ProxyConfig = _reflection.GeneratedProtocolMessageType('ProxyConfig', (_message.Message,), {

  'ProxyMetadataEntry' : _reflection.GeneratedProtocolMessageType('ProxyMetadataEntry', (_message.Message,), {
    'DESCRIPTOR' : _PROXYCONFIG_PROXYMETADATAENTRY,
    '__module__' : 'mesh.v1alpha1.proxy_pb2'
    # @@protoc_insertion_point(class_scope:istio.mesh.v1alpha1.ProxyConfig.ProxyMetadataEntry)
    })
  ,

  'RuntimeValuesEntry' : _reflection.GeneratedProtocolMessageType('RuntimeValuesEntry', (_message.Message,), {
    'DESCRIPTOR' : _PROXYCONFIG_RUNTIMEVALUESENTRY,
    '__module__' : 'mesh.v1alpha1.proxy_pb2'
    # @@protoc_insertion_point(class_scope:istio.mesh.v1alpha1.ProxyConfig.RuntimeValuesEntry)
    })
  ,

  'ProxyStatsMatcher' : _reflection.GeneratedProtocolMessageType('ProxyStatsMatcher', (_message.Message,), {
    'DESCRIPTOR' : _PROXYCONFIG_PROXYSTATSMATCHER,
    '__module__' : 'mesh.v1alpha1.proxy_pb2'
    # @@protoc_insertion_point(class_scope:istio.mesh.v1alpha1.ProxyConfig.ProxyStatsMatcher)
    })
  ,
  'DESCRIPTOR' : _PROXYCONFIG,
  '__module__' : 'mesh.v1alpha1.proxy_pb2'
  # @@protoc_insertion_point(class_scope:istio.mesh.v1alpha1.ProxyConfig)
  })
_sym_db.RegisterMessage(ProxyConfig)
_sym_db.RegisterMessage(ProxyConfig.ProxyMetadataEntry)
_sym_db.RegisterMessage(ProxyConfig.RuntimeValuesEntry)
_sym_db.RegisterMessage(ProxyConfig.ProxyStatsMatcher)

RemoteService = _reflection.GeneratedProtocolMessageType('RemoteService', (_message.Message,), {
  'DESCRIPTOR' : _REMOTESERVICE,
  '__module__' : 'mesh.v1alpha1.proxy_pb2'
  # @@protoc_insertion_point(class_scope:istio.mesh.v1alpha1.RemoteService)
  })
_sym_db.RegisterMessage(RemoteService)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z\032istio.io/api/mesh/v1alpha1'
  _TRACING_CUSTOMTAGSENTRY._options = None
  _TRACING_CUSTOMTAGSENTRY._serialized_options = b'8\001'
  _PROXYCONFIG_PROXYMETADATAENTRY._options = None
  _PROXYCONFIG_PROXYMETADATAENTRY._serialized_options = b'8\001'
  _PROXYCONFIG_RUNTIMEVALUESENTRY._options = None
  _PROXYCONFIG_RUNTIMEVALUESENTRY._serialized_options = b'8\001'
  _PROXYCONFIG.fields_by_name['discovery_refresh_delay']._options = None
  _PROXYCONFIG.fields_by_name['discovery_refresh_delay']._serialized_options = b'\030\001'
  _PROXYCONFIG.fields_by_name['zipkin_address']._options = None
  _PROXYCONFIG.fields_by_name['zipkin_address']._serialized_options = b'\030\001'
  _PROXYCONFIG.fields_by_name['envoy_metrics_service_address']._options = None
  _PROXYCONFIG.fields_by_name['envoy_metrics_service_address']._serialized_options = b'\030\001'
  _PROXYCONFIG.fields_by_name['availability_zone']._options = None
  _PROXYCONFIG.fields_by_name['availability_zone']._serialized_options = b'\030\001'
  _AUTHENTICATIONPOLICY._serialized_start=5792
  _AUTHENTICATIONPOLICY._serialized_end=5854
  _TRACING._serialized_start=240
  _TRACING._serialized_end=2069
  _TRACING_ZIPKIN._serialized_start=857
  _TRACING_ZIPKIN._serialized_end=891
  _TRACING_LIGHTSTEP._serialized_start=893
  _TRACING_LIGHTSTEP._serialized_end=965
  _TRACING_DATADOG._serialized_start=967
  _TRACING_DATADOG._serialized_end=1002
  _TRACING_STACKDRIVER._serialized_start=1005
  _TRACING_STACKDRIVER._serialized_end=1307
  _TRACING_OPENCENSUSAGENT._serialized_start=1310
  _TRACING_OPENCENSUSAGENT._serialized_end=1541
  _TRACING_OPENCENSUSAGENT_TRACECONTEXT._serialized_start=1440
  _TRACING_OPENCENSUSAGENT_TRACECONTEXT._serialized_end=1541
  _TRACING_CUSTOMTAG._serialized_start=1544
  _TRACING_CUSTOMTAG._serialized_end=1777
  _TRACING_LITERAL._serialized_start=1779
  _TRACING_LITERAL._serialized_end=1810
  _TRACING_ENVIRONMENT._serialized_start=1812
  _TRACING_ENVIRONMENT._serialized_end=1882
  _TRACING_REQUESTHEADER._serialized_start=1884
  _TRACING_REQUESTHEADER._serialized_end=1956
  _TRACING_CUSTOMTAGSENTRY._serialized_start=1958
  _TRACING_CUSTOMTAGSENTRY._serialized_end=2059
  _SDS._serialized_start=2071
  _SDS._serialized_end=2141
  _TOPOLOGY._serialized_start=2144
  _TOPOLOGY._serialized_end=2460
  _TOPOLOGY_FORWARDCLIENTCERTDETAILS._serialized_start=2324
  _TOPOLOGY_FORWARDCLIENTCERTDETAILS._serialized_end=2460
  _PRIVATEKEYPROVIDER._serialized_start=2463
  _PRIVATEKEYPROVIDER._serialized_end=2645
  _PRIVATEKEYPROVIDER_CRYPTOMB._serialized_start=2565
  _PRIVATEKEYPROVIDER_CRYPTOMB._serialized_end=2633
  _PROXYCONFIG._serialized_start=2648
  _PROXYCONFIG._serialized_end=5552
  _PROXYCONFIG_PROXYMETADATAENTRY._serialized_start=5049
  _PROXYCONFIG_PROXYMETADATAENTRY._serialized_end=5113
  _PROXYCONFIG_RUNTIMEVALUESENTRY._serialized_start=5115
  _PROXYCONFIG_RUNTIMEVALUESENTRY._serialized_end=5179
  _PROXYCONFIG_PROXYSTATSMATCHER._serialized_start=5182
  _PROXYCONFIG_PROXYSTATSMATCHER._serialized_end=5340
  _PROXYCONFIG_TRACINGSERVICENAME._serialized_start=5342
  _PROXYCONFIG_TRACINGSERVICENAME._serialized_end=5450
  _PROXYCONFIG_INBOUNDINTERCEPTIONMODE._serialized_start=5452
  _PROXYCONFIG_INBOUNDINTERCEPTIONMODE._serialized_end=5513
  _REMOTESERVICE._serialized_start=5555
  _REMOTESERVICE._serialized_end=5790
# @@protoc_insertion_point(module_scope)
