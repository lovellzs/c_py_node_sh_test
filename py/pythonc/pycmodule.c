#include "Python.h"

static PyObject *
Extest_fac(PyObject *self, PyObject *args)
{
    int num;
    if (!PyArg_ParseTuple(args, "i", &num))
        return NULL;
    return (PyObject*)Py_BuildValue("i", fac(num));
}

static PyObject *
Extest_doppel(PyObject *self, PyObject *args)
{
    char *orig_str;
    char *dupe_str;
    PyObject* retval;

    if (!PyArg_ParseTuple(args, "s", &orig_str))
        return NULL;
    retval = (PyObject*)Py_BuildValue("ss", orig_str,
        dupe_str=reverse(strdup(orig_str)));
    free(dupe_str);             //#防止内存泄漏
    return retval;
}

static PyObject *
Extest_test(PyObject *self, PyObject *args)
{
    test();
    return (PyObject*)Py_BuildValue("");
}

static PyMethodDef
ExtestMethods[] =
{
    { "fac", Extest_fac, METH_VARARGS },
    { "doppel", Extest_doppel, METH_VARARGS },
    { "test", Extest_test, METH_VARARGS },
    { NULL, NULL },
};

void initExtest()
{
    Py_InitModule("Extest", ExtestMethods);
}