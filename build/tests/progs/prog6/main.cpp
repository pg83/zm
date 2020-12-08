#include <openssl/bio.h>
#include <openssl/ssl.h>
#include <openssl/err.h>
#include <openssl/rand.h>
#include <openssl/conf.h>
#include <openssl/crypto.h>

int main() {
    OPENSSL_init_crypto(OPENSSL_INIT_NO_ATEXIT, nullptr);
    SSL_library_init();
    SSL_load_error_strings();
    OpenSSL_add_all_algorithms();
    ERR_load_BIO_strings();
}
