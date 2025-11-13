#include <math.h>
#include <stdio.h>

#include "types.h"

#ifndef M_PI
#define M_PI 3.141592653589793238462643383
#endif

void FFT(f64 *x, usize N, f64 *Xr, f64 *Xi) {
    // 0. Precompute.
    usize levels = 0;
    usize n = N;
    for (; n; n >>= 1)
        levels++;
    levels--;

    // 1. Bit reversal permutation.
    // NOTE Probably use a LUT for bit reversals?
    for (usize i = 0; i < N; i++) {
        // can be done more efficiently but i wanted to get something working
        usize ii = i, ri = 0;
        for (usize j = 0; j < levels; j++) {
            ri |= ii & 1;
            ii >>= 1;
            ri <<= 1;
        }
        ri >>= 1;

        Xr[ri] = x[i],
        Xi[ri] = 0.0;
    }

    // 2. Iterative Butterfly stages.
    // Direct translation of the Python code.
    usize size = 2;
    while (size <= N) {
        usize half_size = size / 2;
        for (usize i = 0; i < N; i += size) {
            for (usize k = 0; k < half_size; k++) {
                // Compute twiddle factor.
                f64 twiddle_r =  cos(2 * M_PI * k / (f64) size);
                f64 twiddle_i = -sin(2 * M_PI * k / (f64) size);

                f64 qr = twiddle_r * Xr[i + k + half_size] - twiddle_i * Xi[i + k + half_size];
                f64 qi = twiddle_r * Xi[i + k + half_size] + twiddle_i * Xr[i + k + half_size];

                Xr[i + k + half_size] = Xr[i + k] - qr;
                Xi[i + k + half_size] = Xi[i + k] - qi;

                Xr[i + k] = Xr[i + k] + qr;
                Xi[i + k] = Xi[i + k] + qi;
            }
        }
        size *= size;
    }
}

i32 main(void) {
    // Test the FFT.

    // [1 0 0 0] → [1 1 1 1]
    // [0 1 0 1] → [2 0 -2 0]
    // [1 1 0 0] → [2 1j-1 0 1j1]
    // [1 1 1 1] → [4 0 0 0]

    f64 x[4] = {1, 0, 0, 0};
    f64 Xr[4], Xi[4];

    FFT(x, 4, Xr, Xi);
    printf("[%.1lfj%.1lf %.1lfj%.1lf %.1lfj%.1lf %.1lfj%.1lf]\n", Xr[0], Xi[0], Xr[1], Xi[1], Xr[2], Xi[2], Xr[3], Xi[3]);

    x[0] = 0; x[1] = 1; x[2] = 0; x[3] = 1;
    FFT(x, 4, Xr, Xi);
    printf("[%.1lfj%.1lf %.1lfj%.1lf %.1lfj%.1lf %.1lfj%.1lf]\n", Xr[0], Xi[0], Xr[1], Xi[1], Xr[2], Xi[2], Xr[3], Xi[3]);

    x[0] = 1; x[1] = 1; x[2] = 0; x[3] = 0;
    FFT(x, 4, Xr, Xi);
    printf("[%.1lfj%.1lf %.1lfj%.1lf %.1lfj%.1lf %.1lfj%.1lf]\n", Xr[0], Xi[0], Xr[1], Xi[1], Xr[2], Xi[2], Xr[3], Xi[3]);

    x[0] = 1; x[1] = 1; x[2] = 1; x[3] = 1;
    FFT(x, 4, Xr, Xi);
    printf("[%.1lfj%.1lf %.1lfj%.1lf %.1lfj%.1lf %.1lfj%.1lf]\n", Xr[0], Xi[0], Xr[1], Xi[1], Xr[2], Xi[2], Xr[3], Xi[3]);

    return 0;
}
