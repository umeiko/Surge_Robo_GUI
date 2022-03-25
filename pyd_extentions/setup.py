from distutils.core import setup, Extension
from Cython.Build import cythonize

extension = Extension(
    "joyCtrlFuncs",
    ["joyCtrlFuncs.pyx"],
)

setup(
      ext_modules=cythonize("joyCtrlFuncs.pyx")
    )