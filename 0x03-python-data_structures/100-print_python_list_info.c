#include <object.h>
#include <Python.h>
#include <listobject.h>

void print_python_list_info(PyObject *p)
{
	int i;
	long int Size = PyList_Size(p);

	PyListObject *obj = (PyListObject *)p;

	printf("[*] Size of the Python List = %li\n", Size);
	printf("[*] Allocated = %li\n", obj->allocated);
	for (i = 0; i < Size; i++)
		printf("Element %i: %s\n", i, Py_TYPE(obj->ob_item[i])->tp_name);
}
