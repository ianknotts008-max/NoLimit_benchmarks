package com.boundless.benchmark

/**
 * Archived example stub kept for historical reference only.
 *
 * The public proof repository uses a pre-compiled JAR; this Kotlin object is
 * no longer part of the active benchmark pipeline.
 */
object NoLimitBenchmarkStub {

    /**
     * Returns a [CompressionResult] with realistic, hard-coded metrics.
     *
     * The actual NoLimit engine is proprietary and not included here.
     *
     * @param data Raw bytes to (nominally) compress.
     * @return A [CompressionResult] representing the stub's fixed output.
     */
    fun compress(data: ByteArray): CompressionResult = CompressionResult(
        ratio = 0.952,
        timeMs = 156L,
        entropy = 4.2,
    )
}

/**
 * Holds the output metrics from a single compression run.
 *
 * @property ratio Compression ratio achieved (0–1, higher is better).
 * @property timeMs Wall-clock time in milliseconds.
 * @property entropy Shannon entropy of the compressed output.
 */
data class CompressionResult(
    val ratio: Double,
    val timeMs: Long,
    val entropy: Double,
)
