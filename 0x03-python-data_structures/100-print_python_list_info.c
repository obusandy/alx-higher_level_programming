#include <Python.h>
#include <stdio.h>

/**
 * print_python_list_info - Prints information about a PyListObject
 * @p: Pointer to the PyObject
 */
void print_python_list_info(PyObject *p) {
    Py_ssize_t list_size = 0;
    int index = 0;

    if (PyList_CheckExact(p)) {
        list_size = PyList_Size(p);

        printf("[*] Size of the Python List = %zd\n", list_size);
        printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);

        while (index < list_size) {
            printf("Element %d: %s\n",
                   index, Py_TYPE(PyList_GetItem(p, index))->tp_name);
            index++;
        }
    }
}
