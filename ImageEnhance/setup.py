from distutils.core import setup
import py2exe

setup(
    console=["test.py"],

    options={
    "py2exe":
        {
            "dll_excludes": ["MSVCP90.dll","libzmq.pyd",
            "geos_c.dll",
            "MSVFW32.dll", 
            "AVIFIL32.dll", 
            "AVICAP32.dll", 
            "ADVAPI32.dll", 
            "CRYPT32.dll", 
            "WLDAP32.dll"
            "api-ms-win-core-string-l1-1-0.dll",
            "api-ms-win-security-base-l1-1-0.dll",
            "api-ms-win-core-registry-l2-1-0.dll",
            "api-ms-win-core-registry-l1-1-0.dll",
            "api-ms-win-core-processthreads-l1-1-0.dll",
            "api-ms-win-core-file-l1-1-0.dll",
            "api-ms-win-core-errorhandling-l1-1-1.dll",
            "api-ms-win-security-base-l1-1-0.dll",
            "api-ms-win-core-localization-l1-2-0.dll",
            "api-ms-win-core-stringansi-l1-1-0.dll",
            "api-ms-win-core-heap-obsolete-l1-1-0.dll",
            "api-ms-win-core-string-l2-1-0.dll",
            "api-ms-win-core-atoms-l1-1-0.dll",
            "api-ms-win-core-profile-l1-1-0.dll",
            "api-ms-win-core-string-obsolete-l1-1-0.dll",
            "api-ms-win-core-largeinteger-l1-1-0.dll",
            "api-ms-win*.dll",
            "api-ms-win-core-processthreads-l1-1-2.dll",
            "api-ms-win-core-libraryloader-l1-2-1.dll",
            "api-ms-win-core-file-l1-2-1.dll",
            "api-ms-win-security-base-l1-2-0.dll",
            "api-ms-win-eventing-provider-l1-1-0.dll",
            "api-ms-win-core-heap-l2-1-0.dll",
            "api-ms-win-core-libraryloader-l1-2-0.dll",
            "api-ms-win-core-localization-l1-2-1.dll",
            "api-ms-win-core-sysinfo-l1-2-1.dll",
            "api-ms-win-core-synch-l1-2-0.dll",
            "api-ms-win-core-heap-l1-2-0.dll",
            "api-ms-win-core-handle-l1-1-0.dll",
            "api-ms-win-core-io-l1-1-1.dll",
            "api-ms-win-core-com-l1-1-1.dll",
            "api-ms-win-core-memory-l1-1-2.dll",
            "api-ms-win-core-version-l1-1-1.dll",
            "api-ms-win-core-version-l1-1-0.dll"] 
        }
    }
    )

