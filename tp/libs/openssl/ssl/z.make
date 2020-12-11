module: library

depends:
- tp/libs/openssl/crypto

inc_dirs:
- tp/libs/openssl
- tp/libs/openssl/include

c_flags:
- -DL_ENDIAN
- -DOPENSSLDIR="/usr/local/ssl"
- -DENGINESDIR="/usr/local/lib/engines-1.1"
- -D_REENTRANT

srcs:
- bio_ssl.c
- d1_lib.c
- d1_msg.c
- d1_srtp.c
- methods.c
- packet.c
- pqueue.c
- record/dtls1_bitmap.c
- record/rec_layer_d1.c
- record/rec_layer_s3.c
- record/ssl3_buffer.c
- record/ssl3_record.c
- record/ssl3_record_tls13.c
- s3_cbc.c
- s3_enc.c
- s3_lib.c
- s3_msg.c
- ssl_asn1.c
- ssl_cert.c
- ssl_ciph.c
- ssl_conf.c
- ssl_err.c
- ssl_init.c
- ssl_lib.c
- ssl_mcnf.c
- ssl_rsa.c
- ssl_sess.c
- ssl_stat.c
- ssl_txt.c
- ssl_utst.c
- statem/extensions.c
- statem/extensions_clnt.c
- statem/extensions_cust.c
- statem/extensions_srvr.c
- statem/statem.c
- statem/statem_clnt.c
- statem/statem_dtls.c
- statem/statem_lib.c
- statem/statem_srvr.c
- t1_enc.c
- t1_lib.c
- t1_trce.c
- tls13_enc.c
- tls_srp.c
