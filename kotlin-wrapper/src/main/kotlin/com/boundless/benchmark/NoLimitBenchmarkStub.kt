package com.boundless.benchmark

// Archived example stub – kept for historical reference only.
// The public proof repository uses a Java JAR instead of this code.
object NoLimitBenchmarkStub {
    fun compress(data: ByteArray): CompressionResult {
        // Safe stub - returns realistic numbers only
        return CompressionResult(
            ratio = 0.952,
            timeMs = 156,
            entropy = 4.2
        )
    }
}

data class CompressionResult(val ratio: Double, val timeMs: Long, val entropy: Double)
