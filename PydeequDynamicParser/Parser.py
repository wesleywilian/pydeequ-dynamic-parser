import json

class pydeequDynamicParser:
    pydeequ_check_instance = None
    user_checks = None
    functions_map = None
    
    def __init__(self, pydeequ_check_instance, user_checks):
        self.pydeequ_check_instance = pydeequ_check_instance
        self.user_checks = json.loads(user_checks) if type(user_checks) is str else user_checks
        self.functions_map = {"satisfies": self.dq_satisfies,
                 "isUnique": self.dq_isunique,
                 "containsEmail": self.dq_contains_email,
                 "isComplete": self.dq_is_complete}
        
    @staticmethod
    def validate_eval(assertion):
        if assertion is None:
            return assertion
        else:
            return eval(assertion)
    
    def dq_satisfies(self, columnCondition, constraintName, assertion, hint):
        self.pydeequ_check_instance = self.pydeequ_check_instance.satisfies(columnCondition, constraintName, self.validate_eval(assertion), hint)

    def dq_isunique(self, column, hint):
        self.pydeequ_check_instance = self.pydeequ_check_instance.isUnique(column, hint)

    def dq_contains_email(self, column, assertion, hint):
        self.pydeequ_check_instance = self.pydeequ_check_instance.containsEmail(column, self.validate_eval(assertion), hint)

    def dq_is_complete(self, column, hint):
        self.pydeequ_check_instance = self.pydeequ_check_instance.isComplete(column, hint)   

    def parse(self):
        # add all constraints into pydeequ check instance
        for current_check in self.user_checks:
            current_name = current_check['name']
            current_parameters = current_check['parameters']
            self.functions_map[current_name](**current_parameters)
        return self.pydeequ_check_instance
