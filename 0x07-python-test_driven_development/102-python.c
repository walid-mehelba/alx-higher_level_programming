#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <stdio.h>

/**
 * print_python_string - Prints a Python string
 * @p: The PyObject to print
 *
 * This function checks if the given PyObject is a string.
 * If it is, it prints its length and value. Otherwise, it
 * prints an error message.
 */
void print_python_string(PyObject *p)
{
    if (!PyUnicode_Check(p))
    {
        printf("Invalid PyObject: expected a string\n");
        return;
    }

    Py_ssize_t length = PyUnicode_GetLength(p);
    const char *value = PyUnicode_AsUTF8(p);

    printf("Python String:\n");
    printf("  Length: %zd\n", length);
    printf("  Value: %s\n", value);
}
