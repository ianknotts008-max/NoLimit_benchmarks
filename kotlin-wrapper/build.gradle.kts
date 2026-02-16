// Gradle build file for Kotlin wrapper
// This wrapper is archived and provided only as an example.

plugins {
    kotlin("jvm") version "1.5.0"
}

repositories {
    mavenCentral()
}

dependencies {
    implementation(kotlin("stdlib"))
}
