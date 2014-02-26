import unittest
from datetime import datetime as dt
from odml import Property, Section, Document

longago = dt.strptime('2013-08-11 09:48:49', "%Y-%m-%d %H:%M:%S")
recently = dt.strptime('2014-02-25 14:42:13', "%Y-%m-%d %H:%M:%S")


class TestValidation(unittest.TestCase):

    def setUp(self):
        doc = Document("author")
        sec = Section("foo", "footype")
        doc.append(sec)
        sec.append(Property("strprop", "somestring"))
        sec.append(Property("txtprop", "some\ntext"))
        sec.append(Property("intprop", 200))
        sec.append(Property("floatprop", 2.00))
        sec.append(Property("datetimeprop", longago))
        sec.append(Property("dateprop", longago.date()))
        sec.append(Property("timeprop", longago.time()))
        sec.append(Property("boolprop", True))

        sec = Section("bar", "bartype")
        doc.append(sec)
        sec.append(Property("strprop", "otherstring"))
        sec.append(Property("txtprop", "other\ntext"))
        sec.append(Property("intprop", 300))
        sec.append(Property("floatprop", 3.00))
        sec.append(Property("datetimeprop", dt.now()))
        sec.append(Property("dateprop", dt.now().date()))
        sec.append(Property("timeprop", dt.now().time()))
        sec.append(Property("boolprop", True))

        self.doc = doc

    def test_itersections(self):
        filter_func = lambda x: getattr(x, 'name').find("foo") > -1
        assert(len(self.doc.itersections(recursive=True, filter_func=filter_func)) == 1)

        filter_func = lambda x: getattr(x, 'type').find("foo") > -1
        assert(len(self.doc.itersections(recursive=True, filter_func=filter_func)) == 1)


if __name__ == '__main__':
    unittest.main()