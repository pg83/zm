#include <semaphore.h>
#include <signal.h>
#include <stdio.h>
#include <string.h>

#include <library/cpp/testing/unittest/registar.h>

void handler(int sig)
{
    Y_UNUSED(sig);
}

Y_UNIT_TEST_SUITE(SemWaitSuite)
{
    Y_UNIT_TEST(TestSignalInterruptsSemWait)
    {
        // Don't use SetAsyncSignalHandler - we don't need to set SA_RESTART sa_flag
        struct sigaction sa;

        memset(&sa, 0, sizeof(struct sigaction));
        sa.sa_handler = handler;
        sigemptyset(&(sa.sa_mask));
        sa.sa_flags = 0;
        Y_VERIFY(sigaction(SIGALRM, &sa, nullptr) == 0);

        sem_t x;
        sem_init(&x, 0, 0);
        alarm(1);
        // sem_wait should be interrupted. Otherwise, test will timeout
        sem_wait(&x);
        sem_destroy(&x);

        sa.sa_handler = SIG_DFL;
        Y_VERIFY(sigaction(SIGALRM, &sa, nullptr) == 0);
    }
};
