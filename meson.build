project(
   'test-resize',
   'c', 'cython',
   version: '0.0.1',
   license: 'MIT',
)

cython = find_program('cython')
py = import('python').find_installation(pure: false)

py.extension_module(
  'test',
  'test.pyx',
  install: true,
  subdir: 'test_resize',
)

py.install_sources(
 ['__init__.py', 'test_py.py'],
  subdir: 'test_resize',
)