#ifndef Py_PYTHON_H
#define Py_PYTHON_H

#include <stddef.h>

typedef struct {
  PyObject_HEAD
  int ob_refcnt;
  struct _typeobject *ob_type;
} PyObject;
void print_python_list_info(PyObject *py_list)
#endif
