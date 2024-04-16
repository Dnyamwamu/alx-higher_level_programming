#include <Python.h>
#include <stdio.h>

/**
 * print_python_list_info - prints basic info about Python lists
 * @p: pointer to a Python object
 */
void print_python_list_info(PyObject *p)
{
    Py_ssize_t size, alloc;
    Py_ssize_t i;
    PyObject *item;

    size = PyList_Size(p);
    alloc = ((PyListObject *)p)->allocated;

    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", alloc);

    for (i = 0; i < size; i++)
    {
        item = PyList_GetItem(p, i);
        printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
    }
}
