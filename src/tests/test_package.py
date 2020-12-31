import sys

import pyomo_kernel_extensions

is_pypy = False
try:
    import __pypy__  # noqa: F401

    is_pypy = True
except ImportError:
    is_pypy = False


class Test:

    # See what Python versions the combined
    # coverage report includes
    def test_show_coverage(self):
        if sys.platform.startswith("linux"):
            assert sys.version_info.major == 3
            if not is_pypy:
                if sys.version_info.minor == 6:
                    print(sys.version_info)
                elif sys.version_info.minor == 7:
                    print(sys.version_info)
                elif sys.version_info.minor == 8:
                    print(sys.version_info)
                elif sys.version_info.minor == 9:
                    print(sys.version_info)
            if is_pypy:
                if sys.version_info.minor == 6:
                    print(sys.version_info)
        elif sys.platform.startswith("darwin"):
            assert sys.version_info.major == 3
            if not is_pypy:
                if sys.version_info.minor == 6:
                    print(sys.version_info)
                elif sys.version_info.minor == 7:
                    print(sys.version_info)
                elif sys.version_info.minor == 8:
                    print(sys.version_info)
                elif sys.version_info.minor == 9:
                    print(sys.version_info)
            if is_pypy:
                if sys.version_info.minor == 6:
                    print(sys.version_info)
        elif sys.platform.startswith("win32"):
            assert sys.version_info.major == 3
            if not is_pypy:
                if sys.version_info.minor == 6:
                    print(sys.version_info)
                elif sys.version_info.minor == 7:
                    print(sys.version_info)
                elif sys.version_info.minor == 8:
                    print(sys.version_info)
                elif sys.version_info.minor == 9:
                    print(sys.version_info)
            if is_pypy:
                if sys.version_info.minor == 6:
                    print(sys.version_info)

    def test_version(self):
        pyomo_kernel_extensions.__version__
