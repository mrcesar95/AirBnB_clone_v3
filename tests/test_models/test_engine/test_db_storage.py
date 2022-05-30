#!/usr/bin/python3
"""
Contains the TestDBStorageDocs and TestDBStorage classes
"""

from datetime import datetime
import inspect
import models
from models.engine import db_storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import json
import os
import pep8
import unittest
DBStorage = db_storage.DBStorage
classes = {"Amenity": Amenity, "City": City, "Place": Place,
           "Review": Review, "State": State, "User": User}


class TestDBStorageDocs(unittest.TestCase):
    """Tests to check the documentation and style of DBStorage class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.dbs_f = inspect.getmembers(DBStorage, inspect.isfunction)

    def test_pep8_conformance_db_storage(self):
        """Test that models/engine/db_storage.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/engine/db_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_db_storage(self):
        """Test tests/test_models/test_db_storage.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_engine/\
test_db_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_db_storage_module_docstring(self):
        """Test for the db_storage.py module docstring"""
        self.assertIsNot(db_storage.__doc__, None,
                         "db_storage.py needs a docstring")
        self.assertTrue(len(db_storage.__doc__) >= 1,
                        "db_storage.py needs a docstring")

    def test_db_storage_class_docstring(self):
        """Test for the DBStorage class docstring"""
        self.assertIsNot(DBStorage.__doc__, None,
                         "DBStorage class needs a docstring")
        self.assertTrue(len(DBStorage.__doc__) >= 1,
                        "DBStorage class needs a docstring")

    def test_dbs_func_docstrings(self):
        """Test for the presence of docstrings in DBStorage methods"""
        for func in self.dbs_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))

        def test_dbs_func_undecorated_pep8(self):
            """Test that DBStorage methods are PEP8 compliant"""
            for func in self.dbs_f:
                self.assertTrue(pep8.check_func(func[1]),
                                "{:s} is not pep8 compliant".format(func[0]))


class TestDBStorage(unittest.TestCase):
    """Tests for DBStorage class"""

    def setUp(self):
        """Set up for each test"""
        self.dbs = DBStorage()
        self.dbs.reload()

    def tearDown(self):
        """Tear down after each test"""
        del self.dbs

    def test_dbs_attributes(self):
        """Test for the presence of attributes"""
        self.assertTrue(hasattr(self.dbs, "file_path"))
        self.assertTrue(hasattr(self.dbs, "all"))

    def test_dbs_file_path(self):
        """Test for the correct file path"""
        self.assertEqual(self.dbs.file_path, "file.json")

    def test_dbs_all(self):
        """Test for the all attribute"""
        self.assertEqual(type(self.dbs.all), dict)

    def test_dbs_new(self):
        """Test for the new method"""
        self.dbs.new(BaseModel())
        self.assertEqual(len(self.dbs.all), 1)

    def test_dbs_save(self):
        """Test for the save method"""
        self.dbs.save()
        self.assertTrue(os.path.isfile("file.json"))

    def test_dbs_reload(self):
        """Test for the reload method"""
        self.dbs.reload()
        self.assertEqual(len(self.dbs.all), 0)

    def test_dbs_delete(self):
        """Test for the delete method"""
        self.dbs.delete(self.dbs.all.keys()[0])
        self.assertEqual(len(self.dbs.all), 0)

    def test_dbs_get(self):
        """Test for the get method"""
        self.dbs.get(self.dbs.all.keys()[0])
        self.assertEqual(len(self.dbs.all), 0)

    def test_dbs_count(self):
        """Test for the count method"""
        self.assertEqual(self.dbs.count(), 0)


class TestFileStorage(unittest.TestCase):
    """Test the FileStorage class"""
    @unittest.skipIf(models.storage_t != 'db', "not testing db storage")
    def test_all_returns_dict(self):
        """Test that all returns a dictionaty"""
        self.assertIs(type(models.storage.all()), dict)

    @unittest.skipIf(models.storage_t != 'db', "not testing db storage")
    def test_all_no_class(self):
        """Test that all returns all rows when no class is passed"""

    @unittest.skipIf(models.storage_t != 'db', "not testing db storage")
    def test_new(self):
        """test that new adds an object to the database"""

    @unittest.skipIf(models.storage_t != 'db', "not testing db storage")
    def test_save(self):
        """Test that save properly saves objects to file.json"""

        @unittest.skipIf(models.storage_t != 'db', "not testing db storage")
        def test_reload(self):
            """Test that reload properly reloads objects from file.json"""

        @unittest.skipIf(models.storage_t != 'db', "not testing db storage")
        def test_delete(self):
            """Test that delete properly deletes objects from file.json"""

        @unittest.skipIf(models.storage_t != 'db', "not testing db storage")
        def test_get(self):
            """Test that get properly gets objects from file.json"""

        @unittest.skipIf(models.storage_t != 'db', "not testing db storage")
        def test_count(self):
            """Test that count returns the correct number of objects"""
