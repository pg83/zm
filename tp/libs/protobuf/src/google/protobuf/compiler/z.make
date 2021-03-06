module: library

depends:
- tp/libs/protobuf

c_flags:
- -w

srcs:
- main.cc
- code_generator.cc
- command_line_interface.cc
- plugin.cc
- plugin.pb.cc
- subprocess.cc
- zip_writer.cc
- cpp/cpp_enum.cc
- cpp/cpp_enum_field.cc
- cpp/cpp_extension.cc
- cpp/cpp_field.cc
- cpp/cpp_file.cc
- cpp/cpp_generator.cc
- cpp/cpp_helpers.cc
- cpp/cpp_map_field.cc
- cpp/cpp_message.cc
- cpp/cpp_message_field.cc
- cpp/cpp_padding_optimizer.cc
- cpp/cpp_primitive_field.cc
- cpp/cpp_service.cc
- cpp/cpp_string_field.cc
- java/java_context.cc
- java/java_enum.cc
- java/java_enum_lite.cc
- java/java_enum_field.cc
- java/java_enum_field_lite.cc
- java/java_extension.cc
- java/java_extension_lite.cc
- java/java_field.cc
- java/java_file.cc
- java/java_generator.cc
- java/java_generator_factory.cc
- java/java_helpers.cc
- java/java_map_field.cc
- java/java_map_field_lite.cc
- java/java_message.cc
- java/java_message_lite.cc
- java/java_message_builder.cc
- java/java_message_builder_lite.cc
- java/java_message_field.cc
- java/java_message_field_lite.cc
- java/java_name_resolver.cc
- java/java_primitive_field.cc
- java/java_primitive_field_lite.cc
- java/java_shared_code_generator.cc
- java/java_service.cc
- java/java_string_field.cc
- java/java_string_field_lite.cc
- java/java_doc_comment.cc
- js/js_generator.cc
- js/well_known_types_embed.cc
- objectivec/objectivec_enum.cc
- objectivec/objectivec_enum_field.cc
- objectivec/objectivec_extension.cc
- objectivec/objectivec_field.cc
- objectivec/objectivec_file.cc
- objectivec/objectivec_generator.cc
- objectivec/objectivec_helpers.cc
- objectivec/objectivec_map_field.cc
- objectivec/objectivec_message.cc
- objectivec/objectivec_message_field.cc
- objectivec/objectivec_oneof.cc
- objectivec/objectivec_primitive_field.cc
- php/php_generator.cc
- python/python_generator.cc
- ruby/ruby_generator.cc
- csharp/csharp_doc_comment.cc
- csharp/csharp_enum.cc
- csharp/csharp_enum_field.cc
- csharp/csharp_field_base.cc
- csharp/csharp_generator.cc
- csharp/csharp_helpers.cc
- csharp/csharp_map_field.cc
- csharp/csharp_message.cc
- csharp/csharp_message_field.cc
- csharp/csharp_primitive_field.cc
- csharp/csharp_reflection_class.cc
- csharp/csharp_repeated_enum_field.cc
- csharp/csharp_repeated_message_field.cc
- csharp/csharp_repeated_primitive_field.cc
- csharp/csharp_source_generator_base.cc
- csharp/csharp_wrapper_field.cc
