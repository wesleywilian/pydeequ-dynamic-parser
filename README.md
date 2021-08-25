
# pydeequ-dynamic-parser

Python library which makes it possible to use validation rules in [pydeequ](https://github.com/awslabs/python-deequ) based on json/dict structures.

# Installing

```shell
pip install PydeequDynamicParser
```

# Usage

```python
# User Dynamic Checks
all_checks = [{"name": "isUnique", "parameters": {"column": "COLUMN_NAME", "hint": "Hint here"}},
              {"name": "satisfies", "parameters": {"columnCondition": "(LENGTH(COLUMN_NAME) = 11 OR LENGTH(COLUMN_NAME) = 14) ", "constraintName": "COLUMN_NAME length validate", "assertion": "lambda x: x == 1.0", "hint": None}},
              {"name": "containsEmail", "parameters": {"column": "COLUMN_NAME", "assertion": None, "hint": None}},
              {"name": "isComplete", "parameters": {"column": "COLUMN_NAME", "hint": None}}]

# PyDeequ constraint dynamic constraint based on "all_checks"
from pydeequ.checks import Check
from pydeequ.checks import CheckLevel
from pydeequ.verification import VerificationSuite
from pydeequ.verification import VerificationResult
import PydeequDynamicParser

check = Check(spark, CheckLevel.Error, "Check Name")
check_instance_parsed = PydeequDynamicParser.Parser(check, all_checks).parse()
checkResult = VerificationSuite(spark).onData(df).addCheck(check_instance_parsed).run()
checkResult_df = VerificationResult.checkResultsAsDataFrame(spark, checkResult)

checkResult_df.toPandas()
```

As we can see the line responsible for executing the parse will translate de user json/dict to PyDeequ Check instance.

```python
import PydeequDynamicParser
check_instance_parsed = PydeequDynamicParser.Parser(check, all_checks).parse()
```

# Currently supported validations
- Constraints
  - isUnique
  - satisfies
  - containsEmail
  - isComplete
