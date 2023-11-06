#include <Python.h>
#include <stdio.h>

/**
 * print_python_list_info - Prints information about a PyListObject
 * @p: Pointer to the PyObject
 */
void print_python_list_info(PyObject *py_list)
{
    Py_ssize_t list_size = 0;
    int elmindx = 0;

    if (PyList_CheckExact(py_list))
    {
        list_size = PyList_Size(py_list);

        printf("[*] Size of the Python List = %zd\n", list_size);
        printf("[*] Allocated = %lu\n", ((PyListObject *)py_list)->allocated);

        while (elmindx < list_size)
	{
            printf("Element %d: %s\n",
                   elmindx, Py_TYPE(PyList_GetItem(py_list, elmindx))->tp_name);
            elmindx++;
        }
    }
}
